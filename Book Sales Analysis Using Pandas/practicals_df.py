import pandas as pd

sales=pd.DataFrame({'Book':['Python','Java','C++','SQL','Python','Java','C++','SQL'],
                    'Branch':['City','Town','City','Town','North','South','North','South'],
                    'Copies':[12,8,15,10,14,9,11,13],
                    'Price':[650,700,800,500,650,700,800,500]})
print("Book Sales:")
print(sales)

sales['Revenue']=sales['Copies']*sales['Price']
print("\nWith Revenue Column:")
print(sales)
print("\nTotal Revenue: ",sales['Revenue'].sum())

print("\nRevenue by Copies:")
copies_revenue = sales.groupby('Copies')['Revenue'].sum().sort_values(ascending=False)
print(copies_revenue)

print("\nRevenue by Branch:")
branch_revenue = sales.groupby('Branch')['Revenue'].sum()
print(branch_revenue)
print(f"\nHighest Revenue Branch: {branch_revenue.idxmax()} with ${branch_revenue.max():,.2f}")

print("\nSorted by Revenue (highest first):")
print(sales.sort_values('Revenue', ascending=False).reset_index())
