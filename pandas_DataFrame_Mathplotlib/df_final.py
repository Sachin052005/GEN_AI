import pandas as pd
import numpy as np
data=pd.DataFrame({'Name': ['Virat Kohli','Rohit Sharma','MS Dhoni','Jasprit Bumrah','KL Rahul']})
print('print the name in upper case\n',data['Name'].str.upper())
print('\nprint the name in lower case\n',data['Name'].str.lower())
print('\nprint the length of the name\n',data['Name'].str.len())
print('\nprint the first name only\n',data['Name'].str.split(' ').str[0])
print('\nprint the last name only\n',data['Name'].str.split(' ').str[1])
employee1=pd.DataFrame({'EmpID':[1,2,3,4],
                        'Name':['sachin','virat','ms dhoni','rohit']})
employee2=pd.DataFrame({'EmpID':[1,2,3,4],
                        'salary':[50000,45000,60000,83000]})
print(employee1,'\n',employee2)
merg_data=pd.merge(employee1,employee2,on='EmpID')
print('\n merged datas\n',merg_data)
print('\n Concatenating DataFrame\n')
data1=pd.DataFrame({'name':['sachin','sabarevason'],
                    'Age':[22,25]})
data2=pd.DataFrame({'name':['priya','dharshini'],
                    'Age':[24,27]})
merge_col=pd.concat([data1,data2])
print(data1,'\n',data2,'\nmerged col\n',merge_col)
students =pd.DataFrame({'Name': ['sabare', 'rithika', 'sachin', 'mithra', 'priya', 'vishnu'],
                        'Math': [88, 52, 93, 98, 84, 76],
                        'English': [60, 85, 88, 92, 87, 84],
                        'Science': [68, 90, 85, 91, 89, 82],
                        'Class': ['A', 'B', 'C', 'A', 'B', 'B']})
students['Average'] = students[['Math', 'English', 'Science']].mean(axis=1)
print("\nTop Student:")
top_student = students.loc[students['Average'].idxmax()]
print(top_student['Name'],'with avg of:',top_student['Average'].astype(int))
print("\nLowest Performing Student:")
low_student = students.loc[students['Average'].idxmin()]
print(f"{low_student['Name']} with avg of: {low_student['Average']:.2f}")

import matplotlib.pyplot as plt
visualization=pd.DataFrame({'Category':['A','B','C','D','E'],
                            'Values':[93,75,42,83,37]})
print('\n Bar plot using Pandas')
visualization.plot(kind='bar',x='Category',y='Values',title='Bar Plot of Categories')
print('\nLine plot using Pandas')
visualization.plot(kind='line',x='Category',y='Values',marker='o',title='Line Plot of Categories')
visualization.plot(kind='area',x='Category',y='Values',title='Area Chart')
visualization.plot(kind='box',title='Box Plot')
visualization.plot(kind='scatter',x='Category',y='Values',title='Scatter Plot')
plt.show()






