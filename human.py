import random

import sat


random.shuffle(sat.items)
attempted, correct = 0, 0
for item in sat.items:
    print
    print item['question']
    print
    for i, answer in enumerate(item['answers']):
        print i, answer
    print
    answer = raw_input('> ')
    try:
        answer = int(answer)
    except:
        continue
    if answer == item['correct']:
        correct += 1
    attempted += 1
    print
    print 'correct was {}'.format(item['correct'])
    print '{} of {}; {}'.format(correct, attempted, float(correct) / attempted)
