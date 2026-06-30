# APPROACH 01: without Polymorphism (Bad and Hard to maintain)
class BkashPayment:
    def pay_with_bkash(self, amount):
        print(f"[Bkash] Processing payment of ${amount} via OTP and PIN")


class RocketPayment:
    def pay_with_rocket(self, amount):
        print(f"[Rocket] Processing payment of ${amount} via DBBL Token.")


class NagodPayment:
    def pay_with_nagod(self, amount):
        print(f"[Nagod] Processing payment of ${amount} via OTP and PIN")
        
        

def checkout_manager(payment_object, amount, payment_type):
    if payment_type == "bkash":
        payment_object.pay_with_bkash(amount)  # diff name 01
    elif payment_type == "nagod":
        payment_object.pay_with_nagod(amount)
    elif payment_type == "rocket":
        payment_object.pay_with_rocket(amount)
        
        
user1 = BkashPayment()
checkout_manager(user1, 500, "bkash")

user2 = RocketPayment()
checkout_manager(user2, 300, "rocket")

user3 = NagodPayment()
checkout_manager(user3, 800, "nagod")



# APPROACH 02 : WITH POLYMORPHISM (GOOD AND BEST FOR MAINTAIN)

class BkashPayment:
    def payment_process(self, amount):
        print(f"[bkash] processing payment ${amount} via OTP and PIN")
        
class NagodPayment:
    def payment_process(self, amount):
        print(f"[Nagod] processing payment ${amount} via OTP and PIN")
        
class RocketPayment:
    def payment_process(self, amount):
        print(f"[Rocket] processing payment ${amount} via PIN and biometric.")
        

def manager_checkout(payment_object, amount):
    payment_object.payment_process(amount)
    
    
bkash_user = BkashPayment()
manager_checkout(bkash_user, 300)

rocket_user = RocketPayment()
manager_checkout(rocket_user, 900)