# Info and how to play:
Cooltexto: 
- The game will generate a secret word for you to guess!
- To help you guess, you can guess other words and the game will tell you how far away (ie how different) they are from your guess!
- Timer (Javascript)
- pvp usernames (javascript)

# Notes:
Words that are definitely english words might be "not found", as I don't have the vectors of those.

Structure:
Get: Generate the word list?
Get: Get the results of a guess. I "guess" that's it.

Post and put: Leaderboard functionality prolly Ill deal with that later 

# Setup: 
After cloning the repo, create a folder called word_data. In it, add these three files:
(the final word data stuff I choose to use) 

I would include these in the github if I could, but these are too big for me to upload to github.

Additionally, there might be requirements that I should add a requirements file to

# Credits:
This was a personal learning project inspired by [Contexto](https://contexto.me/en/). Word data was taken from sources like [GloVe embeddings](https://www.kaggle.com/datasets/anmolkumar/glove-embeddings), a list of the top 10k words based on google[link](https://github.com/first20hours/google-10000-english), and a [list of stop words](https://www.kaggle.com/datasets/heeraldedhia/stop-words-in-28-languages?select=english.txt).

I do not claim ownership of the idea or word data I used- this project was created for educational purposes (teaching me flask and html) and not for commercial use (seriously. it's so buggy I think people would have to charge *me* to play it).