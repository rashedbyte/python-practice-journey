import functools

#anonymous function ---- Unnamed
def square (x):
    return x*x

print(square(5))

#lambda argument:expression

x = lambda y : y*y

print(x(3))
 
add = lambda p , m : p+m

print(add)
print(add(23,43))


students = [("c",60),("a",54),("b",100)]

sorted_student_with_marks = sorted(students,key=lambda x:x[0])
sorted_student_with_name = sorted(students, key = lambda x : x[1])
print(sorted_student_with_marks)
print(sorted_student_with_name)


num = [12,423,53,12,214,2541,123,541,23]
sorted_num = sorted(num)
print(sorted_num)


#map(), filter(), reduce()


#map()
nums = [1,2,3,4]
sq = list(map(lambda x : x*x,nums)) #map(ki korte chi, kar upor korte chai)
print(sq)

# filter()
filter_n = [1,2,3,4,5,6,7,8,9,10]
even_sq = list(map(lambda x : x % 2 == 0, filter_n))

print(even_sq)
even_sq = list(filter(lambda x :x % 2 == 0, filter_n))

print(even_sq) 


# reduce()
sum  = functools.reduce(lambda x,y : x+y, filter_n)
print(sum)





# __________real world problem_____________

# probem no 01 ---- discount 10% in a list using map() and lambda function 

old_price = [234,532,124,642,751,995,781,692]

new_price = list(map(lambda x:round(x*0.90),old_price))
print(new_price)


#problem 2 --- using filter() to create a new list where marks > 50

marks = [24,53,64,32,35,46,93,59,21,34,64,23,82,72,50, 74, 83,73]

student_pass = list(filter(lambda x : x>=50, marks))
print(student_pass)


# problem 3 ---- using  reduce() to calculate totall

cart_totals = [230,354,563,123,643,324,325,643,345,923,890,798]

totall = functools.reduce(lambda x,y:x+y, cart_totals)
print(totall)


# real world problem 4. filter() এবং lambda ব্যবহার করে শুধু ইলেকট্রনিক্স প্রোডাক্টগুলোর একটি নতুন লিস্ট তৈরি করুন।

products = [
    {"name":"laptop","category":"electronics", "price":45000},
    {"name":"shirt", "category":"clothing", "price":1200},
    {"name":"smartphone", "category":"electronics", "price":23000},
    {"name":"bed","category":"clothing", "price":3000},
    {"name":"Keyboard", "category":"electronics", "price":2000}
]



electronics_product = list(filter(lambda x : x['category']=="electronics",products))
print(electronics_product)



#real world problem 5, added 15% vat in a list item 

old_price = [234,3242,423,52354,234,5234523,4234,3424]

vat_added_price = list(map(lambda x : round(x*1.15), old_price))
print(vat_added_price)


# real world problem no 6 , calculate totall in list of dictionary

inventory = [
    {"product":"mouse", "stock":32},
    {"product":"keyboard", "stock":234},
    {"product":"laptop", "stock":340},
    {"product":"headphone", "stock":580},
    {"product":"ram", "stock":320}
]

# totall_stock = functools.reduce(lambda x ,y :x['stock']+y['stock'], inventory) , aita ami nije nije likhe chi , nicher line gemini er clue dekeh
totall_stock = functools.reduce(lambda x ,y :x+y['stock'], inventory , 0)
print(totall_stock)


#real world problem 7, filter expensive products using lambda and filter()

products  = [
    {"name":"smartphone", "price":25000},
    {"name":"laptop", "price":50000},
    {"name":"headphone","price":2500},
    {"name":"montor", "price":22000},
    {"name":"mouse", "price":2500}
]

expensive_product = list(filter(lambda x : x['price']>20000, products))
print(expensive_product)



#real world problem 8 , convert cunrrency to usd (map()+lambda)

bdt_price = [2345,324,23565,4324,3214,256423,234234,6345,23423,2342354,192000, 200434]

usd = list(map(lambda x : round(x /120, 2), bdt_price))
print(usd)


print(round(234.5824,1))



#problem 8 , find maximum price 

cart_prices = [450, 1200, 99, 350, 2100, 850]

maximum = functools.reduce(lambda x,y: x if x>y else y, cart_prices)
print(maximum)
