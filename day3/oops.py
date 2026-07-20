class student: #class name(class is a blueprint used to create an object)
    name="sushma" #attribute
    def study(self):
        print("sushma is studying")
s1=student()   #s1 is a object(object represents the class)
print(s1.name)
s1.study() #study is a method

class student:
    def details(self):
        print("had breakfast")
s1=student()
s1.details()

student.details(s1)

#######constructor#########

class student:
    def __init__(self,name,age): #init is constructor(constructor runs automatically when an object is created)
         self.name=name
         self.age=age  
s1=student("ram",20)
s2=student("sush",21)
s3=student("mouni",22)
print(s1.name,s2.name,s3.name)
print(s1.age,s2.age,s3.age)

class bank:
    def __init__(self,balance):
        self.balance=balance

    def check_balance(self):
        print(self.balance)

account=bank(5000)
account.check_balance()

class user:
    def __init__(self,name):
        self.name=name
    def login(self):
        print(self.name,"logged in")

u1=user("mouni")
u1.login()

######single inheritance###########
class father:
    def house(self):
        print("father as a house")

class son(father):
    def bike(self):
        print("son as a bike")
s=son()
s.house()
s.bike()

##########multilevel inheritance##############
class Grandparent:
    def home(self):
        print("Home")

class Parent(Grandparent):
    def home(self):
        print("Home")

class Child(Parent):
    def home(self):
        print("Home")
    
c = Child()
c.home()


######multiple inheritance###########
class Father:
    def money(self):
        print("Money")

class Mother:
    def love(self):
        print("Love")

class Child(Father, Mother):
    pass

c = Child()
c.money()
c.love()

###########hierarichal inheritance#############
class Parent:
    def display(self):
        print("I am Parent")

class Son(Parent):
    def boy(self):
        print("I am Son")

class Daughter(Parent):
    def girl(self):
        print("I am Daughter")

s = Son()
d = Daughter()

s.display()
d.display()

######hybrid inheritance#########
class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

class C(A):
    def print_data(self):
        print("Class C")

class D(B, C):
    def result(self):
        print("Class D")

d = D()

d.show()
d.display()
d.print_data()
d.result()

#####django magic methods############ (# __init__,__str__,__len__)
class student:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name
    

s=student("king")
print(s)

###########decorators###########
def login(func):
    def wrapper():
        print("Checking Login")
        func()
    return wrapper
@login
def dashboard():
    print("Dashboard page")
dashboard()

def message(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")
    return wrapper
@message
def hello():
    print("hello python")
hello()
    
def hi():
    print("hi python")
hi()

def mouni():
    print("mouni is eating")
mouni()

######python to json##########
import json

student={
    "name":"sush",
    "age":22
}
data=json.dumps(student)
print(data)

########json to python###########
import json

student = '{"name":"sush","age":22}'

data = json.loads(student)
print(data)

import requests

response=requests.get(
    "https://api.github.com/users/python"
)

data=response.json()
print(data)