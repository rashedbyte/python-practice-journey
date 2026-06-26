#class(keyword) class_name: (indentation class body)

# class Mobile:
#     def __init__ (self):
#         pass
    #  def __init__(self,brand, mod):
    #       self.brand = brand
    #       self.mod = mod
    #       print("print from self constractor", brand,mod)


    #  def __init__(self ,type = "smartphone", brand = "citycel",model = "c234"):
    #     self.type = type
    #     self.type = brand
    #     self.type = model
    #     print("print from default 3 perameter constractor",type, brand, model)



# c1 = Mobile(brand = "nokia",model="n76")
# c1 = Mobile()
# c1.brand = "nokia"
# c1.model = "n75"



# c2 = Mobile(brand= "xiaomi", mod="redmi 9")



# class Car :
#     def __init__ (self):
#         self.brand = "toyota"
#         self.model = "corolla"

# c1 = Car()
# print(c1)
# print(c1.brand, c1.model)

# c2 = Car()
# c2.brand = "marcedes"
# c2.model = "xyz"
# print(c2.brand, c2.model)


# c3 = Car()
# c3.brand = "honda"
# c3.model = "abc"
# print(c3.brand, c3.model)


#__init__ : Double Under(Dunder Method) , constractor

#constractor 3types: ---> amar shadharonoto jake function boli takei class er vitore likhle function bole 
#   1.default constractor
#   2.parameterized constractor
#   3.default value constractor

# class car:
#     # def __init__(self):
#     #     self.brand = ""
#     #     self.model = ""
#     def __init__(self, brand, model):
#         self.brand=brand
#         self.model=model
#         self.process = process
#         print("print form perameterized constractor!",self.brand, self.model)


#     def __init__(self, brand = "honda", model="civics"):
#         self.brand=brand
#         self.model=model
#         print("print from default peramitarized ", self.brand, self.model)



# car1 = car("toytota", "corolla")
# print(car1.brand, car1.model)
# car2 = car("honda", "civics")
# print(car2.brand, car2.model)
# car3 = car()
# print(car3.model, car3.brand)
# c4 = car("bmw", "cv4")
# # c4.brand = "bmw"
# # c4.model = "c3r"
# # c4.process = "start process"
# print(c4.brand, c4.model)


# class Student:
#     def __init__(self):
#         print("print from default")
#     def __init__ (self, name, roll):
#         self.name = name
#         self.roll = roll
#         print("print from perameter 2", name , roll)
#     def __init__ (self, name, roll , id):
#         self.name = name
#         self.roll = roll
#         self.id = id
#         print("print from 3 perameter", name, roll, id)


# s1 = Student()
# s2 = Student("Rashed", 745144)
# s3 = Student("Jesmin", 745145, 32523)



# class School:
#     def __init__(self):
#         print("print from default constractor")

#     def cls(self,name , roll, reg, class_name = "three"):
#         self.name = name
#         self.roll = roll
#         self.reg = reg
#         self.class_name = class_name
#         print("print from class three\n")
#         print(f"registration submitted\nname : {self.name}\nroll : {self.roll} \n")
    
    
#     def cls(self,name , roll, reg, class_name = "five"):
#         self.name = name
#         self.roll = roll
#         self.reg = reg
#         self.class_name = class_name
#         print("print from class three\n")
#         print(f"registration submitted\nname : {self.name}\nroll : {self.roll} \nreg : {self.reg}\n")


# s1 = School()

# s1.cls("perry",34)
# s1.cls("zack",23,1234)



# instance variable 
# class School:
#     school_name = "abc school" #class variable\

#     def __init__(self , name): #instance variable
#         self.student_name = name

# sc1 = School("rahim")
# # sc1.school_name = "hello school" #nirdisto object er school name change korar jonno
# School.school_name  = "prigachha jn high school, pirgachha, rangpur" #class er vitorer varibable er nam change korar jonno sob object er jnno projojjo
# print(sc1.school_name)
# print(sc1.student_name)

# sc2 = School("karim")
# print(sc2.school_name)
# print(sc2.student_name)


#class vs instance method
# class Employee:
#     company_name = "google co."
#     def __init__(self, name , salary):
#         self.employee_name = name 
#         self.employee_salary = salary

#     def display_info(self):
#         print(f"employee name : {self.employee_name} \nSalary : {self.employee_salary}")
#         print(self.company_name)
#     @classmethod
#     def change_company_name(cls, name,):
#         cls.company_name = name

# employee1 = Employee("rohim", 3000) 
# employee1.display_info()
# employee1.change_company_name("Microsof co.")
# employee1.display_info()


# emp2 = Employee("Rashed", 135000)
# emp2.company_name = 'amazon co.'
# emp2.display_info()
# employee1.display_info()



# static method in python oop(object oriented programming)
# class School:
#     school_name = "abc school"

#     @staticmethod
#     def calculate_grade(marks): #ai method er jonno kono self keyword lage na , ebong cls keyword o lage na 
#         if (marks>90):
#             return "A+"
#         else:
#             return "Fail"


# print(School.calculate_grade(49))



# getter and setter method 

# class Employee:
#     company_name = "oracle co.."
#     def __init__(self,name, salary):
#         self.name = name
#         # self.salary = salary
#         # self._salary = salary  #private variable
#         self.__salary = salary    #private variable


#     def get_salary(self, password): #getter method
#         if password == "1234abc":
#             print(self.__salary)
#         else:
#             print("invalid password")

#     def set_salary(self,password, new_salary): #setter mathod 
#         if password == "1234abc":
#             self.__salary = new_salary
#             print("successfully changed salary..")
#             print("new salary is ", self.__salary)
#         else:
#             print("worng password")

# emp1 = Employee("Rahim", 350000)
# # print(emp1.company_name, emp1.name, emp1.salary)

# # print(emp1.company_name)
# # print(emp1.name)
# # print(emp1.salary)
# # print(emp1.__salary)
# emp1.get_salary("1234abc")
# emp1.set_salary("1234abc", 150000)

#property decorator
# class Employee:
#     company_name = "MicroSoft Corporation"
#     def __init__ (self, name , salary):
#         self.name = name
#         self.__salary = salary
    
#     # @property
#     # def show_salary(self):
#     #     return self.__salary   
#     @property
#     def salary(self):
#         return self.__salary



# em1 = Employee("Shakib", 212000)
# print(em1.salary)
 



# # Association

# class Laptop:
#     def __init__(self, brand):
#         self.brand = brand

# class Student:
#     def __init__(self, name, laptop_obj):
#         self.name = name
#         self.laptop = laptop_obj

#     def show(self):
#         print(f"{self.name} has a laptop {self.laptop.brand}")  


# lap1 = Laptop("Aorus Pro")

# Student1 = Student("rashed", lap1)
# Student1.show()


# # aggregetion in python 
# class Department:
#     def __init__(self, name):
#         self.name = name


# class University:
#     def __init__(self , name):
#         self.name = name
#         self.departments = []
#     def add_department (self, department):
#         self.departments.append(department)


#     def show_department(self):
#          print([x.name for x in self.departments])
    
# University1 = University("Oxford University")
# dept1 = Department("CSE")
# dept2 = Department("EEE")
# dept3 = Department("SWE")

# University1.show_department()
# University1.add_department(dept1)
# University1.show_department()
# University1.add_department(dept2)
# University1.show_department()
# University1.add_department(dept3)
# University1.show_department()



#composition relationship in python 

# class Engine:
#     def __init__(self, power):
#         self.power = power





# class Car:
#     def __init__ (self, brand, power):
#         self.brand = brand
#         self.Engine = Engine(power)

#     def show_info(self):
#         print(f"{self.brand} engine power : {self.Engine.power}HP")


# car1 = Car("Toyota", 300)
# car1.show_info()
# car2 = Car("BMW", 430)
# car2.show_info()






# ___________________practice real world problem _____________________________

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