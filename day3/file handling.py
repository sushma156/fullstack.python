############file handling############
# file = open("student.txt", "w")
# file.write("hello mouni")
# file.close()

# print("Data written successfully")

# file = open("student.txt", "r")
# data = file.read()
# print(data)
# file.close()

# file = open("student.txt", "a")  
# file.write(" hello")
# file.close()

# print("Data appended successfully")

# file = open("student.txt", "r")
# print(file.read())
# file.close()

# ########Exception handling###########
# a=10
# b=0
# print(a/b)

# try:
#     a=10
#     b=0
#     print(a/b)
# except:
#     print("something went wrong")

# try:
#     num=int(input("enter number:"))
#     print(num)
# except ValueError:
#     print("only number allowed")


# try:
#     a=int(input("enter A:"))
#     b=int(input("enter b:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print(" enter only numbers")

# try:
#     file=open("data.txt")
#     print(file.read())
# except:
#     print("file error")
#####finnally block##########
# finally:
#     print("program completed")


#############else block##############
try:
    print(10/2)
except:
    print("error")
else:
    print("success")