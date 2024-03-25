import requests
import sys
import json
from datetime import datetime, timedelta
import time
sys.path.append(r'C:\Users\TSB\Downloads\API-AutoTest-WorkSpace\ATLP Intergration\Input')
import Variable
import Function
sys.path.append(r'C:\Users\TSB\Downloads\API-AutoTest-WorkSpace\ATLP Intergration\Testcase')
import Get_Token

url = Variable.host + Variable.endpoint_servicerequest
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
data = {
    "atlpSubmissionID": "{{WorkNo}}",
    "agentInfo":
      {
    "name": "{{PTNRNAME}}",
    "code": "{{PTNRCODE}}",
    "ucid": "{{UCID}}"
      },

    "serviceRequest":
      {
    "requestType": "DESTUFF",
    "jobType": "IFCL_STRG",
    "jobOrderNumber": "{{WorkNo}}",
    "requestUser": "ATLP",
    "directDelivery": "No",
    "partialCheck": "No",
    "expressDelivery": "No",    
    "jobRecap ": 
       {
    "containerCount": "20FT:0,40FT:2,OTH:0",
    "surveyancePOC": "",
    "surveyancePOCContactNo": "",
    "customerPOC": "",
    "customerPOCContactNo": "",
    "remarkstoCFS": "2 Container 40ft "
       },
    "shipmentDetails": 
       {   
    "mblNumber": "{{MBL}}",
    "doRefNo": "376435376",
    "vesselIMO": "R75437",
    "voyageNo": "NICK",
    "callSign": "12341234",
    "vesselCode": "NICK",
    "vesselName": "NICK",
    "rotationNo": "UEA",
    "pickupTerminal": "AEKHL",
    "eta": "2023-04-23T13:50:00"
      },
    "containers": [
      {
        "iso": "45G0",
        "containerNo": "{{CNTR1}}",
        "operator": "RHS",
        "returnTerminal": "AEKHL",
        "expiryDate": "{{ExpiryDate}}",
        "requestedDate": "{{RequestDate}}",
        "timeSlotNo": "{{Timeslot}}"
      },
	  {
        "iso": "45G0",
        "containerNo": "{{CNTR2}}",
        "operator": "RHS",
        "returnTerminal": "AEKHL",
        "expiryDate": "{{ExpiryDate}}",
        "requestedDate": "{{RequestDate}}",
        "timeSlotNo": "{{Timeslot}}"
      } ],
    "manifestDetails": {
      "items": [
        {
          "type": "IFCL",
          "mblNumber": "{{MBL}}",
          "containerNo": "{{CNTR1}}",
          "sealNo": "6536767",
          "iso": "45G0",
          "cargoTypeDesc": "GP",
          "consigneeName": "Consignee Name",
          "consigneeEmail": "Consignee Email",
          "consigneePhone": "Consignee Phone",
          "quantity": "50",
          "totalWeight": "10000",
          "totalVolume": "25",
          "loadPort": "AEJEA",
          "shipper": "optional free text",
          "notifyParty": "optional",
          "packageTypeCommodity": "BOX",
          "packageTypeCommodityDesc": "BOX",
          "hazardous": "No",
          "reeferTemperature": "",
          "heightCm": "",
          "foreCm": "",
          "afterCm": "",
          "houseBLs": [
            {
              "hblNumber": "{{HBL1}}",
              "childId": "{{HBL1}}",
              "parentId": "{{CNTR1}}",
              "cargoTypeDesc": "GP",
              "shipper": "",
              "notifyParty": "",
              "consigneeName": "Consignee Name",
              "consigneeEmail": "Consignee Email",
              "consigneePhone": "Consignee Phone",
              "quantity": "50",
              "marks": "marks",
              "cargoDesc": "50 boxes",
              "cargoCodeDesc": "C20",
              "cargoCodeDescName": "CFS / Containerized Cargo",
              "hazardIMOClass": "",
              "totalWeight": "10000",
              "totalVolume": "25",
              "loadPort": "AEJEA",
              "lengthm": "",
              "widthm": "",
              "heightm": "",
              "packageTypeCommodity": "BOX",
              "packageTypeCommodityDesc": "BOX",
              "hazardous": "No",
              "hazardousDetails": [
              ],
              "reeferTemperature": "",
              "heightCm": "",
              "foreCm": "",
              "afterCm": ""
            }
          ]
        },
		{
          "type": "IFCL",
          "mblNumber": "{{MBL}}",
          "containerNo": "{{CNTR2}}",
          "sealNo": "6536767",
          "iso": "45G0",
          "cargoTypeDesc": "GP",
          "consigneeName": "Consignee Name",
          "consigneeEmail": "Consignee Email",
          "consigneePhone": "Consignee Phone",
          "quantity": "50",
          "totalWeight": "10000",
          "totalVolume": "25",
          "loadPort": "AEJEA",
          "shipper": "optional free text",
          "notifyParty": "optional",
          "packageTypeCommodity": "BOX",
          "packageTypeCommodityDesc": "BOX",
          "hazardous": "No",
          "reeferTemperature": "",
          "heightCm": "",
          "foreCm": "",
          "afterCm": "",
          "houseBLs": [
            {
              "hblNumber": "{{HBL2}}",
              "childId": "{{HBL2}}",
              "parentId": "{{CNTR2}}",
              "cargoTypeDesc": "GP",
              "shipper": "",
              "notifyParty": "",
              "consigneeName": "Consignee Name",
              "consigneeEmail": "Consignee Email",
              "consigneePhone": "Consignee Phone",
              "quantity": "50",
              "marks": "marks",
              "cargoDesc": "50 boxes",
              "cargoCodeDesc": "C20",
              "cargoCodeDescName": "CFS / Containerized  Cargo",
              "hazardIMOClass": "3",
              "totalWeight": "10000",
              "totalVolume": "25",
              "loadPort": "AEJEA",
              "lengthm": "",
              "widthm": "",
              "heightm": "",
              "packageTypeCommodity": "BOX",
              "packageTypeCommodityDesc": "BOX",
              "hazardous": "No",
              "hazardousDetails": [
              ],
              "reeferTemperature": "",
              "heightCm": "",
              "foreCm": "",
              "afterCm": ""
            }
          ]
        }
      ]
    },
    "documentList": [
      {
        "fileName": "{{RandomDoc}}.pdf",
        "documentType": "MBL",
        "documentDescription": "{{remark}}",
        "docUrl": "ducumenturl"
      } 
    ]
}
}
############################################################################################################
variables = {
    "WorkNo": "",
    "PTNRNAME": "MICC",
    "PTNRCODE": "MICC",
    "HBL1":"",
    "HBL2":"",
    "UCID": "000084",
    "MBL": "",
    "CNTR1": "",
    "CNTR2": "",
    "ExpiryDate":"",
    "RequestDate":"",
    "Timeslot":"1",
    "RandomDoc": "",
    "remark": ""
}
WorkNo=variables["WorkNo"] = Function.generate_random_string()
variables["HBL1"] = Function.generate_random_string()
variables["HBL2"] = Function.generate_random_string()
MBLNo=variables["MBL"] = Function.generate_random_string()
variables["CNTR1"] = Function.generate_container_number()
variables["CNTR2"] = Function.generate_container_number()
variables["RandomDoc"] = Function.generate_random_string()
variables["remark"] = "This is the Remark"
FutureDate = variables["RequestDate"] = Function.generate_future_date(days=7)
FutureDatePlus=datetime.strptime(FutureDate, '%Y-%m-%d') + timedelta(days=3)
ExpiryDate=FutureDatePlus.strftime('%Y-%m-%dT00:00:00')
variables["ExpiryDate"]=ExpiryDate
updated_data = Function.replace_placeholders(data, variables)


# Make a POST request with the data
print(url,'\n')
response = requests.post(url, headers=headers, json=updated_data)


if response.status_code == 200:
    response_data =json.loads(response.text)
    if(response_data.get("code")=="1"):
       print("POST request successful!",'\n')
       print("Response content with Work No: ",WorkNo,"and M.BL is: ",MBLNo)
       print(json.dumps(response_data, indent=2))
    else:
        print("POST request not successful")
        print(json.dumps(response_data, indent=2))
else:
    print("POST request failed with status code:", response.status_code)
    print("Response content:", response.text)

