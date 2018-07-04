import numpy as np
import pandas as pd
import xlrd



outfile = 'for_rotdif.txt'

df = pd.read_csv('dynamics.csv')

res_800 = df['res'].values.tolist()
wH_800  = df['wH'].values.tolist()
wN_800  = df['wN'].values.tolist()
NOE_800  = df['NOE'].values.tolist()
R1_800  = df['R1'].values.tolist()
R2_800  = df['R2'].values.tolist()

df = pd.read_excel('dynamics_600.xlsx')
res_600 = df['res'].values.tolist()
NOE_600  = df['NOE'].values.tolist()
T1_600  = df['T1'].values.tolist()
T2_600  = df['T2'].values.tolist()



for res in res_600[:]:
    idx = res_600.index(res)
    if 200<res<230 and  T1_600[idx]!=0 and T2_600[idx]!=0:
        pass
    elif (res not in res_800) or (not 0.5<T1_600[idx]<1.5) or (not 0.005<T2_600[idx]<0.5) or not (-3<NOE_600[idx]<0.9) or T1_600[idx]==0 or T2_600[idx]==0:
        NOE_600.remove(NOE_600[idx])
        T1_600.remove(T1_600[idx])
        T2_600.remove(T2_600[idx])
        res_600.remove(res)


for res in res_800[:]:
    idx = res_800.index(res)
    if 200<res<230 and  (1/R1_800[idx])!=0 and (1/R2_800[idx])!=0:
        pass
    elif (res not in res_600) or not (-3.2<NOE_800[idx]<0.95) or R1_800[idx]==0 or R2_800[idx]==0:
        NOE_800.remove(NOE_800[idx])
        R1_800.remove(R1_800[idx])
        R2_800.remove(R2_800[idx])
        res_800.remove(res)


NOE_800 = np.asarray(NOE_800, dtype=np.float64)
NOE_600 = np.asarray(NOE_600, dtype=np.float64)
R1_800 = np.asarray(R1_800, dtype=np.float64)
R2_800 = np.asarray(R2_800, dtype=np.float64)
R1_600 = np.power(np.asarray(T1_600, dtype=np.float64),-1)
R2_600 = np.power(np.asarray(T2_600, dtype=np.float64),-1)


def makeFiles(outfile, res_list, field, R1_list, R2_list, NOE_list, error):
    header = '%<residue><chain><atom 1><atom 2><magnet><R1><R1 error><R2><R2 error><NOE><NOE error>\n'
    with open(outfile, 'a') as workfile:
        workfile.write(header)    
    for res in res_list[:]:
        idx = res_list.index(res)
        line = str(res_list[idx]) + '\t' + 'A\tN\tH\t' + str(field) + '\t'+ str(R1_list[idx]) + '\t'+ str(error*R1_list[idx])+ '\t'+ str(R2_list[idx]) + '\t'+ str(error*R2_list[idx])+ '\t'+ str(NOE_list[idx]) + '\t'+ str(abs(error*NOE_list[idx])) +'\n'
        with open(outfile, 'a') as workfile:
            workfile.write(line)
    return 1
            
finished_1 = makeFiles(outfile,res_800, 800.13, R1_800, R2_800, NOE_800, 0.05)
finished_2 = makeFiles(outfile,res_600, 600.13, R1_600, R2_600, NOE_600, 0.05)


if finished_1 == 1 and finished_2==1:
    print('finished')
else:
    print('didnt work')

