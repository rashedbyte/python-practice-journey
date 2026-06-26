#  ___________________practice real world problem _____________________________

#task - 01 (Crate a Book Object)

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         print(f"Book Created : {self.title}, by {self.author}")


# book1 = Book("Python Basic", "Jon Doe")
# book2 = Book("DSA Basics", "Jack Craly")


# # task - 02 (Car Start and Drive System)
# class Car:
#     def __init__(self, brand , speed):
#         self.brand = brand
#         self.speed = speed
#     def drive(self):
#         print(f"The {self.brand} car is driving at {self.speed} km/h")


# car1 = Car("Toyota", 124)
# car2 = Car("BMW", 130)

# car1.drive()
# car2.drive()


# # task - 03 (Employee office Tracking)
# class Employee:
#     company_name = "IBM Technology"
#     def __init__(self, name):
#         self.name = name

#     def show_info(self):
#         print(f"Employee : {self.name}, Company : {self.company_name}")


# e1 = Employee("Rashed")
# e1.show_info()
# e2 = Employee("Jesmin")
# e2.show_info()
# e3 = Employee("Mukta")
# e3.show_info()




# # task 04 (company name rebranding system)

# class Employee:
#     company = "IBM Technology"
#     def __init__(self,name):
#         self.name = name

#     def show_info(self):
#         print(f"Employee : {self.name}, company : {self.company}")

#     @classmethod
#     def rebrand(clsa, new_name):
#         print(f"---------------------\ncompany name changed ! \nold name : {clsa.company}")
#         clsa.company = new_name
#         print(f"new name : {clsa.company}\n---------------------")


#     # @classmethod
#     # def rebrand(cls, new_name):
#     #     print(f"---------------------\ncompany name changed ! \nold name : {cls.company}")
#     #     cls.company = new_name
#     #     print(f"new name : {cls.company}\n---------------------")



# e1 = Employee("Rashed")
# e1.show_info()
# e2 = Employee("Jesmin")
# e2.show_info()
# Employee.rebrand("IBM Cloud")
# e1.show_info()
# e2.show_info()


# # task 05 (car speed limit checker)
# class Car:
#     def __init__(self):
#         pass

#     @staticmethod
#     def speed_checker(speed):
#         if speed>=120:
#             print(f"{speed} is Over Speeding, slow down")
#         else:
#             print(f"{speed} is safe speed")



# c1 = Car()
# c1.speed_checker(100)


# # task 06 interview level (secure ride sharing profile for rider)

# class Rider :
#     def __init__(self,name, password,blance):
#         self.name = name
#         self.__passwrod = password
#         self.__blance = blance
    
#     def show_info(self,password):
#         if password == self.__passwrod:
#             print(f"name : {self.name}, bal : {self.__blance}")
#         else:
#             print("wrong password")
    
#     def update_pass(self, password):
#         if password == self.__passwrod:
#             self.__passwrod == password
#             print("password updated")
#         else:
#             print("wrong password")

#     def credit(self,password,dipo_bal):
#         if password == self.__passwrod:
#             self.__blance -= dipo_bal
#             print(f"balance credited : {dipo_bal} , new balance  {self.__blance}")
#         else:
#             print("wrong password")
#     def debit(self,debt_bal):
#             self.__blance += debt_bal
#             print(f"balance debited : {debt_bal} , new balance  {self.__blance}")


# r1 = Rider("rashed", "1234", 50000)
# r1.show_info("1234")
# r1.debit(6000)
# r1.show_info("1234")
# r2 = Rider("mukta", "3452", 50000)
# r2.show_info("3452")


# print(r2.__blance)   // error : AttributeError: 'Rider' object has no attribute '__blance'



# task 7 : (smart rider email generator) topic property decorator
# class Rider: 
#     def __init__(self,name,rider_id):
#         self.name = name
#         self.rider_id = rider_id
    

#     @property
#     def email(self):
#         return f"{self.name}_{self.rider_id}@uber.com"
    
# r1 = Rider("rashed",727)
# print(r1.email)



# wrong code first time practice 
# class Rider: 
#     def __init__(self,name,rider_id):
#         self.name = name
#         self.rider_id = rider_id
    

#     @property
#     def email(self):
#         self.email = f"{self.name}_{self.rider_id}@uber.com"
#         return self.email
    
# r1 = Rider("rashed",727)
# print(r1.email)