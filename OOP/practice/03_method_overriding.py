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