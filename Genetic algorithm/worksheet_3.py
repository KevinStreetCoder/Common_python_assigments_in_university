# -*- coding: utf-8 -*-

import random
import copy
MUTRATE = 0.01
MUTSTEP = 100
N=10
P= 50
population = []
class individual:
  def __init__(self):
    self.gene = [0]*N
    self.fitness = 0
for x in range (0, P):
  tempgene=[]
  for x in range (0, N):
    tempgene.append( random.randint(0,1))
  newind = individual()
  newind.gene = tempgene.copy()
  population.append(newind)
def test_function( ind ):
  utility=0
  for i in range(N):
    utility = utility + ind.gene[i]
  return utility
offspring=[]
for i in range (0,N):
  random.seed(1)
  parent1 = random.randint( 0, N-1)
  off1 = population.pop(parent1)
  parent2 = random.randint( 0, N-1)
  off2 = population.pop(parent2)
  if off1.fitness > off2.fitness:
    offspring.append( off1 )
  else:
    offspring.append( off2 )

toff1 = individual()
toff2 = individual()
temp = individual()
for i in range( 0, N, 2 ):
  toff1 = copy.deepcopy(offspring[i])
  toff2 = copy.deepcopy(offspring[i+1])
  temp = copy.deepcopy(offspring[i])
  crosspoint = random.randint(1,N)
  for j in range (crosspoint, N):
    toff1.gene[j] = toff2.gene[j]
    toff2.gene[j] = temp.gene[j]
  offspring[i] = copy.deepcopy(toff1)
  offspring[i+1] = copy.deepcopy(toff2)
for i in range( 0, N ):
  newind = individual();
  newind.gene = []
  for j in range( 0, N ):
    gene = offspring[i].gene[j]
    mutprob = random.random()
    if mutprob < MUTRATE:
      alter = random.randrange(0,MUTSTEP)
      if(mutprob%2):
        offspring[i].gene[j] = offspring[i].gene[j]+alter;
        if( offspring[i].gene[j] > 1.0 ): offspring[i].gene[j] = 1.0
      else:
        offspring[i].gene[j] = offspring[i].gene[j]-alter
        if( offspring[i].gene[j] < 0.0 ):offspring[i].gene[j] = 0.0
    newind.gene.append(gene)
print(test_function(newind))
