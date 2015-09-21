#!/usr/bin/python
import sys
str=sys.argv[1]
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
		syl1=char1+char2
		syl2=char2+char1
		if(str.find(syl1,k+1)!=-1 or str.find(syl2,k+1)!=-1 or char1==char2 or co>5):
			test=0
		else:
			k=k+1
	#endwhile
else:
	test=0
print(test)
