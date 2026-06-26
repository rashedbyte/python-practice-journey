#error and exception
#compile time and runtime 
#compile itme(error)      ----> syntax error, indentation error, 
#run time (exception)     ----> zero division error, value error, index error, key accessing error

#error can't handle(compile time error),  exception can handle (run time error)


# try:
#     with open('rahim.txt', 'r') as f:
#         print(f.read())  
# # except Exception as e: #when exception is not exists use this line
# #     print("file not found" , e)
# except FileNotFoundError:
#     print("file not found" )


# try:
#     with open('set.py', 'r') as f:
#         print(f.read())  
#         x = 20/5
#         y = int('234')
# except FileNotFoundError:
#     print("enything else")
#     print("file not found" )
# except ZeroDivisionError as zd:
#     print("anything else")
#     print("name : " , ZeroDivisionError, zd)
#     print("name : " , type(ZeroDivisionError))
# except ValueError as v:
#     print("anythinig else")
#     print(v)

# else:
#     print("nothing else")     


# # finally:
# #     print("print alltime nothing else or anything else")




# file_name = str(input("enter your file name : "))

# # if not file_name.endswith('text'):
# #     print("invalid file")
# # else:
# #     print("file ok...")

# def check_file(file_name):
#     if not file_name.endswith('text'):
#         print("invalid file")
#         raise ValueError("only .tex file are allowed")
#         # raise ValueError("only .tex file are allowed")
#     else:
#         print("file ok...")



# try:
#     check_file(file_name)
# except ValueError as v:
#     print("something else , name : ", v)

# else:
#     print("nothing else, everything okk !")




# real world problem 
# problem no 01 === Secure User input with type conversion (data validation)

# def type_conversion(user_input):
#     return user_input




# while True:
#     try:
#         age = int(input("enter your age : "))
#     except ValueError as v:
#         print("Error : Invalid input! age must be a valid number.")
#     else:
#         print(f"success: age {age} registred successfully.")
#         break




def connection_check(status_code):
    if status_code != 200:
        raise ConnectionError(f"Server Error!{status_code}")
    else:
        print("everything ok \nTesting with 200....")


status_code = 0
try:
    status_code = int(input("Enter Status code : ")) 
    connection_check(status_code)
except ValueError as v:
    print("value error , must use a number")
except ConnectionError as v:
    print("Caught an exception : server return an error status!", v)

