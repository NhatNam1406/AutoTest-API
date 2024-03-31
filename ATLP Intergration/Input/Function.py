import string
import random
from datetime import date, datetime, timedelta

##################################################
# Function to replace the variable in data body
def replace_placeholders(data, variables):
    if isinstance(data, str):
        # Replace placeholders in string
        for key, value in variables.items():
            data = data.replace("{{" + key + "}}", value)
        return data
    elif isinstance(data, list):
        # Replace placeholders in list elements
        return [replace_placeholders(item, variables) for item in data]
    elif isinstance(data, dict):
        # Replace placeholders in dictionary values
        return {key: replace_placeholders(value, variables) for key, value in data.items()}
    else:
        return data
###################################################
def generate_random_string():
    letters_and_digits = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(10))        

###################################################
def generate_container_number():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=7))
    return f"{letters}U{numbers}"
###################################################
def generate_multiple_container(n):
    container_numbers = [generate_container_number() for _ in range(n)]
    return container_numbers

###################################################
def generate_future_date(days=1):
    today = datetime.now().date()
    future_date = today + timedelta(days=days)
    return future_date.strftime('%Y-%m-%d')
 ############################################################
def update_dict(*args):
    merged_dict = {}
    for dictionary in args:
        merged_dict.update(dictionary)
    return merged_dict
########################################################
def increment_placeholders(dictionary, i):
    updated_dict = dictionary.copy()
    for key, value in updated_dict.items():
        if isinstance(value, str) and '[' in value and ']' in value:
            updated_dict[key] = value.replace('[i]', f'[{i}]')
    return updated_dict
########################################################
def generate_variables_LCL(n):
    # Generate Qty, Wgt, and Cbm for each element satisfying the conditions
    Qty = [random.randint(1, 10) for _ in range(n)]
    Wgt = [random.randint(1000, 5000) for _ in range(n)]
    Cbm = [random.randint(1, 10) for _ in range(n)]

    # Calculate TotalQty, TotalWgt, TotalCbm
    TotalQty = sum(Qty)
    TotalWgt = sum(Wgt)
    TotalCbm = sum(Cbm)

    # Convert values to strings and enclose in double quotes
    return TotalQty, TotalWgt, TotalCbm, Qty, Wgt, Cbm
##########################################################
def generate_variables_FCL(n):
    Qty = [random.randint(1, 10) for _ in range(n)]
    Wgt = [random.randint(1000, 5000) for _ in range(n)]
    Cbm = [random.randint(1, 10) for _ in range(n)]

    TotalQty = sum(Qty)
    TotalWgt = sum(Wgt)
    TotalCbm = sum(Cbm)

    return Qty, Wgt, Cbm, TotalQty,TotalWgt,TotalCbm
##########################################################
def generate_random_9_digit_number():
    return ''.join(random.choices('0123456789', k=9))
##########################################################
def generate_random_7_digit_number():
    return ''.join(random.choices('0123456789', k=7))
##########################################################
def generate_random_future_date():
    # Get today's date
    today = datetime.today()   
    # Generate a random number of days between 1 and 14
    random_days = random.randint(1, 14) 
    # Calculate the future date by adding random_days to today's date
    future_date = today + timedelta(days=random_days)   
    # Format the future date as 'YYYY-MM-DD'
    future_date_formatted = future_date.strftime('%Y-%m-%d')
    return future_date_formatted
##########################################################
def generate_random_truck_number():
    # Define the format of the truck number (e.g., AAA 1234)
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=4))
    truck_number = f"{letters} {numbers}"
    return truck_number
#########################################################
def generate_random_phone_number():
    # Generate a random phone number with format (XXX) XXX-XXXX
    area_code = random.randint(100, 999)
    first_part = random.randint(100, 999)
    second_part = random.randint(1000, 9999)
    phone_number = f"({area_code}) {first_part}-{second_part}"
    return phone_number
#########################################################
# Function find Invoice No in Message response, the value retunr is a list
def find_unique_invoice_numbers(response_data):
    unique_invoice_numbers = set()
    def find_invoice_numbers(data):
        for key, value in data.items():
            if key == "invoiceNo":
                unique_invoice_numbers.add(value)
            elif isinstance(value, dict):
                find_invoice_numbers(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        find_invoice_numbers(item)
    find_invoice_numbers(response_data)
    return unique_invoice_numbers
##########################################################
# Function find amount in Message response, the value return is total amount
def calculate_total_amount(response_data):
    service_charge_list = response_data.get("result", {}).get("serviceChargeList", [])
    total_amount = 0
    for charge in service_charge_list:
        total_amount += float(charge.get("amount", 0))
    return total_amount
###########################################################
def get_random_future_date():
    # Get today's date
    today = date.today()

    # Generate a random number of days between 1 and 7
    random_days = random.randint(1, 7)

    # Calculate the future date
    future_date = today + timedelta(days=random_days)

    # Set the time to 09:30:00
    future_time = datetime.combine(future_date, datetime.min.time())

    # Format the future datetime as a string
    formatted_datetime = future_time.strftime("%Y-%m-%dT%H:%M:%S")
    
    return formatted_datetime