import pandas as pd
import numpy as np

data={'Emp_Name':['Sachin','Rajesh','Anitha','Rithika','Mithra'],
      'Age':[25,28,24,30,27],
      'Department':['HR','IT','Finance','Marketing','Operations'],
      'Salary':[35000,55000,48000,52000,60000]}

df=pd.DataFrame(data)
print('col name in list:',df.columns.tolist())

print('\nadd experience col')
df['Experience']=[5,3,6,2,5]
print(df,'\n',df.columns.tolist())

print("\n reomve the col")
df1=df.copy()
df_rem=df1.drop(['Age','Experience'],axis=1)
print(df_rem,'\n',df_rem.columns.tolist())

print('\n renaming the col')
df_rename=df.copy()
df_rename.rename(columns={'Emp_Name':'Name',
                          'Department':'Dep',
                          'Salary':'Annual Salary'},inplace=True)
print(df_rename,'\n',df_rename.columns.tolist())

print("\n convert the data sets to csv file")
df.to_csv('employee.csv',index=False)
file=open('employee.csv','r')
print(file.read())
file.close()

print("\n read csv file")
df_csv=pd.read_csv(r'employee.csv')
print(df_csv,'\n',df_csv.shape)

print("\n convert the data set to excel file")
df.to_excel('employee.xlsx',index=False)
data=pd.read_excel('employee.xlsx')
print(data)

print("\n type conversion")
df_type=df.copy()
df_type['Salary_Float']=df['Salary'].astype(float)
print(df_type)

