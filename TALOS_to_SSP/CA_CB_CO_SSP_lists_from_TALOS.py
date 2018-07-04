#!/usr/bin/env python3
import fileinput

#Input file name
inputFile = 'file_talos.tab'
outputFile_CA = 'file.ca'
outputFile_CB = 'file.cb'
outputFile_C = 'file.co'
outputFile_seq = 'file.seq'


res_CA = []
shift_CA = []
res_CB = []
shift_CB = []
res_C = []
shift_C = []
seq = []

switch = False

def printFiles(outputFile, res_list, shift_list, seq=0):
        with open (outputFile, 'w') as o:
                if seq==1:
                        strseq=''
                        for subseq in res_list:
                                strseq = strseq + ''.join(subseq)
                        newLine = strseq
                        o.write(newLine)
                else:
                        for i in range(len(res_list)):
                                newLine = res_list[i] + ' ' + shift_list[i] + '\n'
                                o.write(newLine)
                                
for line in fileinput.input(inputFile, inplace=0):
        sentence = line.split()
        for word in sentence:
                if word == 'SEQUENCE':
                        seq.append(sentence[2:])
                if word == 'FORMAT':
                        switch = True
                if switch:                   
                        res = sentence[0]
                        atom = sentence[2]
                        shift = sentence[3]
                        if atom == 'CA':
                                res_CA.append(res)
                                shift_CA.append(shift)
                                break
                        if atom == 'CB':
                                res_CB.append(res)
                                shift_CB.append(shift)
                                break
                        if atom == 'C':
                                res_C.append(res)
                                shift_C.append(shift)
                                break


printFiles(outputFile_CA,res_CA,shift_CA)
printFiles(outputFile_CB,res_CB,shift_CB)
printFiles(outputFile_C,res_C,shift_C)
printFiles(outputFile_seq,seq,shift_CA,1)  