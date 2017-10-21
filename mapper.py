#!/usr/bin/env python

import sys

#function for checking if a word matches a sentiment word
def sentiment_check(word):
    if word in pos_words:
        return "pos"
    elif word in neg_words:
        return "neg"
    else:
        return "neu"


#read sentiment files and parse them into lists
neg_file = open("neg-words.txt", "r")
neg_words = [x.strip() for x in neg_file.readlines()]
pos_file = open("pos-words.txt", "r")
pos_words = [x.strip() for x in pos_file.readlines()]

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # replace commas
    line = line.replace(","," ")
    # split the line into words
    words = line.split()

    # check if word matches sentiment-files
    for word in words:
        final = sentiment_check(word)
        print(word, final)
