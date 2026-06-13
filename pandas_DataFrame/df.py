import pandas as pd
import numpy as np

data={'ID':[101,102,103,104,105],
    'Name':['Sachin','Rajesh','Anitha','Rithika','Mithra'],
    'Age':[20,21,19,22,20],
    'Department':['CSE','IT','ECE','CSE','MECH'],
    'Marks':[85,78,92,88,95]}

df= pd.DataFrame(data)
print(df)
print("\nshape of the given table: ",df.shape)

print("\n print first 3 row using head")
row=pd.DataFrame(data)
print(row.head(3))

print("\n print first 2 row using tail")
row_last=pd.DataFrame(data)
print(row_last.tail(2))

print("\n Statistical summary")
sat=pd.DataFrame(data)
print(sat.describe())

print("\nprint particular col in reverse")
col_rev=pd.DataFrame(data)
print(col_rev['Name'][::-1])

print("\nprint particular col")
col=pd.DataFrame(data)
print(col[['Name','Department']][:2])

print("\nprint particular row")
row=pd.DataFrame(data)
print(col[:2])

print("\nprint particular row col detail")
row_col=pd.DataFrame(data)
print(row_col.iloc[0,3])

print("\nprint particular row detail")
full_row=pd.DataFrame(data)
print(full_row.iloc[2])


print("\nprint particular row_loc")
row_loc=pd.DataFrame(data,index=['A','B','C','D','E'])
print(row_loc.loc['A':'D'])

data_index={'ID':[101,102,103,104,105],
    'Name':['sachin','Rajesh','Anitha','sachin','Mithra'],
    'Age':[20,21,19,22,20],
    'Department':['CSE','IT','ECE','CSE','MECH'],
    'Marks':[85,78,92,88,95]}
print("\nprint particular col_filter")
col_filter=pd.DataFrame(data_index)
print(col_filter[col_filter['Name']=='sachin'])

print("\nprint particular filter_range")
filter_range=pd.DataFrame(data_index)
print(filter_range[filter_range['Marks']>90])

print("\nsorting age-small_to_large and name-large-_to_small")
sorting=pd.DataFrame(data)
print(sorting.sort_values(['Age','Name'],ascending=[True,False]))

print("\nAge Statistics:")
print(f"Average Age:{df['Age'].mean()}") 
print(f"Median Age:{df['Age'].median()}") 
print(f"Minimum Age:{df['Age'].min()}")
print(f"Maximum Age:{df['Age'].max()}")
print(f"Standard Deviation:{df['Age'].std()}")
print(f"Sum of all Ages:{df['Age'].sum()}")

print("\n add col fees")
df['dep_fees']=[40000,45000,30000,42000,50000]
print(df)

print("\n fees convert to dollar")
df['dep_dollar']= df['dep_fees']/96
print(df)

print("\n addtional fees ")
def addtional_fees(department):
    if department =='CSE':
        return 4500
    elif department =='IT':
        return 3800
    elif department =='ECE':
        return 5200
    else:
        return 1000

df['extra_fees']=df['Department'].apply(addtional_fees)
print(df)







