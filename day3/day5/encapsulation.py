# encapsulation means wrapping data

######without encapsulation########
class bank:
    def __init__(self):
        self.balance=10000
account=bank()
account.balance=1000000000000
print(account.balance)

###with encapsulation###
class bank:
    def __init__(self):
        self._balance=10000
    def deposit(self,amount):
        self._balance+=amount
    def show_balance(self):
        print(self._balance)
account=bank()
account.deposit(5000)
account.show_balance()

####getter##########
class employee:
    def __init__(self,salary):
        self._salary=salary

    def get_salary(self):
        return self._salary
    
emp=employee(52485)
print(emp.get_salary())

#############setter###########

class employee:
    def __init__(self):
        self._salary=0
    def set_salary(self,amount):
        if amount>0:
            self._salary=amount
        else:
            print("invalid salary")

    def get_salary(self):
        return self._salary
    
emp=employee()
emp.set_salary(54678)
print(emp.get_salary())

##########polymorphism###########
#polymorphism means the same method name can perform
# different action depending on the object

class dog:
    def sound(self):
        print("dog barks")

class cat:
    def sound(self):
        print("cat meows")
Dog=dog()
Cat=cat()

Dog.sound()
Cat.sound()

class car:
    def move(self):
        print("car runs on road")
    
class train:
    def move(self):
        print("train runs on track")
Car=car()
Train=train()

Car.move()
Train.move()

class Phonepe:
    def pay(self):
        print("payment done through phonepe")

class Googlepay:
    def pay(self):
        print("payment done through Googlepay")

class Paytm:
    def pay(self):
        print("payment done through paytm")

P=Phonepe()
G=Googlepay()
PY=Paytm()

P.pay()
G.pay()
PY.pay()

######Abstraction#########
##abstraction means hiding internal implementation and
# showing only neccesary feature to the user

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

c = Car()
c.start()

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c=Cat()
d.sound()
c.sound()

