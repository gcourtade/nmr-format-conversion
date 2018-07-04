#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
#Input file name
manual = "file_manual.str"
automatic = "file_auto.str"



def readlinesFromFile(fileName):
	input = open(fileName, 'r')
	lines = input.readlines()
	return lines


def parseLine(lines):
        H = {}
        N = {}
        CA = {}
        for line in lines:
                resnum = line.split()[1]
                atom = line.split()[3]
                if atom == 'H':
                        shift = line.split()[5]
                        H[resnum] = shift
                elif atom == 'N':
                        shift = line.split()[5]
                        N[resnum] = shift
                elif atom == 'CA':
                        shift = line.split()[5]
                        CA[resnum] = shift                        
        return H, N, CA

##def writeFile(resnr, atomShift, atomType):    #Output file name
##	outputFile = name + '.' + atomType
##	outputFile = open(outputFile, 'w')
##	i=0
##	for item in resnr:
##		newLine = (resnr[i] + ' ' + atomShift[i] + '\n')
##		outputFile.write(newLine)
##		i=i+1
##	outputFile.close()
	
def indeces(list_name):
        return range(0,len(list_name))

manualH,manualN, manualCA = parseLine(readlinesFromFile(manual))
autoH,autoN, autoCA = parseLine(readlinesFromFile(automatic))
res = []
auto_shiftsN = []
auto_shiftsH = []
manual_shiftsN= []
manual_shiftsH= []
res_CA = []
manual_shiftsCA= []
auto_shiftsCA= []
auto_unique = list(set(list(manualH.keys()))-set(list(autoH.keys())))
print('in manual, not in auto:', auto_unique)
print(len(autoH.keys()))
print(len(manualH.keys()))
for i in range(1,150):
        if str(i) in (manualH.keys() and autoH.keys()):
               res.append(int(i))
               auto_shiftsN.append(float(autoN[str(i)]))
               auto_shiftsH.append(float(autoH[str(i)]))               
               manual_shiftsN.append(float(manualN[str(i)]))
               manual_shiftsH.append(float(manualH[str(i)]))
        if str(i) in (manualCA.keys() and autoCA.keys()):
                res_CA.append(int(i))
                manual_shiftsCA.append(float(manualCA[str(i)]))
                auto_shiftsCA.append(float(autoCA[str(i)]))               
##plt.scatter(res, manual_shifts, c='k')
##plt.scatter(res, auto_shifts, c='r')
##plt.show()
auto_shiftsH  = np.asarray(auto_shiftsH)
auto_shiftsN  = np.asarray(auto_shiftsN)
manual_shiftsH  = np.asarray(manual_shiftsH)
manual_shiftsH  = np.asarray(manual_shiftsH)
manual_shiftsCA = np.asarray(manual_shiftsCA)
auto_shiftsCA = np.asarray(auto_shiftsCA)
res_CA = np.asarray(res_CA)
res = np.asarray(res)
distance = (auto_shiftsH - manual_shiftsH)**2 + (auto_shiftsN - manual_shiftsN)**2
distance = distance/np.max(distance)


wrong = []
for d in indeces(distance):
        if distance[d]>0.1:
                wrong.append(res[d])
print('wrongly assigned:', wrong)
print('percent error:', (len(wrong)/len(autoH.keys())))
                
fig, ax = plt.subplots()
ax.scatter(manual_shiftsH, manual_shiftsN, color='b')
ax.scatter(auto_shiftsH, auto_shiftsN, color='r')

for i, txt in enumerate(res):
    ax.annotate(txt, (manual_shiftsH[i],manual_shiftsN[i]), (manual_shiftsH[i]*1.002,manual_shiftsN[i]*1.002), color='k')
    ax.annotate(txt, (auto_shiftsH[i],auto_shiftsN[i]), (auto_shiftsH[i]*0.99,auto_shiftsN[i]*0.99), color='r')
plt.show()

plt.bar(res, distance)
plt.show()

auto_shiftsCA = auto_shiftsCA + 3.22

diff_CA =  abs(auto_shiftsCA-manual_shiftsCA)

        
for i in indeces(diff_CA):
        if diff_CA[i] < 0.5:
                print(0, res_CA[i], manual_shiftsCA[i], auto_shiftsCA[i])
        else:
                print(1, res_CA[i], manual_shiftsCA[i], auto_shiftsCA[i])

        
fig, ax = plt.subplots()
ax.scatter(manual_shiftsCA, auto_shiftsCA)


for i, txt in enumerate(res_CA):
    ax.annotate(txt, (manual_shiftsCA[i],auto_shiftsCA[i]))
plt.show()


##writeFile(resCAList, caList, 'ca')
##writeFile(resCBList, cbList, 'cb')
##writeFile(resCList, cList, 'c')
