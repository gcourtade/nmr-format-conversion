#!/usr/bin/env python3
import fileinput

#Input file name
inputFile = "filename.str"

wordCount=0

for line in fileinput.input(inputFile, inplace=1): 
	sentence = line.split()
	for word in sentence:
		if word == 'filename.str':
			wordCount = wordCount + 1
		if wordCount == 2 and len(sentence)>10:
			if (sentence[7] != 'C') and (sentence[7] != 'CA') and (sentence[7] != 'CB') and (sentence[7] != 'N') and (sentence[7] != 'H'):
				line=""
	print(line, end="")
			