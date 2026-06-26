# a = [20,23,12,"ten", 53,39]
# b = ["apple", "banana" , 210, "cherry" ,  "mango" ,  "lemon"]

# for item in a : 
#     if ( type(item)== type(" ")):
#         print("this is string item in list: " , item)
#         break
#     else:
#         print(item)

# for item in b:
#     if (type(item)==(type(1))):
#         print("this is number item in list : ", item)
#         break
#     else:
#         print(item)


# print("hello world")

# for item in a:
#     if(type(item)==type("")):
#         continue
#     print(item)

# print("++++++++++++++++++++++++++")

# for item in b:
#     if(type(item)==type(0)):
#         continue
#     print(item)



"""ral world problem solve"""

user_email = ["rashed.byte@gmail.com", "abu_musa@gmail.com", "naim_hasan_at_gmail.com", "naim_hasan@gmail.com", "hello_at_gmail.com", "hello3gamli.com"]

valid_address = []
invalid_address = []


for email in user_email:
    if "@" not in email:
        print("invalid mail address : " ,email)
        continue
    print("valid mail address : " , email)


for mail in user_email:
    if "@" not in mail:
        invalid_address.append(mail)
        continue
    valid_address.append(mail)


print("============valid list==============")
for i in valid_address:
    print(i)


print("============invalid list============")
for i in invalid_address:
    print(i)
    
    
for i in range (20, 2):
    print(i)
