import sys
from collections import defaultdict
import math
import random
import os
import os.path 
import glob

punctuations = '''!()-[]{};:'."\,<>/?@#$%^&*_~'''

def corpus_reader(): 
    with open(sys.argv[1],'r') as corpus: 
        for line in corpus: 
            if line.strip():
                sequence = line.lower().strip().split()
                for i in range(len(sequence)):
                    if sequence[i] in punctuations:
                        sequence[i]=""
        yield sequence

def get_count(corpus):
    word_counts = defaultdict(int)
    for sentence in corpus:
        for word in sentence: 
            word_counts[word] += 1
    return set(word for word in word_counts if word_counts[word] > 1) 

def get_ngrams(sequence, n):
    results = [] 

    count_start = 1 
    if not n > 0: 
        return results 
    elif n > 1: 
        count_start = n - 1 

    ext_sequence = [] 

    ext_sequence += sequence + ["STOP"] 

    for i in range(len(ext_sequence) - n + 1): 
        result = [] 
        # print(i) 
        for j in range(i, i + n): 
            # print(j - i) 
            result.append(ext_sequence[j]) 
        results.append(tuple(result))

    return results 
class TrigramModel(object):
    
    def __init__(self):
    
        generator = corpus_reader()
        self.lexicon = get_count(generator)
        self.lexicon.add("STOP")
    
        # Now iterate through the corpus again and count ngrams
        generator = corpus_reader()
        self.count_ngrams(generator) 

    def count_ngrams(self, corpus):
   
        self.unigramcounts = {} # might want to use defaultdict or Counter instead
        self.bigramcounts = {} 
        self.trigramcounts = {} 
        self.totalwordcounts = 0  

        for sequence in corpus: 
            for token in get_ngrams(sequence, 1): 
                if not token in self.unigramcounts: 
                    self.unigramcounts[token] = 0 
                self.unigramcounts[token] += 1 

            for token in get_ngrams(sequence, 2): 
                if not token in self.bigramcounts: 
                    self.bigramcounts[token] = 0 
                self.bigramcounts[token] += 1 

            for token in get_ngrams(sequence, 3): 
                if not token in self.trigramcounts: 
                    self.trigramcounts[token] = 0 
                self.trigramcounts[token] += 1 

            # Calculate total number of words 
            self.totalwordcounts += len(sequence) 
        for key, value in self.unigramcounts.items():
            print (" ".join(map(str,key))," ",value,file=open(sys.argv[2], 'a'))
        for key, value in self.bigramcounts.items():
            print (" ".join(map(str,key)), " ",value,file=open(sys.argv[2], 'a'))
        for key, value in self.trigramcounts.items():
            print (" ".join(map(str,key)), " ",value,file=open(sys.argv[2], 'a'))
        print("count words"," ",self.totalwordcounts,file=open(sys.argv[2],'a'))


        return
model = TrigramModel()

