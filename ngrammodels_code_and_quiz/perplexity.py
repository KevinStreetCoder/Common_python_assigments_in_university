import sys
from collections import defaultdict
import math
import random
import os
import os.path 
import glob
import re
from typing import final

unigram={}
bigram={}
trigram={}
string_list=[]

lambda1 = 1/3.0
lambda2 = 1/3.0
lambda3 = 1/3.0 
with open(sys.argv[1],'r') as f:
    for line in f:
        line = line.rstrip('\n')
        dict1 = dict((tuple(a.split(' ')), int(b.strip()))  
                     for a, b in (element.split("   ")  
                                  for element in line.split(', '))) 
        for key, value in dict1.items():
            if len(key)==2:
                bigram[key]=value
            elif len(key)==1:
                unigram[key]= value
            elif len(key)==3:
                trigram[key]= value
            else:
                break
with open(sys.argv[2],'r') as file:
    strings = file.read()
    pat = ('\. +(?=[A-Z])')
    match_text = re.sub(pat,'.\n',strings)
    pat2=('\.')
    final_text = [re.sub(pat2,' STOP',match_text)]
for word in final_text:
       lst=word.split("\n")
new_list = []

# Creating list of list format
for elem in lst:
   temp = elem.split(', ')
   new_list.append((temp))

# Final list
res = []

for elem in new_list:
   temp = []
   for e in elem:
      temp.append(e)
   res.append(temp)
for i in range(len(res)):
    temps=''.join(res[i])
temp_string = temps.split()
for j in range(len(temp_string)-2):
    s1 = temp_string[j].lower()
    s2 = temp_string[j+1].lower()
    s3 = temp_string[j+2].lower()
    s4 = s1 + s2
    s5 = "count"+"words"
    s6 = s1 + s2 + s3
    for key, value in unigram.items():
        if(''.join(key) == s1):
            count_s1=[str(value)]
            count_s1_final=count_s1[0]
        else:
            count_s1_final = 0.1
        if(''.join(key) == s2):
            count_s2=[str(value)]
            count_s2_final=count_s2[0]
        else:
            count_s2_final = 0.1
    for key, value in bigram.items():
        #print(''.join(key))
        if(''.join(key) == s4):
            count_s4=[str(value)]
            count_s4_final=count_s4[0]
        else:
            count_s4_final = 0.1
        if(''.join(key) == s5):
            count_s5=[str(value)]
            count_s5_final=count_s5[0]
    for key, value in trigram.items():
        if(''.join(key) == s6):
            count_s6=[str(value)]
            count_s6_final=count_s6[0]
        else:
            count_s6_final = 0.1
    uni_prob = float(count_s1_final)/float(count_s5_final)
    bi_prob = float(count_s4_final)/float(count_s1_final)
    tri_prob = float(count_s6_final)/float(count_s4_final)
    prexity= lambda1 * tri_prob + lambda2 * bi_prob + lambda3 * uni_prob
    print(prexity)

            
    