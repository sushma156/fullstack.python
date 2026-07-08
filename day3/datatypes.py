# student=("ram","sam","san")
# print(student[-2])
# ###########tuple is a collection used to store multiple values in a single variables and it is immutable#####################
# numbers=(10,20,30,40)
# print(numbers[-1])

# data=(1,2,3)
# data[1]=100
# print(data)

# ####duplicate values in tuple##########
# x=(1,2,3,1,1,1,2,3)
# print(x.count(1))
# print(x.count(2))

# #######index##########

# colors=("blue","green","pink")
# print(colors.index("blue"))
# print(colors.index("green"))

# #####tuple slicing#########

# num=(10,20,30,40,50)
# print(num[1:3])


# ####SETS(it is a collection of:removes duplicate values:set is a unique:unordered values############)
# x={1,2,3,2,1,1,1} #sets are unordered,so they do not have index positions.
# print(x)
# data={1,2,3}
# data.add(4)
# print(data)

# #######union(it combines both sets values) and intersection(it takes common values from the set)########
# a={1,2,3}
# b={3,4,5}
# print(a|b)

# a={1,2,3}
# b={3,4,5}
# print(a&b)


# ########function#############(it is a block of reusable code used to perform specific task)

# def greeting():
#     print("hello students")
# greeting()

# #######return function###########

# def add():
#     return 10+20
# result=add()
# print(result)

# def sub():
#     return 10-20
# result=sub()
# print(result)

# def mul():
#     return 10*20
# result=mul()
# print(result)

# def div():
#     return 10/20
# result=div()
# print(result)

# def mod():
#     return 10%20
# result=mod()
# print(result)

# def double():
#     return 10//20
# result=double()
# print(result)

# #######function arguments#############
# def add(a,b):
#     print(a+b)
# add(10,20)

# def sub(a,b):
#     print(a-b)
# sub(10,20)
    
# def mul(a,b):
#     print(a*b)
# mul(10,20)

# def div(a,b):
#     print(a/b)
# div(10,20)

# def mod(a,b):
#     print(a%b)
# mod(10,20)

# #########*args###########
# def mo(*numbers):
#     print(numbers)
# mo(10,20,30,40,50)

# def add(*num):
#     total=0
#     for i in num:
#         total+=i
#     print(total)
# add(10,20,30,40,50,60)

# ########***kwargs############

# def student(**details):
#     print(details)

#     student(
#         name="penta",
#         age=29,
#         job="sales"
#     )
#     print(details)


# def student(**details):
#     print("name:",details["name"])
#     print("age:",details["age"])
#     print("job:",details["job"])

# student(
#         name="penta",
#         age=29,
#         job="sales"
#     )
# print(student)

# ##########square root function######

# def sqrt(n):
#   return n*n
# print(sqrt(36))

# def sq(n):
#   return n*n
# print(sq(16))

# ##########lambda function#######
# square=lambda x:x*x
# print(square(25))

# add=lambda a,b:a+b
# print(add(10,20))

# Even= lambda x: "Even" if x % 2 == 0 else "Odd"
# print(Even(10))
# print(Even(1))

# penta=lambda name:name.upper()
# print(penta("rukhu vas"))

