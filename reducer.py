#!/usr/bin/env python

import sys

pos_count = 0.0
neg_count = 0.0
sentiment = 0.0

#handle input stream from mapper
for line in sys.stdin:

    if "pos" in line:
        pos_count+=1
    elif "neg" in line:
        neg_count+=1

sentiment = (pos_count - neg_count) / (pos_count + neg_count)
print "positive words:%s\tnegative words:%s" % (pos_count, neg_count)
print "sentiment score:%s" % (sentiment)
