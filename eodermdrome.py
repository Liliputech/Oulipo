#!/usr/bin/python
#
# Usage : eodermdrome.py [dictfile]
# - dictfile is a textfile (ascii encoding) containing one word per line.
# - a test "dictfile" is provided
#
# This work wouldn't have been possible without the help of my dear friends:
# Arthur Bourcigaux : Mathematician and brilliant algorithm designer
# Valentin Lageard : Philosopher and writer
#
# I'm the humble ghostwriter of the two great minds mentionned above.
# This link also inspired me alot for the dictionnary bruteforcing part:
# -http://wordaligned.org/articles/partitioning-with-python
#
# This work is also dedicated to my dear friend, mentor and colleage Densyo who "went away" the day before the release of this nifty piece of code.
# He was a genius and have been of great influence for me.
# 
# Arthur Suzuki

import sys
from collections import defaultdict
from itertools import product, combinations, chain
#from eodermdrome import is_eodermdrome

dict_file=sys.argv[1]
	
def is_eodermdrome(str=['']):
	#Main eodermdrome detection algorithm
	if(len(str)==11):
		test=1
		k=0
		co=0
		mem=[]
		while(k<10 and test==1):
			char1=str[k]
			char2=str[k+1]
			if(char1 not in mem):
				mem.append(char1)
				co=co+1
			if(char2 not in mem):
				mem.append(char2)
				co=co+1
			syl1=char1+char2
			syl2=char2+char1
			if(str.find(syl1,k+1)!=-1 or str.find(syl2,k+1)!=-1 or char1==char2 or co>5):
				test=0
			else:
				k=k+1
		#endwhile
	else:
		test=0
	return(test)

def find_eod_simple(file):
	#Finds single word eodermdrome and returns it
	words=defaultdict(list)
	for word in open(dict_file).read().split():
		words[len(word)].append(word)
	print(words)
	eods=list(filter(is_eodermdrome, words[11]))
	return(eods)

def find_eod_5_6(file):
	#Finds eodermdrome from combinations of words of length 5+6 and returns it
	seq=chain.from_iterable
	words=defaultdict(list)
	candidates=[]
	for word in open(dict_file).read().split():
		words[len(word)].append(word)
	for combi in product(words[5],words[6]):
		if(is_eodermdrome(combi[0]+combi[1])): candidates.append(combi[0]+combi[1])
	eods=candidates
	return(eods)

def sum_to_n(n):
	#This function is gonna be usefull for combination for word length between 1 and 11
	from operator import sub
	b, mid, e = [0], list(range(1,n)), [n]
	splits = (d for i in range(n) for d in combinations(mid, i))
	return(list(map(sub, chain(s,e),chain(b,s))) for s in splits)

def find_eod(file):
	seq=chain.from_iterable
	words=defaultdict(list)
	candidates=[]
	for word in open(dict_file).read().split():
                words[len(word)].append(word)
	for sum in sum_to_n(11):
		batch=seq(words[sum[i]] for i in range(len(sum)))
		for combi in combinations(batch,len(sum)):
			x=""
			for str in combi: x=x+str
			if(is_eodermdrome(x)): candidates.append(x)
	return(candidates)

#result = find_eod_simple(dict_file)
#result = find_eod_5_6(dict_file)
result = find_eod(dict_file)
for eod in result:
	print(eod)
