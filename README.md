# Info and how to play:
- The game will generate a secret word for you to guess!

- To help you guess, you can guess other words and the game will tell you how far away (ie how different) they are from your guess!

- The list of words you've guessed previously will appear, in order of closeness to the hidden word, below your guess.

- Guessing might be a bit hard/time consuming (as it is for regular contexto), so there is also a reveal word button. Feel free to guess some words you think are similar to the revealed word to really test the vector similarity orderings! 

- After guessing the word, you'll get to know how long you took. You'll also get a play again button. Please wait for it to say "New game loaded!" before guessing. (This lets the cosine similarity be calculated)

**When starting the game, please wait for the "loading game! please wait" to turn to "Game loaded! Make your first guess!"**

# Demo screenshots:
<img width="1899" height="1041" alt="Screenshot 2025-07-22 134232" src="https://github.com/user-attachments/assets/0a2e4f64-5eff-493a-9982-71bfed134056" />
<img width="1567" height="909" alt="Screenshot 2025-07-22 134300" src="https://github.com/user-attachments/assets/0356277f-6bc2-4a3d-aaab-d625bb0f62b2" />

These screenshots are not all the features, just the most important ones.

# Notes:
- Words that are definitely english words might be "not found", as I don't have the vectors of those. This should only occur rarely. 

- The only words that can be chosen are a subset of ~300 common words that I hand filtered to ensure that they are guessable.

- When over 1000 words away from the target, the similarity scores are pretty meaningless. My recommended strategy is guess randomly until you find one fairly close. 

# Setup for running this yourself: 
1. Clone the repo
2. Run pip install -r requirements.txt
3. Run python app.py
4. visit http://localhost:8000/

# Credits:
This was a personal learning project inspired by [Contexto](https://contexto.me/en/). Word data was taken from sources like [GloVe embeddings](https://www.kaggle.com/datasets/anmolkumar/glove-embeddings), a list of the [top 10k words based on google](https://github.com/first20hours/google-10000-english), and a [list of stop words](https://www.kaggle.com/datasets/heeraldedhia/stop-words-in-28-languages?select=english.txt).

I do not claim ownership of the idea or word data I used- this project was created for educational purposes (teaching me flask and html) and not for commercial use (seriously. it's so bad people would probably have to charge *me* to play it).
