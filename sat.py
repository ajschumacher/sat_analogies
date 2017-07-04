filename = 'data/SAT-package-V3.txt'

with open(filename) as f:
    contents = f.read()

chunks = contents.split('\r\n\r\n')  # Split on blank lines.
chunks = [[line for line in chunk.split('\r\n') if line]
          for chunk in chunks]
chunks = [chunk for chunk in chunks if len(chunk) == 8]
assert len(chunks) == 374

# format now is:
# one line describes the source of the question
# then there's the problem and five options, each like:
# word1 word1 n:n
# and a line with a letter a-e for which option is correct

items = []
for chunk in chunks:
    chunk.pop(0)  # lose the description of the question's source
    correct_letter = chunk.pop()  # which of the options
    correct_index = 'abcde'.index(correct_letter)
    chunk = [line.split()[:-1] for line in chunk]
    question = chunk.pop(0)
    item = {'question': question,
            'answers': chunk,
            'correct': correct_index}
    items.append(item)

# items = [item for item in items if ['no', 'choice'] not in item['answers']]
# assert len(items) == 354
