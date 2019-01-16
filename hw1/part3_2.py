import sys
import nltk
from collections import Counter
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

from nltk.corpus import stopwords
stopword_set = set(stopwords.words('english'))
no_sw_toks = [t for t in tokens if t not in stopword_set ]

# WORD ASSOCIATION METRICS
def PMI(unigram_fd, bigram_cfd, threshold, file_name):
    pmi_dict = {}
    N = unigram_fd.N()
    for w1, fd in bigram_cfd.items():
        
        for w2, w1w2_count in fd.items():
            if (w1w2_count < threshold):
                continue
            # calculate pmi
            pmi = np.log(w1w2_count) - unigram_fd[(w1, )] - np.log(unigram_fd[(w2,)]) + np.log(N) 

            temp = w1 + ' ' + w2
            temp = '%30s %10d %10d %10d ' % (temp, unigram_fd[(w1, )], unigram_fd[(w2, )], w1w2_count)
            pmi_dict[temp] = pmi

    # output format: word1 word2 word1_freq word2_freq word1-2_freq word1-2_pmi
    pmi_dict = sorted(pmi_dict.items(), key=lambda x: x[1])
    outfile = open(file_name, 'w')
    for k, v in pmi_dict:
        outfile.write('%s %10f\n' %(k, v))
    outfile.close()



unigram_fd = nltk.FreqDist(nltk.ngrams(no_sw_toks, 1))
bigram_cfd = nltk.ConditionalFreqDist(nltk.ngrams(no_sw_toks, 2))
PMI(unigram_fd, bigram_cfd, 0, 'pmi1.txt')
PMI(unigram_fd, bigram_cfd, 100, 'pmi2.txt')
PMI(unigram_fd, bigram_cfd, 20, 'pmi3.txt')
PMI(unigram_fd, bigram_cfd, 50, 'pmi4.txt')
PMI(unigram_fd, bigram_cfd, 300, 'pmi5.txt')






