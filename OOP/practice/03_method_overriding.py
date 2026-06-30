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
