#!/usr/bin/env python3

#Input file name
inputFile = "filename.str"
name=inputFile.split('.')[0]


def readlinesFromFile(fileName):
	input = open(fileName, 'r')
	lines = input.readlines()
	return lines


def parseLine(lines):
	resCAList =[]
	resCBList = []
	resCList=[]
	caList = []
	cbList = []
	cList = []
	distList = []
	for line in lines:
		if len(line)>1:
			firstChar = line.split()[0]
			if firstChar.isdigit():
				atom = line.split()[3]
				if atom=='C':
					cList.append(line.split()[5])
					resCList.append(line.split()[1])
				if atom=='CA':
					caList.append(line.split()[5])
					resCAList.append(line.split()[1])
				if atom=='CB':
					cbList.append(line.split()[5])
					resCBList.append(line.split()[1])

	return resCAList, caList, resCBList, cbList, resCList, cList

def writeFile(resnr, atomShift, atomType):    #Output file name
	outputFile = name + '.' + atomType
	outputFile = open(outputFile, 'w')
	i=0
	for item in resnr:
		newLine = (resnr[i] + ' ' + atomShift[i] + '\n')
		outputFile.write(newLine)
		i=i+1
	outputFile.close()
	
lines = readlinesFromFile(inputFile)
resCAList, caList, resCBList, cbList, resCList, cList = parseLine(lines)
writeFile(resCAList, caList, 'ca')
writeFile(resCBList, cbList, 'cb')
writeFile(resCList, cList, 'c')