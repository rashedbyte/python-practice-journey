#dictionary assign in = {} curly bracess
#dictionary assign item in key value pair
#dictionary is not indexable, [x]--> dic1[1]  [R]---> dic1[key]
#dictionary key is immutable


# a = {'rahim':23, "karim":43, "list":[203,32,53,21]}
# print(a)
# print(type(a))

# for i in a:
#     print(i)

# for i in a.values():
#     print("values : ", i)

# for i in a.keys():
#     print("keys is : " , i)

# for k,v in a.items():
#     print("key values : ", k ,":", v)

# dict1 = {1,2,3,4}
# dict2 = {"mango", "banana", "cherry", "blackberry"}

# joint_list = list(zip(dict1,dict2))
# joint_dict = dict(zip(dict1, dict2))

# for n,val in enumerate(joint_list,start=1):
#     print(f"joint list value {n}: {val}")


# for k,v in joint_dict.items():
#     print(f"key : {k}  value : {v}")


"""_________real world problem solving using python dictionary________"""


'''first problem'''

inventory = {
    "P101":{"NAME":"LAPTOP","STOCK":5},
    "P102":{"NAME":"MOUSE","STOCK":0},
    "P103":{"NAME":"KEYBOARD","STOCK":12},
    "P104":{"NAME":"MONITOR","STOCK":2},
    "P105":{"NAME":"HEADPHONE","STOCK":3}
}




for p_id , p_info in inventory.items():
    print("_________________________________")
    print("_________________________________")
    print("product id : ", p_id)
    print("product name : ", p_info["NAME"])
    if p_info["STOCK"] == 0:
        print(f"{p_info['NAME']} is stock finished, please order now!")
        print(f"stock size is : {p_info['STOCK']}")
    elif p_info['STOCK'] < 3 : 
        print(f"{p_info['NAME']} is almost stock finished, please refill now.")
        print(f"Stock size is : {p_info['STOCK']}")
    else:
        print(f"{p_info['NAME']} is Stock available!")
        print(f"Stock size is : {p_info['STOCK']}")






for k,v in inventory.items():
    for k1,v1 in v.items():
        print(v1)

print("_________________________________")
print("_________________________________")
for k,v in inventory.items():
    print("product id : ", k)
    p_name = v["NAME"]
    stock_size = v["STOCK"]
    print(f"product name : {p_name} \nStock available : {stock_size}.")
    print("_________________________________")
    print("_________________________________")



"""second problem"""

users = [
    {"name":"Rashed", "age":23, "city":"Rangpur","active":True},
    {"name":"Jesmin", "age":22, "city":"Rangpur", "active":True},
    {"name":"Mukta", "age":21, "city":"Rangpur", "active":True},
    {"name":"Ali", "age":23, "city":"Dhaka", "active":False},
    {"name":"abu musa", "age":25, "city":"Shariatpur", "active":True},
    {"name":"Abu Naim", "age":26, "city":"Dinajpur", "active":True},
    {"name":"Karim uddin", "age":30, "city":"Rangpur", "active":True}
]


rangpur_users = []


for user in users:
    x = user["city"]
    if x == "Rangpur" :
        # user_list = []
        # user_list.append(user['name'])
        # user_list.append(user['age'])
        # user_list.append(user["city"])
        # rangpur_users.append(user_list)
        rangpur_users.append(user['name'])

print(rangpur_users)