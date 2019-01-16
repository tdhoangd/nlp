import sys
import nltk
import string

punct_set = set(string.punctuation)

# PART 2.1
if len(sys.argv) > 1:
    datafile = sys.argv[1]
else:
    datafile = 'splited_sentences.txt'

f = open(datafile, 'r')
lines = f.readlines()
f.close()

for line in lines:
    line = line.lower()
    tokens = nltk.word_tokenize(line)
    no_punct_toks = [t for t in tokens if t not in punct_set]
    print (' '.join(no_punct_toks))
