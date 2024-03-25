import string
import random
from datetime import datetime, timedelta

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
def generate_future_date(days=1):
    today = datetime.now().date()
    future_date = today + timedelta(days=days)
    return future_date.strftime('%Y-%m-%d')
###################################################
def generate_variables():
    # Generate Qty1 and Qty2 satisfying the conditions
    Qty2 = random.randint(1, 10)
    Qty1 = random.randint(1, min(20, 2 * Qty2))
    
    # Generate Wgt1 and Wgt2 satisfying the conditions
    Wgt2 = random.randint(1000, 5000)
    Wgt1 = random.randint(1, min(10000, 2 * Wgt2))
    
    # Generate Cbm1 and Cbm2 satisfying the conditions
    Cbm2 = random.randint(1, 10)
    Cbm1 = random.randint(1, min(20, 2 * Cbm2))

    # Calculate TotalQty, TotalWgt, TotalCbm
    TotalQty = Qty1 + Qty2
    TotalWgt = Wgt1 + Wgt2
    TotalCbm = Cbm1 + Cbm2

    # Convert values to strings and enclose in double quotes
    return TotalQty,TotalWgt,TotalCbm,Qty1,Wgt1,Cbm1,Qty2,Wgt2,Cbm2
    