import numpy as np
import scipy.linalg
import scipy.spatial


def safe(items, word_to_vec):
    safe_items = []
    missed_words = set()
    for item in items:
        all_included = True
        words = item['answers'][:]
        words.extend([item['question']])
        words = sum(words, [])
        for word in words:
            if word not in word_to_vec:
                all_included = False
                missed_words.add(word)
        if all_included:
            safe_items.append(item)
    print 'missing {} words: {}'.format(len(missed_words),
                                        sorted(list(missed_words)))
    print 'all words for {} of {} questions'.format(len(safe_items),
                                                    len(items))
    return safe_items


def vec_for(word, word_to_vec):
    # default to vector of zeros
    if word in word_to_vec:
        return word_to_vec[word]
    else:
        try:  # works for vanilla dicts
            for key, value in word_to_vec.iteritems():
                return np.zeros(value.shape, value.dtype)
        except:  # handle one case of trained word2vec
            return np.zeros(300)


def norm(vector):
    l2_norm = scipy.linalg.norm(vector)
    if l2_norm == 0:
        return vector
    else:
        return vector / l2_norm


def norm_euc(first, second):
    return scipy.spatial.distance.euclidean(norm(first), norm(second))


def dot_prod(first, second):
    return 0 - np.dot(first, second)

def answer(item, word_to_vec, distance):
    question = (vec_for(item['question'][0], word_to_vec) -
                vec_for(item['question'][1], word_to_vec))
    answers = [vec_for(first, word_to_vec) - vec_for(second, word_to_vec)
               for first, second in item['answers']]
    distances = [distance(question, answer) for answer in answers]
    return np.argmin(distances)


def score(items, word_to_vec):
    for item in items:
        item['euclidean'] = answer(item, word_to_vec,
                                   scipy.spatial.distance.euclidean)
        item['norm_euc'] = answer(item, word_to_vec,
                                  norm_euc)
        item['dot_prod'] = answer(item, word_to_vec,
                                  dot_prod)
        item['cosine'] = answer(item, word_to_vec,
                                scipy.spatial.distance.cosine)
    euc_correct = sum(item['correct'] == item['euclidean'] for item in items)
    print 'euclidean correct: {} of {} ({})'.format(
        euc_correct, len(items), float(euc_correct) / len(items))
    norm_euc_correct = sum(item['correct'] == item['norm_euc']
                           for item in items)
    print 'norm_euc correct: {} of {} ({})'.format(
        norm_euc_correct, len(items), float(norm_euc_correct) / len(items))
    dot_prod_correct = sum(item['correct'] == item['dot_prod']
                           for item in items)
    print 'dot_prod correct: {} of {} ({})'.format(
        dot_prod_correct, len(items), float(dot_prod_correct) / len(items))
    cos_correct = sum(item['correct'] == item['cosine'] for item in items)
    print 'cosine correct: {} of {} ({})'.format(
        cos_correct, len(items), float(cos_correct) / len(items))
    agreement = sum(item['euclidean'] == item['cosine'] for item in items)
    print 'euc/cos agreement: {} of {} ({})'.format(
        agreement, len(items), float(agreement) / len(items))
