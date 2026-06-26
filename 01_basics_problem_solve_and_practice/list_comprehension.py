# list_a = [1,2,3,4,5,6] 

# print("main list : " , list_a)

# print("new list where item div by 2 : ")
# list_b = []
# for i in list_a:
#     if i%2==0:
#         list_b.append(i)
# print("new list using normal method : ", list_b)

# print("using comprehension : ")
# list_c = [i for i in list_a if i%2==0]
# print("comprehension method : ", list_c)


# print("new list if i%2==0 -- i**2, else i - i ")
# print("normal method")
# list_d = []
# for i in list_a:
#     if i%2 == 0:
#         i = i**2
#         list_d.append(i)
#     else:
#         list_d.append(i)
# print(list_d)

# print("comprehension methon")
# list_e = [i*i if i%2 == 0 else i for i in list_a]
# print(list_e)


#REAL WORLD PROJECT
# ----Cleaning user input data-----------

user_input = ["rashed  ", "aBu mUsa" , "tahmiD" , "ReDoan", "ShimuL" , "Jesmin", "muKta"]

cleaning_user_input = []
for name in user_input:
    # clean_data = cleaning_user_input.append(name.strip().title())
    x = name.strip()
    y = x.title()
    cleaning_user_input.append(y)
    print("old data :", name)
    print("clean data :", y)


cleaning_user_input = [name.strip().title() for name in user_input]

print(user_input)
print(cleaning_user_input)

#-----------E_commerce Product Price increment------------------

price_list = [20,34,53,123,53,120,250, 320, 500, 350, 1500, 80]

increment_price_list = []

for price in price_list:
    # increment_price_list.append(round(price * 1.05))
    new_price = int(round(price*1.05))
    increment_price_list.append(new_price)
    print(f"old_price : {price}, new price : {new_price}")
print(price_list)
print(increment_price_list)
print("----------------------------")
increment_price_list = [int(round(price*1.05))  for price in price_list]
print(price_list)
print(increment_price_list)


#_____________filtaring invalid or none values in database______________

data_set = ['hello', None, 30, None, 'hi', 100, 300, None, 2.4, 3.87, None , 3.70]

cleaning_data = []

for data in data_set: 
    if data is not None:
        cleaning_data.append(data)
print(cleaning_data)
print(data_set)

cleaning_data = [data for data in data_set if data is not None]
print(data_set)
print(cleaning_data)