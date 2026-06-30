# ==============================================================================
# Topic: Method Overriding in Python OOP
# Practiced and Researched using Python Documentation, W3Schools, and GeeksforGeeks.
# ==============================================================================

# ------------------------------------------------------------------------------
# APPROACH 1: Bad Practice (Without Method Overriding)
# Problem: If we use different method names, the parent 'Bank' class becomes useless 
# and inheritance loses its true purpose.
# ------------------------------------------------------------------------------
class Bank:
    def calculate_interest(self):
        print("Default interest rate is 5%")
        
class SonaliBank(Bank):
    def sonali_bank_interest(self):
        print("Sonali Bank interest rate is 7%")

class BracBank(Bank):
    def brac_interest(self):
        print("Brac Bank interest rate is 9%")
        
s_bank = SonaliBank()
b_bank = BracBank()

# Calling completely different method names
s_bank.sonali_bank_interest()
b_bank.brac_interest()


# ------------------------------------------------------------------------------
# APPROACH 2: Best Practice (With Method Overriding)
# Solution: Keeping the exact same method name 'calculate_interest' across all 
# child classes. This enforces a standard across the entire system.
# ------------------------------------------------------------------------------
class Bank:
    def __init__(self):
        pass
    
    def calculate_interest(self):
        print("Default interest rate is 7%")
        
class SonaliBank(Bank):
    def __init__(self):
        pass
        
    # Overriding the parent method with the exact same name
    def calculate_interest(self):
        print("Sonali Bank interest rate is 10%")
        
class RupaliBank(Bank):
    def __init__(self):
        pass
    
    def calculate_interest(self):
        print("Rupali Bank interest rate is: 12%")
        
class IslamiBank(Bank):
    def __init__(self):
        pass
    
    def calculate_interest(self):
        print("Islami Bank interest rate is: 5%")


# Creating objects and calling the overridden methods directly
SonaliBank().calculate_interest()
RupaliBank().calculate_interest()
IslamiBank().calculate_interest()


# ------------------------------------------------------------------------------
# Concept Summary (Answering Gemini's Quiz):
# Method Overriding requires the exact same method name in both Parent and Child classes. 
# If the name is different, it becomes a new separate method, not overriding. 
# Overriding means replacing the parent's behavior while keeping the signature identical.
# ==============================================================================



# ==============================================================================
# Topic: Quiz Reflection - Method Overriding Proof of Concept
# Objective: Proving that Python executes the overridden child method instead 
# of the parent method when called from a child object.
# ==============================================================================

class Vehicle:
    def __init__(self):
        pass
        
    def fuel_type(self):
        print("Printed from Vehicle class")
        
class ElectricCar(Vehicle):
    def __init__(self):
        pass
        
    # Successfully overriding the parent method with the exact same name
    def fuel_type(self):
        print("Printed from ElectricCar class")
    
# Creating the child object and calling the method instantly in one line
car1 = ElectricCar().fuel_type()

# Output: Printed from ElectricCar class
# ==============================================================================




# ==============================================================================
# topic : quiz reflection - method overriding parent method and child method using super().
# Objective : learning super() method to use child class a  parent method and also child method.
# ==============================================================================


class Hero:
    def __init__(self):
        pass
    
    def attack(self): # hero's normal power method
        print("Normal Punch ! ")
        
class SuperHero(Hero):
    def __init__(self):
        pass
    
    def attack(self):
        super().attack() #successfully overriding with super() method
        print("Laser Beam !") # hero's extra power
        

# create push_punch object 
PushPunch = SuperHero()
# attack
PushPunch.attack()



# Approach 1: without super() method , worst case

class GameCharacter: 
    def __init__(self):
        pass
    
    def login(self):
        print("1. checking sever connection....")
        print("2. Loading player data and inventory....")
        print("3. Rendering 3D character model....")
        
class Warrior(GameCharacter):
    def __init__(self):
        pass
    
    def login(self):
        # parent line
        print("1. checking sever connection....")
        print("2. Loading player data and inventory....")
        print("3. Rendering 3D character model....")
        # child extra line 
        print("4. Warrior : equip heavy sword and iron shield.")
        
class Mage(GameCharacter):
    def __init__(self):
        pass
    
    def login(self):
        print("1. checking sever connection....")
        print("2. Loading player data and inventory....")
        print("3. Rendering 3D character model....")
        
        # child extra line  
        print("4. Mage : equip magical staff and mana potions.")
        


warrior_p = Warrior().login()
mage_p = Mage().login()

# when i write every login def function with 3 parents print line , then we don't need parent class because parent class is not need for this type of problem.


# APPROaCH 2 : using super() method , this is good practice for this type of problem 

class GameCharacter:
    def __init__(self):
        pass
    def login(self):
        print("1. Checking server connection...")
        print("2. Loading player data and inventory...")
        print("3. Rendering 3D character model...")
        
        
class Mage(GameCharacter):
    def __inti__(self):
        pass
    
    def login(self):
        super().login()
        print("4. Mage : equip magical staff and mana potions.")
        
class Warrior(GameCharacter):
    def __init__(self):
        pass
    
    def login(self):
        super().login()
        print("4. Warrior : equip heavy sword and iron shield.")
        
        
warrior_player = Warrior().login()
mage_player = Mage().login()

