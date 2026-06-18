print("Find the sum of all elements in a list")
number =[20,59,95,38,84,74,26]
total=sum(number)
print("sum of all elements: ",total)

val=list(map(int,input("Enter the value: ").split()))
tot=0
for num in val:
    tot+=num
print("sum of all elements: ",tot)

print("\nlist of integers,find and print the maximum element")
maximum=max(number)
print("maximum element in the list: ",maximum)

element=list(map(int,input("Enter the value: ").split()))
highest=element[0]
for i in element:
    if i>highest:
        highest=i
print("maximum element in the list: ",highest)

value=[57.7,64.7,764.6,86.76]
print("\nminimum element in a list of floating-point numbers")
minimum=min(value)
print("minimum element in the list: ",minimum)


min_val=list(map(float,input("Enter the value: ").split()))
minimum_val=min_val[0]
for i in min_val:
    if i<minimum_val:
        minimum_val=i
print("minimum element in the list: ",minimum_val)

print('-'*50)
