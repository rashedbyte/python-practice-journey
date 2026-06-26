# a = 10 #global variable 

# print(a)
# def func ():
#     y = 30 #local variable 
#     a = 200
#     print("local a =  ",a)
#     print("y = ", y)

# func()
# print("global a = ", a)

 
#  #LEGB
#  # LOCAL
#  # ENCLOSING
#  #GLOBAL
#  #BUILT IN SCOPE


# n = 20 # global variable

# def outer():
#     global n
#     n = "enclosing" #enclosing variable
#     def inner():
#         n = "local variable"
#         print("n form inner function : variable ", n)
#     print("n from outer enclosing variable : ", n)
#     inner()


# outer()
# print("n from global variable",n)



# var = 'global var'
# print("global var = " , var)
# def check ():
#     global var
#     var = 'using enclosing var'
#     print("enclosing var = ", var)
#     def inner():
#         # var = 'local var'
#         # nonlocal var
#         var = 'using non-local'
#         print("local var = " , var)

#     inner()
#     print("encloasing var : ", var)

# check()

# print("global var = ", var)


#real world machine learning problem, "Global Model Hyperperameters Tuning"

learning_rate = 0.01

def train_default_model():
    print("Training model with default learning rate : ", learning_rate)

def train_experimental_model():
    learning_rate = 0.1
    print("Training model with experimental learning rate : ", learning_rate)


# train_default_model()
# train_experimental_model()

# print("current global learning rate : ", learning_rate)




# data preprocessing and cache management

data_cache = {}

def fetch_and_process_data(dataset_name):
    global data_cache
    if dataset_name in data_cache:
        print(f"returning cached data for {[dataset_name]}.....")
    else:
        print(f"processing {[dataset_name]} for the first time.....")
        
        data_cache[dataset_name] ="Processed"

    

fetch_and_process_data("titanic")
fetch_and_process_data("iris")
fetch_and_process_data("iris")
fetch_and_process_data("titanic")

print(f"final global cache storage : {data_cache}")




#User Authentication and login Tracker

# current_user = "Guest"
# print(f"initail user : {current_user}")
# def login_user(user):
#     global current_user
#     current_user = user
#     print(f"{current_user} is logged in successfully.")
#     return current_user

# def logout_user():
#     global current_user
#     current_user  = "Guest"
#     print("logged out successfully.")
#     return current_user

# print("updated user : " , login_user("Rashed"))
# print("final user : ", logout_user())