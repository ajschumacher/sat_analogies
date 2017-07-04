import numpy as np


def read(filename):
    word_to_vec = {}
    with open(filename) as f:
        for line in f:
            first_space_index = line.index(' ')
            word = line[:first_space_index]
            values = line[first_space_index + 1:]
            vector = np.fromstring(values, sep=' ', dtype=np.float16)
            word_to_vec[word] = vector
    return word_to_vec
