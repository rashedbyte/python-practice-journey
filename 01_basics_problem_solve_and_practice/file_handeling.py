import os
import pathlib

# f = open('hello.text',"r")
# x = f.read()
# print(x)


# # Standar way for file operation in python 

# with open('hello.text', 'r') as f:
#     content = f.read()
#     print(content)
    

# with open('hello.text', 'w') as w:
#     write = w.write("hello world")


# with open('hello.text', 'a') as append:
#     append.write("\nI'm Rashed from Bangladesh")
#     append.write("\nThis is a new line.")
#     append.write("\n")


# lines = ['i love python \n', 'i live java\n', 'i love fortan\n']

# with open("hello.text", "a") as list_append:
#     list_append.writelines(lines)

# f.close()

# #more function for file handeling 

# if os.path.exists('hello.text'):
#     print("file found")


# else:
#     print("file not found")


# file_path = pathlib.Path('hello.text')

# x = file_path.exists()
# print(x)
# if x  == True:
#     print("file exists")
# else: 
#     print("file not found")

# #others logic for check file 

# if file_path.exists():
#     print("file found")
# else:
#     print("file not found")


# absulate_path = os.path.abspath('file_handeling.py')
# print(absulate_path)


# file_name = 'dict.py'
# file_size = os.path.getsize(file_name)
# kb_size = round(file_size / 1024, 1)

# print(f"{file_name} size is : {kb_size} kilobytes")



# #mini project with my simple idea

# file_name = str(input("enter your file name :"))

# if os.path.exists(file_name):
#     print(f"{file_name} is found.....")
#     file_path = os.path.abspath(file_name)
#     print("path : ", file_path)
#     file_size = round(os.path.getsize(file_name)/1024)
    
#     if file_size>1024:
#         file_size = round(file_size/1024,2)
#         if file_size > 1024:
#             file_size = round(file_size/1024,3)
#             print(f"file size : {file_size}GB")
#         else:
#             print(f"file size : {file_size}MB")

#     else:
#         print(f"file size : {file_size}KB")
    
# else:
#     print(f"{file_name} is not found !")


# with open('hello.text','r') as f:
#     print(f.read(5))





# task 01 : log file error filtering " data cleaning"

# x = open("error.log", 'x')
# error_file = 'error.log'
# file_name = 'server.log'
# with open(file_name , 'r') as f:
    
#     lines = f.readlines()
#     # print(lines)
#     for line in lines:
#         # print(line)
#         # print(line.find('ERROR'))
#         l_line = line.lower()
#         if l_line.find('error') == 1:
#             with open(error_file,'a') as e:
#                 e.write(line)
#                 print("write line : ", line)
# --------------practice code for task-01
    # lines = f.readlines()
    # print("lines : ", lines)
    # line = f.readline(1)
    # print("line : ",line)
    # read_line = f.readline()
    # small_read_line = read_line.lower()
    # print(read_line)
    # print("totall value : ", len(read_line))
    # print(read_line[2])

    # x = read_line.find("INFO")
    # y = small_read_line.find("info")

    # print(f"line: {small_read_line} {y}")
    # print(f"line : {read_line}, {x}")

    # if line[0] in '10':
    #     print("0 in first line")
    # else:
    #     print("0 is not in first line")


# task 02 : automated file organizer by extension (automotion script)

files_to_organize = [
    "break_continue.py", 
    "dict.py", 
    "error.log", 
    "file_handeling.py", 
    "function.py",
    "hello.txt", 
    "lambda_function.py",
    "loop.py", 
    "movie.mkv", 
    "music.mp3", 
    "note.txt", 
    "server.log",
    "todo.txt"
    ]
# python_script = []
# text_file = []
# other_file = []

# for file in files_to_organize:
#     # print(file)
#     # print(os.path.exists(file))
#     if (os.path.exists(file)) and ('.txt' in file):
#         print(f"{file} is a text file . Path : {os.path.abspath(file)}")
#         text_file.append(file)
        
#     elif (os.path.exists(file)) and ('.py'  in file):
#         print(f"{file} is a python script file. Path : {os.path.abspath(file)}")
#         python_script.append(file)
#     else:
#         print("file exitension is not match with python and text")
#         other_file.append(file)
        
for file in files_to_organize:

    x = file.endswith('.txt')
    print(x)