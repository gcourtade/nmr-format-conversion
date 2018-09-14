
filename= 'restraints.tbl' #restraints in XPLOR/CNS format
seqfile = 'sequence.aa' #sequence in fasta format, no headers, no line-breaks
outfile = 'restraints.upl' #output file in CYANA format. NOTE: To use with CYANA remember to write 'translate xplor' and 'pseudo=3' before reading this upl file.
 

cyana_line_list = []

def readlinesFromFile(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    return lines
one_to_three = {'A':'ALA',
        'R':'ARG',
        'N':'ASN',
        'D':'ASP',
        'C':'CYSS', #Assuming all CYSS partake in disulfide bonds, change to CYS for reduced cysteines
        'Q':'GLN',
        'E':'GLU',
        'G':'GLY',
        'H':'HIS',
        'I':'ILE',
        'L':'LEU',
        'K':'LYS',
        'M':'MET',
        'F':'PHE',
        'P':'PRO',
        'S':'SER',
        'T':'THR',
        'W':'TRP',
        'Y':'TYR',
        'V':'VAL'
    }
seq = readlinesFromFile(seqfile)
seq = list(seq[0])

xplor_lines = readlinesFromFile(filename)

for line in xplor_lines:
    items = line.split()
    res1 = items[2]
    atom1 = items[5]
    res2 = items[8]
    atom2 = items[11]
    dist = items[13]

    aa_name1 = one_to_three[seq[int(res1)-1]]
    aa_name2 = one_to_three[seq[int(res2)-1]]

    cyana_line = res1 + ' ' + aa_name1 + ' ' + atom1 + ' ' + res2 + ' ' + aa_name2 + ' ' + atom2 + ' ' + dist + '\n'
    cyana_line_list.append(cyana_line)

with open(outfile, 'w') as f:
    for line in cyana_line_list:
        f.write(line)

