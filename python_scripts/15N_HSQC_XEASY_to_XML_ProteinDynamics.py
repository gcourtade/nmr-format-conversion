# This script reads a 15N-HSQC peaklist in XEASY format
# and converts it to an XML peaklist that can be read by
# the ProteinDynamics software
# 
# The input and output filenames have to be changed accordingly.
#  
# - Gaston Courtade, 19 January 2015
# 
#!/usr/bin/env python3

#Input file name
inputFile = "NOE_7102.peaks"



def readlinesFromFile(fileName):
    input = open(fileName, 'r')
    
    #The number 3 in the line under should be changed to reflect the number of lines in the XEASY file header before the peaks are defined.
    lines = input.readlines()[3:]
    return lines

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def parseLine(lines):
    HshiftList = []
    NshiftList =[]
    resList =[]
    j=0
    for j in range (0, len(lines)):
        line = lines[j]
        checkLine = isfloat(line.split()[1])
        if checkLine:
            Hshift=line.split()[1]
            Nshift=line.split()[2]
            aa = line.split()[0]
            HshiftList.append(Hshift)
            NshiftList.append(Nshift)
            resList.append(aa)
      
    return HshiftList, NshiftList, resList
    
def writeXML(HshiftList, NshiftList, resList):    
	#Output file name
    outputFile = "NOE_peaklist.xml"
    outputFile = open(outputFile, 'w')
    
    header='''<?xml version="1.0" encoding="UTF-8"?>
<PeakList>
<PeakList2D>
<PeakList2DHeader creator="User" date="2014-04-26T14:58:00" expNo="1" name="User" owner="User" procNo="1" source="Jamix">
<PeakPickDetails/>
</PeakList2DHeader>
'''

    footer = '''</PeakList2D>
</PeakList>'''
    
    outputFile.write(header)
    i=0
    for item in resList:
        newLine = ('<Peak2D F1="' + str(NshiftList[i]) + '" F2="' + str(HshiftList[i]) + '" annotation="' + str(resList[i]) + '" intensity="0" type="2"/>' + '\n')
        outputFile.write(newLine)
        i=i+1
    outputFile.write(footer)
    outputFile.close()
    
lines = readlinesFromFile(inputFile)
HshiftList, NshiftList, resList = parseLine(lines)
writeXML(HshiftList, NshiftList, resList)