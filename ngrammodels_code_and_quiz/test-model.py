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
uni_bol = False
uni_bol_2 = False
bi_bol= False
for j in range(len(temp_string)-1):
    s1 = temp_string[j].lower()
    s2 = temp_string[j+1].lower()
    s4 = s2 + s1
    s5 = "count"+"words"
    for key, value in unigram.items():
        if(''.join(key) == s1):
            uni_bol = True
            count_s1=[str(value)]
            count_s1_final=count_s1[0]
        if(''.join(key) == s2):
            uni_bol_2 = True
            count_s2=[str(value)]
            count_s2_final=count_s2[0]
    for key, value in bigram.items():
        #print(''.join(key))
        if(''.join(key) == s4):
            bi_bol = True
            count_s4=[str(value)]
            count_s4_final=count_s4[0]
        if(''.join(key) == s5):
            count_s5=[str(value)]
            count_s5_final=count_s5[0]
    if(uni_bol_2 and uni_bol and bi_bol):
        uni_prob = int(count_s1_final)/int(count_s5_final)
        bi_prob = int(count_s4_final)/int(count_s1_final)
        print(bi_prob)

            