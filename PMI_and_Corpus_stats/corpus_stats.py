#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
"""PMI calculator homework.word frequency count program and bigram"""
__author__="mariyam sheth"
import sys
import re

frequency = {}
bigram_freq = {}
with open(sys.argv[1],'r') as f:
    strings = f.read().lower()
    match_text = re.findall(r'\w+',strings)
    for word in match_text:
        count= frequency.get(word,0)
        frequency[word] = count + 1
    frequency_list  = frequency.keys()

    for words in frequency_list:
        print (words, frequency[words],file=open(sys.argv[2], 'a'))
    
    for i in range(len(match_text)-1):
        bigram = match_text[i]+"_"+match_text[i+1]
        if bigram not in bigram_freq:
            bigram_freq[bigram] = 0
        bigram_freq[bigram] += 1
    
    for key, value in bigram_freq.items():
        print (key, value,file=open(sys.argv[2], 'a'))
        
    totals = len(strings.split())
    print("@total@  " + str(totals),file=open(sys.argv[2], 'a'))
