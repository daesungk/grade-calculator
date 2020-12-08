import pandas as pd 
import numpy as np
import random
import string

# Creat Dataframe
df = pd.DataFrame()

# Setting
NumOfRows = 540
NumH = 36
NumQ = 6
NumE = 4

# Column lists
Col_List_Q = []
Col_List_E = []
Col_List_H = []

for i in range(NumH):
    Col_List_H.append("H"+str(i+1))
for i in range(NumQ):
    Col_List_H.append("Q"+str(i+1))
for i in range(NumE):
    Col_List_H.append("E"+str(i+1))

Col_List_info = ["UID", "UIN", "Name"]
Col_List_A = Col_List_Q + Col_List_E + Col_List_H
Col_List = Col_List_info + Col_List_A

# Generate Col_List_info
def Rand_Char(y):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(y))
for i in range(NumOfRows):
    df.at[i,"UID"] = Rand_Char(random.randint(5,13)) + "@school.edu"
for i in range(NumOfRows):
    df.at[i,"UIN"] = str(random.randint(1000000001,10000000000))
for i in range(NumOfRows):
    df.at[i,"Name"] = Rand_Char(random.randint(5,10)).capitalize() + " " + Rand_Char(random.randint(5,10)).capitalize()

# Generate Col_List_A
### How to generator scores for assignments: "Random" or "Zero"
Gen_Mode = "Random" 
### Gen_Mode = "Zero"
for X in Col_List_A:
    for i in range(NumOfRows):
        if Gen_Mode == "Random":
            df.at[i, X] = random.randint(50,100)
        else:
            df.at[i, X] = 0

# Export csv file
df.to_csv('gradebook.csv')
