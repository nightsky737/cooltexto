#session['smth'] = 'smth' makes it for the browser tab
from flask import *
import numpy as np
import os 
import random
from numpy import linalg as LA


os.chdir("word_data") #crappy way to do it.

common_words = {} #https://github.com/first20hours/google-10000-english
with open("common_words.txt", "r", encoding='utf-8') as file:
    for line in file:
        common_words[line[:-1]] = True #Omitting the /n


stop_words = {} #https://github.com/stopwords-iso/stopwords-en/blob/master/stopwords-en.txt
with open( "stopwords-en.txt", "r", encoding='utf-8') as file:
    for line in file:
        stop_words[line[:-1]] = True

def filter(word):
    '''
    If its common, a stop word, or too short:
    Returns false.
    common_words.get(word)
    '''
    return (common_words.get(word)) and (not stop_words.get(word)) and len(word) > 3

def load_embeddings(file_path):
    embeddings = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            if(filter(word)):
                vector = np.asarray(values[1:], dtype='float32')
                embeddings[word] = vector
    return embeddings

embeddings = load_embeddings('glove.6B.200d.txt')

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
    print(word)
    if debug:
        print(f"generating for {word}")
    ret = order(word)
    session['current_ordering'] = ret
    session['current_word'] = word
    # print("Setting session ordering with", len(ret), "items")

    return ret
def get_current_word():
    return session['current_word']


def guess(guess):
    ordering = session['current_ordering']

    if not ordering:
        return "ahahaha welcome to debugging hell"
        abort(400, description="No ordering found. Generate one first.")

    if guess not in ordering:
        return "not found in ordering guess again"
        abort(400, description=f"'{guess}' not found in ordering.")
   
    return ordering[guess]