import sys
import nltk


# PART 2.1
if len(sys.argv) > 1:
    datafile = sys.argv[1]
else:
    datafile = 'deserialized.txt'

f = open(datafile, 'r')
lines = f.readlines()
f.close()

# fix a sentence that spans in multiple lines
data = ""
for line in lines:
    line = line.rstrip()
    if len(line) > 0:
        if line[-1] == '.':
            line += '\n'
        else:
            line += ' '
        data += line


# split sentences
sentences = nltk.sent_tokenize(data)
for sentence in sentences:
    print (sentence)