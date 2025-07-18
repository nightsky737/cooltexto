fix the yaml
Swap to using nltk's list of english stopwords
ranks.nl also has a good stopword list

google has some very common words, and so does kaggle.
- Convert to set for fast lookup in those words? Eh nah. this only runs once or twice when generating orderings

kaggle's stop words in 28 languages is looking p juicy

Additionally, there might be requirements that I should add a requirements file to
