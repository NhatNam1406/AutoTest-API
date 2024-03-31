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

url = Variable.host + Variable.endpoint_companytype
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
   "ucid":"{{ucid}}"
     }
######################################################
variables = {}
variables["WorkNo"] =Function.generate_random_string()
variables["ucid"] =Function.generate_random_string()
updated_data = Function.replace_placeholders(data, variables)
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