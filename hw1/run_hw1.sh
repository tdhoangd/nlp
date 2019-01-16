#!/bin/bash

python3 deserialization_script.py cna_eng/*.xml.gz > deserialized.txt

python3 part2_splitsentences.py deserialized.txt > splited_sentences.txt
python3 part2_wordtokenize.py splited_sentences.txt > tokens.txt

python3 part3_1.py tokens.txt
python3 part3_2.py tokens.txt


