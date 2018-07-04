#!/usr/bin/env python3
import fileinput

#Input file name
inputFile = "predSS.tab"

wordCount=0

for line in fileinput.input(inputFile, inplace=1): 
	sentence = line.split()
	for word in sentence:
		if word == 'FORMAT':
			wordCount = wordCount + 1
		if wordCount == 1 and len(sentence)==9:
			ss = sentence[8]
			res = sentence[0]
			conf = float(sentence[7])
			dict = {'L':0, 'H':1, 'E':-1}
			if ss in dict:
				ssp = conf*dict[ss]
				line = res + '\t' + '%4.2f' % (ssp) + '\n'
			else:
				line=""
		
	print(line, end="")
	
		