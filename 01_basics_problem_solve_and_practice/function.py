# print("hello ")
# user_name = input("Enter your name : ")

# print(f"hello {user_name}")
# print(user_name * 2)

# x = [23,34,52,13,43,52,93,59]

# def avg (x):
#     n = len(x)
#     return sum(x)/n

# print(max(x))
# print(min(x))
# print(avg(x))
# print(sum(x))



#kind of function 
# 1. no input no return
# 2. no input return interger , string, char, etc
# 3. input str, int, char etc and no return
# 4. input str int , char etc and return char, int , string , etc


#type 01 - no input no return

# def hello ():
#     print("hello")

# hello()

# #type 2. no input retun anything type
# def hello ():
#     return "hello"

# x = hello()
# print(x)

# # type 3 . input anything , return nothing

# def add (x,y): # x,y perameter
#     print(x+y)

# add(20,30) # 20,30 argument

# # type 4. input data and return data 
# def add(n1,n2): #n1 and n2 is perameter
#     return n1 + n2

# result  = add(20,30) # 20 , 30 is both are argumnet
# print(result)


#args in python function perameter

# def addition(a,b): #normal perameter
#     result  = sum([a,b]) #result = a+b
#     return result

# addition(int(23), int(32))


# def addition(*args):
#     result = args #args return a tuple 
#     print(result, "  ", type(args))
#     print(sum(result))

# addition(203,324,234,23,23,423,4,23423,97)


# def addition_with_args(*args): #args perameter in function 
#     result = sum(args)
#     return result

# add  = addition_with_args(203,354,32134,32523,35,2345,235,234,234)
# print(add)
# def addition_with_args(*someHow): #args perameter in function 
#     result = sum(someHow)
#     return result

# add  = addition_with_args(203,354,32134,32523,35,2345,235,234,234)
# print(add)


# def my_func (f_name, l_name, age):
#     print(f"my name is {f_name} {l_name}, and I'am {age} years old.")

# my_func("rahim","khan", 35)
# my_func(25,"khan", "rahim")

# my_func(age = 25, l_name= "Ali", f_name="Rashed")


# arbitary number of keyword arguments

# def func(**kewargs):
#     print(f"my name is {kewargs['name']} , and I'm {kewargs['age']} years old.")
#     print(kewargs) #kewargs return a dictionary

# func(
#     name = "Md Rashed Ali",
#     age = 23,
#     marks = 23,
#     subject = "english"
# )
# def func(**any):
#     print(f"my name is {any['name']} , and I'm {any['age']} years old.")
#     print(any) #kewargs return a dictionary

# func(
#     name = "Md Rashed Ali",
#     age = 23,
#     marks = 23,
#     subject = "english"
# )





# default perameter in python function 

def print_my_name(f_name, l_name): #normal perameter
    print("form normal function : " , f_name, l_name)

print_my_name("Md " , "Rashed")

def print_khan_group_name(f_name,l_name = "Khan"):
    print("from default perameter : " , f_name, l_name)

print_khan_group_name("Rashed ") #if second perameter is not fill , use default perameter value automatically
print_khan_group_name("Fill : Rashed"," Ali") #if second perameter is fill , use second perameter.

