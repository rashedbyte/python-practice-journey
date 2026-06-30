# # real world problem solving

# # problem no 01 (Vehicle and car heritage)

# # class Vehicle:
# #     def __init__(self,brand):
# #         self.brand = brand
        
# #     def start(self):
# #         print(f"{self.brand} is starting now!")
        
        
# # class Car(Vehicle):
# #     pass


# # car1 = Car("Toyota")

# # car1.start()


# # class Vehicle:
# #     def __init__(self, brand):
# #         self.brand = brand
        



# # ral world problem no 02 -- super vehicle architecture , topic : inheritance with super() method 

# # way 01 (short code)
# # class Car(Vehicle):
# #     def __init__(self, brand, doors):
# #         super().__init__(brand)
# #         # self.brand = brand  _____> ai jayga ta bujlam na , ami jodi aikhane ai vabe likhtam taw to hoito tahole amr oi clas ta ke inherit korar dorkar ki chilo ? 
# #         self.doors =doors
        
        
# #     def show_details (self):
# #         print(f"This {self.brand} Car has {self.doors} doors.")
        
# # car = Car("BMW X7", 4)
# # car.show_details()

# # way 02 long code wrong way with out inheritance
# # class Car: 
# #     def __init__(self,brand, model, year, price, fuel_type, doors):
# #         self.brand = brand
# #         self.model = model
# #         self.year = year
# #         self.price = price
# #         self.fuel_type = fuel_type 
# #         self.doors = doors
# #         print(f"Car : {self.brand} {self.model} has {self.doors} doors, Established year : {self.year}, Fuel type : {self.fuel_type}, price : {self.price}   ")
        


# # class Bike: 
# #     def __init__(self,brand, model, year, price, fuel_type, engine_cc):
# #         self.brand = brand 
# #         self.model = model 
# #         self.price = price
# #         self.year = year
# #         self.fuel_type = fuel_type
# #         self.engine_cc = engine_cc
# #         print(f"Bike : {self.brand} {self.model} a {self.engine_cc}CC, Established year : {self.year}, Fuel type : {self.fuel_type}, price : {self.price}   ")
        
        
        
# # class Truck: 
# #     def __init__(self,brand, model, year, price, fuel_type, cargo_capacity):
# #         self.brand = brand 
# #         self.model = model
# #         self.price = price
# #         self.year = year
# #         self.fuel_type = fuel_type
# #         self.cargo_capacity = cargo_capacity
# #         print(f"Truck : {self.brand} {self.model} has {self.cargo_capacity} Cargo Capacity, Established year : {self.year}, Fuel type : {self.fuel_type}, price : {self.price}   ")
        

# # car = Car("mercedes","SUV",1998,"$2.5M","Diesel",5 )
# # bike = Bike("Suzuki" , "gikser SF", 2000, "$50K", "octane", 220)
# # truck = Truck("Sonalika", "LSV 023", 2009, "$200K", "Diesel", 400)



# # way 03 easy way with using inheritance

# class Vehicle:
#     def __init__(self, brand, model, year, price, fuel_type):
#         self.brand = brand
#         self.model = model
#         self.year = year 
#         self.price = price
#         self.fuel_type = fuel_type


# class Car(Vehicle):
#     def __init__(self, brand,model,year, price , fuel_type, doors):
#         super().__init__(brand, model, year, price, fuel_type)
#         self.doors = doors
#         print(f"{self.brand} {self.model} is {self.doors}doors, established year : {self.year}, price {self.price}, fuel type : {self.fuel_type}")
        
# class Bike(Vehicle): 
#     def __init__(self, brand, model, year, price, fuel_type,engine_cc):
#         super().__init__(brand, model, year, price, fuel_type)
#         self.engine_cc = engine_cc
#         print(f"{self.brand} {self.model} is {self.engine_cc}CC, established year : {self.year}, price {self.price}, fuel type : {self.fuel_type}")

# class Truck(Vehicle): 
#     def __init__(self, brand, model, year, price, fuel_type,cc):
#         super().__init__(brand, model, year, price, fuel_type)
#         self.cc = cc
#         print(f"{self.brand} {self.model} is {self.cc}Cargo Capacity, established year : {self.year}, price {self.price}, fuel type : {self.fuel_type}")
        
        
        
# car = Car("mercedes","SUV",1998,"$2.5M","Diesel",5 )
# bike = Bike("Suzuki" , "gikser SF", 2000, "$50K", "octane", 220)
# truck = Truck("Sonalika", "LSV 023", 2009, "$200K", "Diesel", 400)


# # ==============================================================================
# # Topic: Challenge Chapter 9 - Smart Banking System (Method Overriding)
# # Objective: Creating a banking system where Premium Accounts charge an extra 
# # processing fee using super() without duplicating parent core transaction steps.
# # ==============================================================================

# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.balance = balance 
#         self.account_holder = account_holder
        
#     def transfer_money(self, amount):
#         # Good Practice: Using 'amount' directly without binding it to 'self'
#         print("Step 01: Verifying account security and biometric data...")
#         print(f"Step 02: {self.account_holder} transferred ${amount} successfully!")
        
# print("_________________________________")

# class PremiumAccount(BankAccount):
#     # Since PremiumAccount uses the exact same input data, 
#     # we don't need to define a separate __init__ constructor here.
    
#     def transfer_money(self, amount):
#         # Calling parent method to execute Step 1 and Step 2 dynamically
#         super().transfer_money(amount)
#         print("Step 03: Charging an extra $5 Premium Lounge Processing Fee.")

        
# print("Processing Start...")
# pre_acc = PremiumAccount('Mr. Ali', 23000)
# pre_acc.transfer_money(3400)



