import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# read csv data
df = pd.read_csv('../gradebook-processor/gradebook-proc-sel.csv')
df_A = pd.read_csv('../data/Section_A.csv')
df_B = pd.read_csv('../data/Section_B.csv')
df_C = pd.read_csv('../data/Section_C.csv')

# Weight
Weight_H = 25
Weight_Q = 10
Weight_M = 15
Weight_F = 20

# Total
df["Total"] = (Weight_H*df["HW"] +Weight_Q*df["Quiz"] +Weight_M*df["E1"] +Weight_M*df["E2"] +Weight_M*df["E3"] +Weight_F*df["E4"])/100

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

df_A = pd.merge(df_A, df, on ='UID', how ='left')
df_A.to_csv('finalgrades_Sec_A.csv')
df_B = pd.merge(df_B, df, on ='UID', how ='left')
df_B.to_csv('finalgrades_Sec_B.csv')
df_C = pd.merge(df_C, df, on ='UID', how ='left')
df_C.to_csv('finalgrades_Sec_C.csv')

