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
'''
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
'''    
#-----------------------------------------------------------------------------------
'''
print("Find the factorial of a given number")
num=int(input("Enter the number: "))
fact=1
if num<0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range (2,num+1):
        fact *=i
    print("Factorial of",num,"is",fact)
print('-'*30)

print("\nReverse a string without using any built-in functions")
val=input("Enter the word: ")
rev=""
for i in val:
    rev=i+rev
print("Reversed string: ",rev)
print('-'*30)
    
print("\nCheck if a given string is a palindrome")
txt=input("Enter a string: ")
reverse=""
for i in txt:
      reverse=i+reverse
if txt==reverse:
    print(txt,"is a palindrome")
else:
    print(txt,"is not a palindrome")
print('-'*30 )

print('\nRemove all duplicate elements from a list')
values=list(map(str,input("Enter the string: ").split()))
empty=[]
for i in values:
    if i not in empty:
        empty.append(i)
print("Duplicates are removed: ",empty)
'''
#----------------------------------------------------------------------
'''
print("Find the second-largest number in a list of integers")
val=list(map(int,input("Enter the numbers: ").split()))
val.sort()
print("\n Second largest number is: ",val[-2])
print('-'*30)

print("\nConvert a decimal number to binary")
num = int(input("Enter a decimal number: "))
binary = ""
if num == 0:
    binary = "0"
else:
    while num > 0:
        remainder = num % 2
        binary = str(remainder)+binary
        num = num // 2
print("Binary number:", binary)
print('-'*30)

print("\nFind the common elements between two lists")
list1=list(map(int,input("Enter the number: ").split()))
list2=list(map(int,input("Enter the number: ").split()))

common=[]
for i in list1:
    if i in list2 and i not in common:
        common.append(i)
print("Common elements: ",common)
'''
#------------------------------------------------------------------------
print("Sort a list of strings in alphabetical order")
words = input("Enter the strings separated by space: ").split()
words.sort()
print("Sorted list:", words)
print('-'*30)

print('\n Remove all spaces from a given string')
txt=input("Enter the a string: ")
space=""
for i in txt:
    if i!=" ":
        space+=i
print("String without space: ",space)
print('-'*30)

print("Check if two strings are anagrams")

str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not an Anagram")
print('-'*30)






