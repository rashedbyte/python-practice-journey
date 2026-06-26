import random
# a  = [1,2,3,4,5,6,7,8,9,10]

# index = 0

# while index<= len(a)-1:
#     print(a[index])
#     index = index + 1


# for i in a:
#     print(i)

# print("Welcome to the games ")
# def games ():
#     print("________________________________")
#     user_input = int(input("Guess a number between 1 - 3 : "))
#     return user_input


# play = "yes"
# play_time = 0
# win_point = 0


# while play.lower() == "yes":
#     comp = int(random.randint(1,3))
#     user = games()
#     play_time += 1
#     if(user == comp):
#         print(f"you won ! your number is : {user}")
#         win_point = win_point+1
#     else:
#         print(f"you lose ! computer number is : {comp}")

#     play = input("play again (yes/no) : ")

# print("----------------------------------------------")
# print("This is End.")
# print("Your result")
# print("----------------------------------------------")


# print(f"you play {play_time} and \nWon {win_point} time.")
    


# x = random.random()
# print(x, f"{x} type is ", type(x))
# x = random.randbytes(10)
# print("randbytes", x, f"{x} type is ", type(x))
# x = random.randrange(2,20)
# print("random range", x , f"{x} type is ", type(x))
# x = random.SystemRandom()
# print("System Rand ", x, f"{x} type is ", type(x))
# x = random.uniform(10.0, 10.5)
# print("random uniform " , x, f"{x} type is ", type(x))
# x = random.randint(1,100)
# print("random int : ", x, f"{x} type is ", type(x))


## password check 

# wrong_pass = True
# while wrong_pass:
#     password = input("enter your password : ")
#     if(password == "1234"):
#         print("login Successfull.")
#         wrong_pass = False
 


### show post 

posts = [
    "আজকের আবহাওয়া চমৎকার! ☀️",
    "পাইথন প্রোগ্রামিং শিখতে আমার খুব ভালো লাগছে। 💻",
    "নতুন একটি বই পড়া শুরু করলাম। 📖",
    "বন্ধুদের সাথে বিকালের আড্ডা! ☕",
    "সাফল্যের কোনো শর্টকাট নেই, কঠোর পরিশ্রমই আসল। 💪"
]

index = 1
for post in posts: 
    print(f"{index} no. post : {post}")
    index += 1


#### pin check 

# pin = 1234

# wrong_pin = True
# user_input = int(input("enter your pin : "))
# while wrong_pin:
    
#     if user_input == pin:
#         print("login successfull. \nAccount blance: 324324324.0 BDT")
#         break
#     else:
#         user_input = int(input("Wrong pin. \nenter your pin again : "))



# correct_pin = 1234

# while True:  # লুপটি চলতেই থাকবে যতক্ষণ না আমরা নিজে থেকে 'break' করছি
#     user_input = int(input("Enter your pin: "))
    
#     if user_input == correct_pin:
#         print("Login successful. \nAccount balance: 324324324.0 BDT")
#         break  # পিন সঠিক হলে লুপ এখানেই শেষ
#     else:
#         print("Wrong pin. Please try again.\n")  # পিন ভুল হলে লুপ আবার ওপর থেকে শুরু হবে


cart_items = [150, 0, 320, 0, 450, 99]

result = 0
# for item in cart_items:
#     result = result+item

# print(result)

### next way 

for item in cart_items:
    if item == 0:
        continue
    result += item

print(result)