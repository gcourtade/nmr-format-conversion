#fits T2 and displays T2 as a function of amino aciddata in the following format.
#T: time in s from vdlist.
#2, 3, 4, ...: are the amino acid numbers with their respective intensities at each time T.
#T	0.01696	0.03392	0.06784	0.10176	0.1696	0.20352
#2	15010	7771	6538	5252	3766	2053
#3	12642	8431	5156	3075	1908	778
#4	25126	13742	12316	6120	8016	3576

import matplotlib.pyplot as plt
from matplotlib import style
style.use('seaborn-white')
import numpy as np
from scipy.optimize import curve_fit

def fitT2(T, I0, T2):
    return I0*np.exp(-T/T2)

def calcT2(T, data):
    T = np.asarray(T, dtype=np.float64)
    data = np.asarray(data, dtype=np.float64)
    p0 = [1500, 0.1]
    popt, pcov = curve_fit(fitT2, T, data, p0)
    return popt[1]

with open('T2_data.txt', 'r') as workfile:
    lines = workfile.readlines()
    
res_list =[]
T2_list =[]

switch = False    
for line in lines:
    if switch:
        try:
            data = line.split()[1:]
            this_T2 = calcT2(T, data)
            T2_list.append(this_T2)
            res = line.split()[0]
            res_list.append(res)
        except:
            pass
    else:
        T = line.split()[1:]
        switch = True
        
res_list = np.asarray(res_list, dtype=np.float64)
np.sort(res_list)
print(res_list)



plt.bar(res_list, T2_list)
plt.show()

