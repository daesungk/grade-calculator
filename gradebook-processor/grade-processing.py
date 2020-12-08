import pandas as pd 
import numpy as np
import random
import string

# Creat Dataframe
df = pd.read_csv('../data/gradebook.csv')

# Column lists
Col_List = list(df.columns)
Col_List_info = ["UID", "UIN", "Name"]
Col_List_Q = [string for string in Col_List if "Q" in string]
Col_List_H = [string for string in Col_List if "H" in string]
Col_List_E = [string for string in Col_List if "E" in string]
Col_List_A = Col_List_Q + Col_List_E + Col_List_H
Col_List = Col_List_info + Col_List_A

NumOfRows = df.shape[0]
NumH = len(Col_List_H)
NumQ = len(Col_List_Q)
NumE = len(Col_List_E)

# Averages by Groups
df["Q_Avg"] = df[Col_List_Q].mean(axis = 1)
df["H_Avg"] = df[Col_List_H].mean(axis = 1)
df["E_Avg"] = df[Col_List_E].mean(axis = 1)

# The lowest scores
df["Q_L1"] = df[Col_List_Q].apply(lambda row: row.nsmallest(2).values[0],axis=1)
df["H_L1"] = df[Col_List_H].apply(lambda row: row.nsmallest(2).values[0],axis=1)
df["H_L2"] = df[Col_List_H].apply(lambda row: row.nsmallest(2).values[-1],axis=1)

# Drop the lowest scores from HW and Quiz
df["Quiz"] = (df[Col_List_Q].sum(axis=1)-df["Q_L1"])/(NumQ-1)
df["HW"] = (df[Col_List_H].sum(axis=1)-df["H_L1"]-df["H_L2"])/(NumH-2)

Col_List_Fin = Col_List_info + ["HW", "Quiz"] + Col_List_E

df_proc = df[Col_List_Fin]
# Export csv file
df_proc.to_csv('gradebook-proc-sel.csv')
df.to_csv('gradebook-proc-all.csv')
