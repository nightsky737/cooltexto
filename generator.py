#session['smth'] = 'smth' makes it for the browser tab
from flask import *
import numpy as np
import os 
import random
from numpy import linalg as LA


os.chdir("word_data") #crappy way to do it.

common_words = set() #https://github.com/first20hours/google-10000-english
with open("wordsfiltered.txt", "r", encoding='utf-8') as file:
    for line in file:
        common_words.add(line[:-1]) #Omitting the /n


stop_words = set() #https://github.com/stopwords-iso/stopwords-en/blob/master/stopwords-en.txt
with open( "english.txt", "r", encoding='utf-8') as file:
    for line in file:
        stop_words.add(line[:-1])

def filter(word):
    '''
    If its common, not a stop word, or too short:
    Returns false.
    common_words.get(word)
    '''
    return (word in common_words) and (not (word in stop_words )) and len(word) > 3

def load_embeddings(file_path):
    embeddings = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            embeddings[word] = np.asarray(values[1:], dtype='float32')
    return embeddings

embeddings = load_embeddings('glove.6B.300d.txt') 

os.chdir("..")

def get_cos_sims(word):
    '''give it a word and it will return a dictionary of the cosine sims'''
    def cosine_sim(a, b):
        return np.dot(a, b) / (LA.norm(a) * LA.norm(b))
    cos_sims = {} #First word alphabetically -> Similarity with word
    for other_word in embeddings:
        cos_sims[other_word] = cosine_sim (embeddings[other_word], embeddings[word])
    return cos_sims

def order(word):
    '''picks word and orders it. Returns a dictionary of Words -> Ranking
    cause aint no way we repeatedly searching for stuff in a 6b long list
    '''
    all_words_list = list(embeddings.keys())
    cos_sims = get_cos_sims(word)
    all_words_list.sort(key=lambda x: cos_sims[x], reverse=True)
    return dict(zip(all_words_list, [i for i in range(len(all_words_list))]))

def generate_orderings(debug=False):
    word = random.choice(list(embeddings.keys()))

    while(not filter(word)):
        word = random.choice(list(embeddings.keys()))
    if debug:
        print(f"generating for {word}")
    ret = order(word)
    session['current_ordering'] = ret
    session['current_word'] = word
    session['user_guessed_ordering'] = []
    return ret


def get_current_word():
    return session['current_word']


def guess(guess):
    ordering = session.get('current_ordering')

    if not ordering:
        return "ahahaha welcome to debugging pain"

    if guess not in ordering:
        return "not found"
        
    if guess in session['user_guessed_ordering']:
        return "already guessed"
        
    if session['current_ordering'][guess] != 0:
        session['user_guessed_ordering'].append(guess)
    return ordering[guess]

#I guess we also need rankings? ATP we might just make a separate endpoint that gets the list of words?
def get_guesses():
        #Sorts and returns sorted dictionary of the user's previously guessed stuff

    ordering = session.get('current_ordering')
    guesses = session.get('user_guessed_ordering')

    if not ordering:
        print( "Ordering not yet created. this should not be happening")

    if guesses == None:
        print( "Guesses not yet created. this should not be happening")

    if ordering != None and guesses != None:
        sorted_guesses = sorted(guesses, key=lambda x: session['current_ordering'][x])

        return [(word, session['current_ordering'][word]) for word in sorted_guesses]
 