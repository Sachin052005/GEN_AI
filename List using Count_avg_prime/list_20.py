'''
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
'''
#-------------------------------------------------------------------------

print("Average of all numbers in a list")
number=[75,86,95,27,73,30]
val=sum(number)
print(val)
average=val/len(number)
print(round(average,2))

print("Average of all numbers in a list")
num=list(map(int,input("Enter the number: ").split()))
total=0
for i in num:
    total+=i
avg=total/len(num)
print(int(avg))
print('-'*30)

print('\n Number of even numbers in a given list')
values=[74,95,94,95,28,84,854]
count=0
for num in values:
      if num%2==0:
          print(num,end=' ')
          count+=1
print("\n Number of even numbers: ",count)

numbers=list(map(int,input("Enter the values:").split()))
count_Even=0
for i in numbers:
    if i%2==0:
        print(i,end=' ')
        count_Even+=1
print("\n Number of even number in the list: ",count_Even)
print('-'*30)

input_val=int(input("Enter the number: "))

if input_val>1:
    for i in range(2,input_val):
        if input_val%i==0:
            print(input_val ," is not a prime number")
            break
    else:
        print(input_val," is a prime number")
else:
    print(input_val ," is not a prime number")
      























