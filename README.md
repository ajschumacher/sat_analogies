# SAT Analogies by Word Vectors

To populate `data/`:

 * Acquire `data/SAT-package-V3.txt` ([a set of 374 SAT analogy questions](https://www.aclweb.org/aclwiki/index.php?title=SAT_Analogy_Questions_(State_of_the_art))) by emailing Peter Turney.
 * Download [GloVe vectors](https://nlp.stanford.edu/projects/glove/) and unzip, providing (for example) `data/glove.6B.50d.txt`.
 * Download [word2vec vectors](https://code.google.com/archive/p/word2vec/) and gunzip, providing `data/GoogleNews-vectors-negative300.bin`.

---

Task performance:

```bash
reading "data/glove.twitter.27B.25d.txt"
euclidean correct: 70 of 291 (0.240549828179)
cosine correct: 76 of 291 (0.26116838488)
agreement: 206 of 291 (0.707903780069)
euclidean correct: 92 of 374 (0.245989304813)
cosine correct: 96 of 374 (0.256684491979)
agreement: 262 of 374 (0.700534759358)

reading "data/glove.twitter.27B.50d.txt"
euclidean correct: 77 of 291 (0.264604810997)
cosine correct: 83 of 291 (0.285223367698)
agreement: 181 of 291 (0.621993127148)
euclidean correct: 97 of 374 (0.25935828877)
cosine correct: 106 of 374 (0.283422459893)
agreement: 227 of 374 (0.606951871658)

reading "data/glove.twitter.27B.100d.txt"
all words for 291 of 374 questions
euclidean correct: 82 of 291 (0.281786941581)
cosine correct: 95 of 291 (0.3264604811)
agreement: 177 of 291 (0.60824742268)
euclidean correct: 105 of 374 (0.280748663102)
cosine correct: 124 of 374 (0.331550802139)
agreement: 222 of 374 (0.593582887701)

reading "data/glove.twitter.27B.200d.txt"
all words for 291 of 374 questions
euclidean correct: 82 of 291 (0.281786941581)  # 81 when float32
cosine correct: 97 of 291 (0.333333333333)
agreement: 156 of 291 (0.536082474227)  # 155 when float32
euclidean correct: 111 of 374 (0.29679144385)  # 110 when float32
cosine correct: 130 of 374 (0.347593582888)
agreement: 194 of 374 (0.51871657754)  # 193 when float32

reading "data/glove.6B.50d.txt"
euclidean correct: 120 of 368 (0.326086956522)
cosine correct: 133 of 368 (0.361413043478)
agreement: 245 of 368 (0.665760869565)
euclidean correct: 121 of 374 (0.323529411765)
cosine correct: 135 of 374 (0.360962566845)
agreement: 249 of 374 (0.66577540107)

reading "data/glove.6B.100d.txt"
euclidean correct: 129 of 368 (0.350543478261)
cosine correct: 139 of 368 (0.377717391304)
agreement: 210 of 368 (0.570652173913)
euclidean correct: 130 of 374 (0.347593582888)
cosine correct: 141 of 374 (0.377005347594)
agreement: 212 of 374 (0.566844919786)

reading "data/glove.6B.200d.txt"
euclidean correct: 129 of 368 (0.350543478261)  # 128 when float32
cosine correct: 153 of 368 (0.415760869565)  # 152 when float32
agreement: 207 of 368 (0.5625)  # 206 when float32
euclidean correct: 131 of 374 (0.350267379679)  # 130 when float32
cosine correct: 155 of 374 (0.414438502674)  # 154 when float32
agreement: 209 of 374 (0.558823529412)  # 208 when float32

reading "data/glove.6B.300d.txt"
euclidean correct: 128 of 368 (0.347826086957)
cosine correct: 155 of 368 (0.421195652174)
agreement: 189 of 368 (0.513586956522)
euclidean correct: 129 of 374 (0.344919786096)
cosine correct: 157 of 374 (0.419786096257)
agreement: 192 of 374 (0.513368983957)

reading "data/glove.42B.300d.txt"
euclidean correct: 142 of 373 (0.380697050938)
cosine correct: 166 of 373 (0.445040214477)
agreement: 192 of 373 (0.514745308311)  # 193 when float32
euclidean correct: 142 of 374 (0.379679144385)
cosine correct: 166 of 374 (0.44385026738)
agreement: 193 of 374 (0.516042780749)  # 194 when float32

reading "data/glove.840B.300d.txt"
euclidean correct: 135 of 373 (0.361930294906)
cosine correct: 183 of 373 (0.490616621984)
agreement: 199 of 373 (0.533512064343)
euclidean correct: 135 of 374 (0.360962566845)
cosine correct: 183 of 374 (0.489304812834)
agreement: 200 of 374 (0.534759358289)

reading "data/GoogleNews-vectors-negative300.bin"
euclidean correct: 120 of 366 (0.327868852459)
cosine correct: 158 of 366 (0.431693989071)
agreement: 164 of 366 (0.448087431694)
euclidean correct: 123 of 374 (0.328877005348)
cosine correct: 161 of 374 (0.430481283422)
agreement: 166 of 374 (0.44385026738)
```

---

Missing words:

 * `glove.twitter.27B`
     * "2B tweets, 27B tokens, 1.2M vocab, uncased, 25d, 50d, 100d, & 200d vectors"
     * missing 105 words: ['abash', 'abstemious', 'acrid', 'aesthete', 'assiduous', 'avaricious', 'belligerents', 'bewilder', 'bibliographer', 'bungler', 'burnish', 'carouse', 'censorious', 'choleric', 'chronicler', 'cloudburst', 'cloying', 'combativeness', 'combustive', 'commodious', 'conflagration', 'congeal', 'corpulence', 'deaden', 'deferential', 'deleterious', 'desultory', 'disconcert', 'disinfection', 'dispassionate', 'disputant', 'dissembler', 'dissonant', 'drabness', 'effusive', 'embezzle', 'emend', 'emollient', 'entanglements', 'entreat', 'eulogize', 'exculpate', 'fecundity', 'flippancy', 'foolhardy', 'idolatrous', 'immunize', 'impious', 'indemnify', 'indigence', 'ingenuous', 'inoculation', 'inquisitorial', 'intransigent', 'irrigated', 'jocular', 'jollity', 'laconic', 'litigant', 'lummox', 'malinger', 'mendicant', 'merrymaking', 'misdeed', 'modulated', 'mollify', 'navigable', 'obdurate', 'ostracism', 'overexertion', 'parsimony', 'perfidious', 'perjure', 'persuasiveness', 'petrify', 'pinioned', 'potentate', 'prevarication', 'propagandize', 'proselytize', 'pugilist', 'purgation', 'putrefaction', 'querulous', 'refracted', 'reiteration', 'reveler', 'separable', 'sinuous', 'sluggishness', 'soporific', 'stevedores', 'surreptitious', 'testiness', 'toothsome', 'torpid', 'tremulous', 'truculent', 'unfeasible', 'unfetter', 'unfrock', 'ungainly', 'unnerve', 'wastefulness', 'wizened']
     * all words for 291 of 374 questions
 * `glove.6B`
     * "Wikipedia 2014 + Gigaword 5 (6B tokens, 400K vocab, uncased, 50d, 100d, 200d, & 300d vectors"
     * missing 6 words: ['abash', 'combustive', 'dissembler', 'emend', 'unfetter', 'unfrock']
     * all words for 368 of 374 questions
 * `glove.42B`
     * "Common Crawl (42B tokens, 1.9M vocab, uncased, 300d vectors"
     * missing 1 word: ['unfrock']
     * all words for 373 of 374 questions
 * `glove.840B`
     * Common Crawl (840B tokens, 2.2M vocab, cased, 300d vectors
     * missing 1 word: ['unfrock']
     * all words for 373 of 374 questions
 * `GoogleNews-vectors-negative300.bin`
     * missing 8 words: ['abash', 'aesthete', 'archaeology', 'catalogue', 'emend', 'self-righteous', 'tranquillity', 'unfrock']
     * all words for 366 of 374 questions
