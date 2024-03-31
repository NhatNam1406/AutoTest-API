import requests
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

url = Variable.host + Variable.endpoint_cntr_appoinments
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
   "atlpSubmissionID": "{{WorkNo}}",
     }
######################################################
Appoinment={
    "requestType": "TRUCK_APPT",
    "jobType": "{{CntrStatus}}",
    "appointmentNumber": "{{appointmentNumber}}",
    "appointmentStatus": "CheckedIN",
    "refJobOrderNumber": "{{WorkNo}}",
    "appointmentDate": "{{Futureday}}",
    "timeSlotNo": "{{timeSlotNo}}",
    "truckNo": "{{TruckNo}}",
    "driverID": "{{driverID}}",
    "driverMobile": "{{driverMobile}}",
    "truckType": "{{Trucktype}}",
    "truckTypeDesc": "{{TruckName}}",
    "companyCode": "Teo",
    "remark": "{{Remark}}"
          }
Container={
        "containerNo": "{{Container[i]}}",
        "weight": "10000",
        "iso": "{{Sztp}}",
        "operator": "RHS"
         }
#####################################################
variables = {}
variables["CntrStatus"] = 'CNTR_IN' # or 'CNTR_OUT'
variables["appointmentNumber"] =Function.generate_random_9_digit_number()
variables["WorkNo"] =Record.Save_WorkNo_FCL
variables["Futureday"] =Function.generate_random_future_date()
variables["timeSlotNo"] = str(2)
variables["TruckNo"] = Function.generate_random_truck_number()
variables["driverID"] = Function.generate_random_7_digit_number()
variables["driverMobile"] = Function.generate_random_phone_number()
variables["Trucktype"] = Data.GNRL_CODE
variables["TruckName"] = Data.GNRL_NM
variables["Remark"] = "Welcome API"
variables["Sztp"] = "45G0"
#######################################################
n=Record.Save_No_Cntr_FCL # Number of container
ContainerList = []
for i in range(1, n + 1):
    container = Container.copy()  # Create a new dictionary object for each container
    container["containerNo"] = Record.Save_HBL_FCL[f"ContainerNo[{i}]"]
    ContainerList.append(container)

# Replace the placeholder with actual container numbers
for container in ContainerList:
    container["containerNo"] = container["containerNo"].replace("{{container}}", container["containerNo"])
result  = {"containers": ContainerList}
Appoinment.update(result)
result1 = {"appointmentDetails": Appoinment}
data.update(result1)
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

