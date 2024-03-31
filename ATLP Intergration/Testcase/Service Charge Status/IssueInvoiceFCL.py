import requests
import random
import sys
import json
from datetime import datetime, timedelta
import time
sys.path.append(r'C:\Users\nhatn\Downloads\Python\KPCFS-AutoTest\ATLP Intergration\Input')
import Variable
import Function
sys.path.append(r'C:\Users\nhatn\Downloads\Python\KPCFS-AutoTest\ATLP Intergration\Testcase')
import Get_Token
sys.path.append(r'C:\Users\nhatn\Downloads\Python\KPCFS-AutoTest\ATLP Intergration\Data')
import Data
import Record

url = Variable.host + Variable.endpoint_service_charges_status
############################################# HEADER ##########################################
token=Get_Token.Token
headers = {
    "Authorization": token,
    "Content-Type": "application/json",
    "host": "localhost:8081",
    "accept-encoding": "gzip, deflate, br",
    "connection": "keep-alive"
}
############################################# MESSAGE BODY ################################################
#####################################################
data={
     "atlpSubmissionID": str(Function.generate_random_9_digit_number()),
     "jobType": "IFCL_STRG",
     "jobOrderNumber": "{{WorkNo}}",
     "invoiceNo": "{{Draftinvoice}}",
     "paymentStatus":"Issued"
     }
######################################################
PaymentDetails={
    "referenceNumber": str(Function.generate_random_7_digit_number()),
    "totalAmount": "{{Totalamt}}",
    "receiptNumber": str(Function.generate_random_7_digit_number()),
    "bankName": "ViettinBank",
    "requestedUser": "Super User",
    "referenceDate": "{{FutureDate}}",
    "paymentMethod": "{{PaymentMD}}"
}
#######################################################
# Structure the format of schema
result = {"paymentDetails": PaymentDetails}
data.update(result)
#######################################################
# Input data into schema
variables = {}
variables["WorkNo"] = Record.Save_WorkNo_FCL
variables["Draftinvoice"] =Record.Save_DraftInv_FCL
variables["Totalamt"] =Record.Save_Totalamount_FCL
variables["FutureDate"] = str(Function.get_random_future_date())
variables["PaymentMD"] = random.choice(Variable.Paymentmethod)
updated_data = Function.replace_placeholders(data, variables)

A =json.dumps(updated_data, indent=4)
print(A)

response = requests.post(url, headers=headers, json=updated_data)
if response.status_code == 200:
    response_data =json.loads(response.text)
    if(response_data.get("code")=="1"):
       print("POST request successful!")
       print(json.dumps(response_data, indent=2))
    else:
        print("POST request not successful")
        print(json.dumps(response_data, indent=2))
else:
    print("POST request failed with status code:", response.status_code)
    print("Response content:", response.text)






