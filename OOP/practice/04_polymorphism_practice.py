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


# APPROACH 03: WITH OUT POLYMORPHISM (BAD PRACTICE) 
# File system (file type export)

class PDFExporter:
    def convert_to_pdf(self , data):
        print(f"[PDF] Converting data to PDF format. Content : '{data}'")
        
        
class ExcelExporter:
    def convert_to_excel(self, data):
        print(f"[Excel] Converting data to Excel Rows/columns. content: '{data}'")

x = ExcelExporter().convert_to_excel("excel")        
        
def download_button(exporter_object, data, file_type="excel"):
    if file_type.lower() == "pdf":
        exporter_object.convert_to_pdf(data)
    elif file_type.lower() == "excel":
        exporter_object.convert_to_excel(data)
        
        
file1_data = "this is a python program to practicing python oop polymorphism concept."
file1 = PDFExporter()
download_button(file1, file1_data, "pdf")

print("_____________________________\n")

file2_data = "this is our daily costing sheets"
file2 = ExcelExporter()
download_button(file2, file2_data)
        
        


# APPROACH 4 : WITH POLYMORPHISM  (good practice)
# (File exporting system)

class PDFExporter:
    def convert_file(self, data):
        print(f"[PDF] converting data to PDF format, content: {data} ")
        
class ExcelExporter:
    def convert_file(self, data):
        print(f"[Excel] converting data format to row/columns. content: {data}")        
        
class CSVExporter:
    def convert_file(self,data):
        print(f"[CSV] converting data format to comma separated value pairs. content: {data}")
        


def download_button(file_object, data):
    file_object.convert_file(data)
    print("data processing completed")
    

file1 = "this is a pdf file"
file1_obj = PDFExporter()
download_button(file1_obj,file1)

file2 = "this is an excel file"
file2_obj = ExcelExporter()
download_button(file2_obj,file2)

file3 = "this is a csv file"
file3_obj = CSVExporter()
download_button(file3_obj, file3)


