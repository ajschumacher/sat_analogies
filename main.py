import gensim

import sat
import glove
import computer


glove_files = ['data/glove.twitter.27B.25d.txt',
               'data/glove.twitter.27B.50d.txt',
               'data/glove.twitter.27B.100d.txt',
               'data/glove.twitter.27B.200d.txt',
               'data/glove.6B.50d.txt',
               'data/glove.6B.100d.txt',
               'data/glove.6B.200d.txt',
               'data/glove.6B.300d.txt',
               'data/glove.42B.300d.txt',
               'data/glove.840B.300d.txt']
for glove_file in glove_files:
    print 'reading "{}"'.format(glove_file)
    word_to_vec = glove.read(glove_file)
    safe_items = computer.safe(sat.items, word_to_vec)
    computer.score(safe_items, word_to_vec)
    computer.score(sat.items, word_to_vec)

word2vec_file = 'data/GoogleNews-vectors-negative300.bin'
print 'reading "{}"'.format(word2vec_file)
word_to_vec = gensim.models.KeyedVectors.load_word2vec_format(
    word2vec_file, binary=True)
safe_items = computer.safe(sat.items, word_to_vec)
computer.score(safe_items, word_to_vec)
computer.score(sat.items, word_to_vec)
