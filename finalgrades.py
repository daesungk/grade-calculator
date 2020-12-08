# import pandas 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# read csv data
df_pl = pd.read_csv('gbook.csv')
df_wa_CF = pd.read_csv('wa_CF.csv')
df_wa_D = pd.read_csv('wa_D.csv')
df_C = pd.read_csv('moodle_C.csv')
df_D = pd.read_csv('moodle_D.csv')
df_F = pd.read_csv('moodle_F.csv')
df_m2 = pd.read_csv('Midterm2.csv')
df_q4 = pd.read_csv('quiz4.csv')

# Select relevant data
df = df_pl.loc[:, ['UID', 'Q1', 'Q2', 'Q3', 'E1', 'E4']]
df['E23'] = df_m2['Total']
df['Q4'] = df_q4['Q4']
df = df.fillna(0)

# Blank columns (temporary)
nofr = df.shape[0]
df['E5'] = [90] * nofr

# Quiz 
df_ql = ['Q1', 'Q2', 'Q3', 'Q4']
df["Q sum"] = df[df_ql].sum(axis=1)
df["Q lowest"] = df[df_ql].apply(lambda row: row.nsmallest(2).values[0], axis=1)
df["Q"] = (3*df["Q sum"] - 2*df["Q lowest"])/ 10

# HW
df_wa = pd.concat([df_wa_CF, df_wa_D])
df_wa = df_wa.loc[:, ['UID', 'Final']]
df_wa.columns = ['UID', 'HW']
df = pd.merge(df, df_wa, on ='UID', how ='left')

df = df.fillna(0)

# Weight
df["Total"] = df["Q"]*(1/10) + (df["E1"]+df["E23"]+df["E4"])*(15/100) + df["E5"]*(1/5) + df["HW"]*(1/4)

# Reordering
df = df[['UID', 'HW', 'Q1', 'Q2', 'Q3', 'Q4', 'Q lowest', 'Q sum', 'Q', 'E1', 'E23', 'E4', 'E5', 'Total']]

# Cut-off
AP = np.floor(df['Total'].quantile(0.95))
AO = np.floor(df['Total'].quantile(0.65))
AM = np.floor(df['Total'].quantile(0.6))
BP = np.floor(df['Total'].quantile(0.5))
BO = np.floor(df['Total'].quantile(0.35))
BM = np.floor(df['Total'].quantile(0.3))
CP = np.floor(df['Total'].quantile(0.2))
CO = np.floor(df['Total'].quantile(0.15))
CM = np.floor(df['Total'].quantile(0.1))
print(AP)
print(AO)
print(AM)
print(BP)
print(BO)
print(BM)
print(CP)
print(CO)
print(CM)

# Letter grades
def LetGrad(X):
    if X >= AP:
        return "A+"
    elif X >= AO:
        return "A"
    elif X >= AM:
        return "A-"
    elif X >= BP:
        return "B+"
    elif X >= BO:
        return "B"
    elif X >= BM:
        return "B-"
    elif X >= CP:
        return "C+"
    elif X >= CO:
        return "C"
    elif X >= CM:
        return "C-"
    else:
        return "D+"

df["Letter grade"] = df["Total"].apply(LetGrad)

# Export
df.to_csv('finalgrades.csv')

df_C_m = pd.merge(df_C, df, on ='UID', how ='left')
df_C_m.to_csv('finalgrades_C1.csv')

df_D_m = pd.merge(df_D, df, on ='UID', how ='left')
df_D_m.to_csv('finalgrades_D1.csv')

df_F_m = pd.merge(df_F, df, on ='UID', how ='left')
df_F_m.to_csv('finalgrades_F1.csv')
