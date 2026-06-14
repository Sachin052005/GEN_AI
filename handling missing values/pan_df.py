import pandas as pd
import numpy as np
data={'ID':[101,102,103,104,105],
    'Name':['Sachin','Rajesh','Anitha','Rithika','Mithra'],
    'Age':[20,21,19,22,20],
    'Department':['CSE','IT','ECE','CSE','MECH'],
    'Fees':[50000,45000,78000,67000,83000],
    'Marks':[85,78,92,88,95]}
df=pd.DataFrame(data)
dep_avg=df.groupby('Department')['Fees'].mean().astype(int)
print(dep_avg)

print("\nCount_Dep")
count_dep=pd.DataFrame(data)
print(count_dep.groupby('Department').size())

print("\n using Agg")
agg=pd.DataFrame(data)
print(agg.groupby('Department')['Fees'].agg(['mean','median','min','max','std']))

miss_data={'ID':[101,102,103,104,105],
    'Name':['Sachin',np.nan,'Anitha','Rithika','Mithra'],
    'Age':[20,21,19,np.nan,20],
    'Department':['CSE','IT','ECE','CSE','MECH'],
    'Fees':[50000,45000,78000,67000,np.nan],
    'Marks':[85,78,92,88,95]}

print("\n handling missing data")
handling=pd.DataFrame(miss_data)
print(handling)

print("\n count missing val")
print(handling.isnull().sum())

print("\n filter from top to atlast")
print(handling[handling.isnull().any(axis=1)])
print(handling[handling.notnull().all(axis=1)])

print("\n print only notnull val")
clean=handling.dropna()
print(handling.shape)
print(clean.shape)
print(clean)

clean1=handling.copy()
clean1['Name'] = clean1['Name'].fillna('Rajesh')
clean1['Age'] = clean1['Age'].fillna(clean1['Age'].mean())
clean1['Fees'] = clean1['Fees'].fillna(83000)
print(clean1)

print("\n fill nan val by previous val")
clean2=handling.copy()
clean2=clean2.ffill()
print(clean2)

print("\n fill nan by next val")
clean3=handling.copy()
clean3=clean3.bfill()
print(clean3)
