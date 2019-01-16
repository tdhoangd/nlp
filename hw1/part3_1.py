import sys
import nltk
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


if len(sys.argv) > 1:
    datafile = sys.argv[1]
else:
    datafile = 'tokens.txt'

f = open(datafile, 'r')
lines = f.read().splitlines()
f.close()

tokens = []
for line in lines:
    tokens += line.split()

# WORD COUNTING AND DISTRIBUTION
unigrams = list(nltk.ngrams(tokens, 1))
bigrams = list(nltk.ngrams(tokens, 2))

unigram_freqs = Counter(unigrams).most_common()
bigram_freqs = Counter(bigrams).most_common()

# 1
type_count = len(unigram_freqs)
print ('Number of unique types in this corpus: ', type_count)
# 2
token_count = len(unigrams)
print ('Number of unigram tokens: ', token_count)
# 3
y_unigram_freqs = [ k[1] for k in unigram_freqs]   # extract frequencu values only
y_unigram_freqs = np.log10(np.array(y_unigram_freqs))
y_bigram_freqs = [ k[1] for k in bigram_freqs]
y_bigram_freqs = np.log10(np.array(y_bigram_freqs))

x_unigram_ranks = np.log10(np.arange(1, len(unigram_freqs) + 1))
x_bigram_ranks = np.log10(np.arange(1, len(bigram_freqs) + 1))

plt.plot(x_unigram_ranks, y_unigram_freqs, label='unigrams')
plt.plot(x_bigram_ranks, y_bigram_freqs, label='bigrams')
plt.legend(loc='upper right')
plt.show()

del x_unigram_ranks, x_bigram_ranks, y_unigram_freqs, y_bigram_freqs

# 4
print ('Most 20 common words:\n')
common_words = [x[0][0] for x in unigram_freqs[:20] ]
print (common_words)

# 5
from nltk.corpus import stopwords
stopword_set = set(stopwords.words('english'))
no_sw_toks = [t for t in tokens if t not in stopword_set ]

no_sw_unigrams = list(nltk.ngrams(no_sw_toks, 1))
no_sw_unigram_freqs = Counter(no_sw_unigrams).most_common()

print ('Number of unique types in no stopwords corpus: ', len(no_sw_unigram_freqs))
print ('Number of tokens in no stopwords corpus: ', len(no_sw_unigrams))

# 6
print ('Most 20 common words after removing stopwords: \n')
common_words = [x[0][0] for x in no_sw_unigram_freqs[:20] ]
print (common_words)
