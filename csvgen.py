# import pandas 
import pandas as pd 
import numpy as np
import random

# Creat Dataframe
df = pd.DataFrame()
NumOfRows = 500

Col_List_info = ["UID", "UIN", "Name"]
Col_List_Q = ["Q1","Q2","Q3","Q4"]
Col_List_E = ["E1","E2","E3","E4"]
Col_List_H = ["H1","H2","H3","H4"]
Col_List_A = Col_List_Q + Col_List_E + Col_List_H
Col_List = Col_List_info + Col_List_A

for X in Col_List_A:
    for i in range(NumOfRows):
        df.at[i, X] = random.randint(50,100)

df.to_csv('gradebook-demo.csv')
