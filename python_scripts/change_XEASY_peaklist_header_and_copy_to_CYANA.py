# This fixes the headers of peaklists files made in XEASY and copies them to the CYANA DIR. Without the right header format, CYANA will not run properly.

import fileinput
from shutil import copyfile

#filenames
files13C = '13c'
files15N = '15n'
fileTalos = 'talosn'
targetDir = 'CYANA DIR' 


#processing toggle switches
pro1 = False
pro2 = False
pro3 = False


#Read every line in file
for line in fileinput.input(files15N + '.peaks', inplace=1): 
	#If wrong header, correct it
	if line.startswith('#INAME 3 H'):
		line ='#INAME 3 HN\n'
		pro1 = True
	else:
		if pro1:
			print('#SPECTRUM N15NOESY H N HN')
			pro1 = False
	#The rest of the lines are untouched	
	print(line, end="")


#Do the same with the other file
for line in fileinput.input(files13C + '.peaks', inplace=1):
	if line.startswith('#INAME 1 13C'):
		line = '#INAME 1 C\n'
		pro3 = True
	if line.startswith('#INAME 3 1H'):
		line ='#INAME 3 HC\n'
		pro2 = True
	else:
		if pro2 and pro3:
			print('#SPECTRUM C13NOESY C H HC')
			pro2=False
			pro3=False
	print(line, end="")
 
#Copy the correct files to the cyana folder
copyfile(files15N + '.peaks', targetDir + files15N + '.peaks')
copyfile(files15N + '.prot', targetDir + files15N + '.prot')
copyfile(files13C + '.peaks', targetDir + files13C + '.peaks')
copyfile(files13C + '.prot', targetDir + files13C + '.prot')
#copyfile(fileTalos + '.aco', targetDir + fileTalos + '.aco')
