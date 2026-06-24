print("-------Object-Oriented Programming System-------")
class Student:
    name="Sachin"
    age=21
print(Student.name)
print(Student.age)
print('-'*30)
print("\nUsing Methods")
class Information:
    def Job(self):
        print("The interview is scheduled on 25th September at 9:00 AM")
info=Information()
info.Job()
print('-'*30)
print("\nUsing Constructor")
class Details:
    def __init__(self,Fathername,Mothername):
        self.Fathername=Fathername
        self.Mothername=Mothername

    def data(self):
        print("Father Name: ",self.Fathername)
        print("Mother Name: ",self.Mothername)
de=Details("Rajesh Kannan","Anitha")
de.data()
print('-'*30)
print("\nObject Updating Data")
de=Details("RAJESH KANNAN","ANITHA")
print("Before: ",de.Fathername,de.Mothername)
de=Details("rajesh","anitha")
print("After: ",de.Fathername,de.Mothername)
print('-'*30)
print("\nMultiple Object")
class students:
    def __init__(self,name,Age):
        self.name=name
        self.Age=Age

s1=students("sachin",21)
s2=students("suga",25)
s3=students("kavin",24)

print(s1.name,s1.Age)
print(s2.name)
print(s3.Age)
print('-'*30)

print("\n Data Abstraction")
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print("Area of Square: ",self.side*self.side)
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("Area of Rectangle: ",self.length*self.width)
s=Square(5)
s.area()
r=Rectangle(5,2)
r.area()
print('-'*30)     
        
