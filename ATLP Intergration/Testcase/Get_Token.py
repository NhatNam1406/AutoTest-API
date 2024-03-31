import requests
import sys
import time
sys.path.append(r'C:\Users\nhatn\Downloads\Python\KPCFS-AutoTest\ATLP Intergration\Input')
import Variable

url = Variable.host + Variable.endpoint_token
print("URL is: ",url,'\n')
# Make a POST request with the data

response = requests.post(url)

def get_access_token():
    response = requests.post(url)
    if response.status_code == 200:
        token = response.json().get("access_token")
        return token
    else:
        print("Failed to get access token:", response.text)
        return None
######################################    
start_time = time.time()
Token = get_access_token()
end_time = time.time()
elapsed_time = end_time - start_time
######################################
if Token:
    print("Access token:", Token)
    print(f"Time consumed  {elapsed_time:.2f} seconds","\n")
else:
    print("Failed to get access token.")




