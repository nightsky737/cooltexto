def get_glove_vocab(glove_path):
    vocab = []
    with open(glove_path, 'r', encoding='utf8') as f:
        for line in f:
            word = line.split(' ', 1)[0]
            vocab.append(word)
    return vocab

glove_vocab = get_glove_vocab('word_data/glove.6B.300d.txt')

query = "twilight"
print(f"{query} is in GloVe: {query in glove_vocab}")