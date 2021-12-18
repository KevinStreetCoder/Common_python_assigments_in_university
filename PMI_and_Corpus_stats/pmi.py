#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
"""PMI calculator homework. PMI caluculator program"""
__author__="mariyam sheth"
import sys
import re
import math

total_s = "@total@ "
s2 = sys.argv[2]
s3 = sys.argv[3]
s4 = s2 + "_"+s3
app1=[]
app2=[]
app3 = []
total=[]
with open(sys.argv[1],'r') as f:
    for line in f:
        #print(type(line))
        line = line.rstrip('\n')
        res = line.partition(s2)[2]
        ret = line.partition(total_s)[2]
        rev = line.partition(s3)[2]
        rez = line.partition(s4)[2]
        app1.append(res)
        total.append(ret)
        app2.append(rev)
        app3.append(rez)
    while("" in app1) :
        app1.remove("")
    while("" in total) :
        total.remove("")  
    while("" in app3) :
        app3.remove("") 
    while("" in app2) :
        app2.remove("")   
count_1 = int(app1[0])
count_2 = int(app2[0])
count_3 = int(app3[0])
total_z =int( total[0])
#print(total_z)
#print(count_1)
#print(count_2)
#print(count_3)
pmi = math.log((count_3 * total_z)/(count_1 * count_2),2)
print("pmi")
print(pmi)
