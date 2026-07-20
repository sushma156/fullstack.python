product_price=5000
delivery_charges=100

total=product_price+delivery_charges
print(total)


########
a=10
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
student=10
groups=2

print(student//groups)

##############

followers=100
followers +=1
print(followers)

############

saved_password="ABC"
entered_password="ABC"

print(saved_password == entered_password)


#############

balance=5000
pin_correct=True
if balance >=1000 and pin_correct:
    print("withdraw allowed")
else:
    print("failed")


###### billing calculator

product=input("enter product name:")
price=float(input("enter the price:"))
quantity=int(input("enter the quantity:"))
discount=int(input("enter the discount:"))
total=price*quantity
final_bill=total-discount

print("product:",product)
print("total amount:",total)
print("final bill:",final_bill)

########### conditions

password=input("enter the password:")
if password=="ss123":
    print("login successful")
else:
   print("login failed")

age=20
if age>=18:
    print("eligible to vote")

CGPA=9
if CGPA>=9:
    print("grade A")
elif CGPA>=8:
    print("grade B")
elif CGPA>=7:
    print("grade C")
else:
    print("fail")

#logical conditions
###########AND###############
age=26
salary=50000
if age>18 and salary>30000:
    print("Loan approved")
################OR############
day="sunday"
if day=="sunday" or day=="saturday":
    print("holiday")
#################NOT#############
login=False
if not login:
    print("please login")

###########using function#########

def withdraw_money():
    pin=input("enter thr pin:")
    if pin=="1234":
        print("login successful")
        amount=int(input("enter the amount:"))
        balance=5000
        if amount<=balance:
            balance=balance-amount
            print("withdraw successful")
            print("remaining balance:",balance)
        else:
            print("insufficient balance")
    else:
        print("incorrect pin")

withdraw_money()
  
########## for LOOP #############

for i in range(2,6):
    print(i)
users=["thu,tha,thi"]
for users in users:
    print("message sent to",users)

######to print characters from string(ch/char)#############
name="dhoni"

for ch in name:
    print(ch)

###########WHILE LOOP#############
count=1
while count <=5:
    print(count)
    count += 1
    
############continue statement(only specified iteration will be skipped and others will be executed)
for i in range(10):
    if i==5:
        continue
    print(i)

##############break statement(until specified iteration will be executed)
for i in range(10):
    if i==5:
        break
    print(i)

password=""
while password !="1234":
    password=input("enter password:")
    print("login success")

###########LIST and APPEND,Remove######################
student1="ss"
student2="sam"
student3="san"
student =[
    "ss",
    "sam",
    "san"
]
student.append("mo")
student.append("mad")
print(student)