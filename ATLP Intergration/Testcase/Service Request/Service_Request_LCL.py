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
#####################################################
data={
   "atlpSubmissionID": "{{WorkNo}}"
     }
#####################################################
Agentinfo={    
"agentInfo":
      {
    "name": "{{PTNRNAME}}",
    "code": "{{PTNRCODE}}",
    "ucid": "{{UCID}}"
      }
}
#####################################################
ServiceRequest ={
    "requestType": "DESTUFF",
    "jobType": "ILCL_STRG",
    "jobOrderNumber": "{{WorkNo}}",
    "requestUser": "ATLP",
    "directDelivery": "{{DirectDelivery}}",
    "partialCheck": "{{PartialCheck}}",
    "expressDelivery": "No"  
               }
#####################################################
Jobrecap={
        "jobRecap ": 
        {
    "containerCount": "20FT:0,40FT:2,OTH:0",
    "surveyancePOC": "",
    "surveyancePOCContactNo": "",
    "customerPOC": "",
    "customerPOCContactNo": "",
    "remarkstoCFS": "2 Container 40ft "
       }
}
######################################################
ShipmentDetail={
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
      }
}
######################################################
Container={
        "containers": [
        {
        "iso": "{{Sztp}}",
        "containerNo": "{{CNTR}}",
        "operator": "RHS",
        "returnTerminal": "AEKHL",
        "expiryDate": "{{ExpiryDate}}",
        "requestedDate": "{{RequestDate}}",
        "timeSlotNo": "{{Timeslot}}"
        }
                     ] 
}
#####################################################
Items={
          "type": "{{Worktype}}",
          "mblNumber": "{{MBL}}",
          "containerNo": "{{CNTR}}",
          "sealNo": "6536767",
          "iso": "{{Sztp}}",
          "cargoTypeDesc": "{{Cargotype}}",
          "consigneeName": "Consignee Name",
          "consigneeEmail": "Consignee Email",
          "consigneePhone": "Consignee Phone",
          "quantity": "{{TotalQty}}",
          "totalWeight": "{{TotalWgt}}",
          "totalVolume": "{{TotalCbm}}",
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
}
###################################################
houseBLs={
              "hblNumber": "{{HBL[i]}}",
              "childId": "{{HBL[i]}}",
              "parentId": "{{CNTR}}",
              "cargoTypeDesc": "{{Cargotype[i]}}",
              "shipper": "",
              "notifyParty": "",
              "consigneeName": "Consignee Name",
              "consigneeEmail": "Consignee Email",
              "consigneePhone": "Consignee Phone",
              "quantity": "{{Qty[i]}}",
              "marks": "marks",
              "cargoDesc": "50 boxes",
              "cargoCodeDesc": "{{CargoCode[i]}}",
              "cargoCodeDescName": "CFS / Containerized Cargo",
              "hazardIMOClass": "",
              "totalWeight": "{{Wgt[i]}}",
              "totalVolume": "{{Cbm[i]}}",
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
#################################################
DocumentList={
        "documentList": [
      {
        "fileName": "{{RandomDoc}}.pdf",
        "documentType": "MBL",
        "documentDescription": "{{remark}}",
        "docUrl": "ducumenturl"
      } 
                        ]
}
################################################
# Make adjust for number of HBL here
num_duplicates=10
HBL = [Function.increment_placeholders(houseBLs, i) for i in range(1, num_duplicates + 1)]
Result1 = {"houseBLs": HBL} # HouseBL
Items.update(Result1)
Result2={"items":[Items]}
Result3={"manifestDetails":Result2}
Result4=Function.update_dict(ServiceRequest,Jobrecap,ShipmentDetail,Container)
Result5=Function.update_dict(Result4,Result3,DocumentList)
Result6={"serviceRequest":Result5}
Finaldata=Function.update_dict(data,Agentinfo,Result6)

############################################################################################################
variables = {
    "WorkNo": "",
    "Worktype":"ILCL",
    "DirectDelivery":"No",
    "PartialCheck":"No",
    "PTNRNAME": "MICCO LOGISTICS - SOLE PROPRIETORSHIP L.L.C",
    "PTNRCODE": "MICC",
    "UCID": "000084",
    ###########################
    "HBL[i]":"",
    "Cargotype":"GP",
    "Cargotype[i]":"GP",
    "CargoCode[i]":"C20",
    "MBL": "",
    "CNTR":"",
    "Sztp":"45G0",
    ###########################
    "TotalQty":"",
    "TotalWgt":"",
    "TotalCbm":"",
    "Qty[i]":"",
    "Wgt[i]":"",
    "Cbm[i]":"",
    ###########################
    "ExpiryDate":"",
    "RequestDate":"",
    "Timeslot":"1",
    "RandomDoc": "",
    "remark": ""
}
######################################################
Save_HBL_QTY={}
TotalQty, TotalWgt, TotalCbm, Qty, Wgt, Cbm = Function.generate_variables_LCL(num_duplicates)
variables["TotalQty"] =str(TotalQty)
variables["TotalWgt"] =str(TotalWgt)
variables["TotalCbm"] =str(TotalCbm)
for i in range(1, num_duplicates + 1):
    Save_HBL_QTY[f"Qty[{i}]"] = variables[f"Qty[{i}]"] = str(Qty[i-1])
    Save_HBL_QTY[f"Wgt[{i}]"] = variables[f"Wgt[{i}]"] = str(Wgt[i-1])
    Save_HBL_QTY[f"Cbm[{i}]"] = variables[f"Cbm[{i}]"] = str(Cbm[i-1])
######################################################
Save_HBL_Information={}
for i in range(1,num_duplicates+1):
    Save_HBL_Information[f"HBL{i}"]       =variables[f"HBL[{i}]"] = Function.generate_random_string()
    Save_HBL_Information[f"Cargotype{i}"] =variables[f"Cargotype[{i}]"] = str("GP")
    Save_HBL_Information[f"CargoCode{i}"] =variables[f"CargoCode[{i}]"] = str("C20")
######################################################
Container=variables["CNTR"] = Function.generate_container_number()       
WorkNo=variables["WorkNo"] = Function.generate_random_string()
MBLNo=variables["MBL"] = Function.generate_random_string()
variables["RandomDoc"] = Function.generate_random_string()
variables["remark"] = "This is the Remark"
FutureDate = variables["RequestDate"] = Function.generate_future_date(days=7)
FutureDatePlus=datetime.strptime(FutureDate, '%Y-%m-%d') + timedelta(days=3)
ExpiryDate=FutureDatePlus.strftime('%Y-%m-%dT00:00:00')
variables["ExpiryDate"]=ExpiryDate
updated_data = Function.replace_placeholders(Finaldata, variables)
################ Save Information of HBL as Dictionary ########################
Save_HBL_LCL = {}
for i in range(1, num_duplicates + 1):
    Save_HBL_LCL[f"HBL[{i}]"]       = Save_HBL_Information[f"HBL{i}"]
    Save_HBL_LCL[f"Cargotype[{i}]"] = Save_HBL_Information[f"Cargotype{i}"]
    Save_HBL_LCL[f"CargoCode[{i}]"] = Save_HBL_Information[f"CargoCode{i}"]
    Save_HBL_LCL[f"Qty[{i}]"] = Save_HBL_QTY[f"Qty[{i}]"]
    Save_HBL_LCL[f"Wgt[{i}]"] = Save_HBL_QTY[f"Wgt[{i}]"]
    Save_HBL_LCL[f"Cbm[{i}]"] = Save_HBL_QTY[f"Cbm[{i}]"]
    Save_HBL_LCL[f"ContainerNo[{i}]"] = Container
###############################################################################
################### STORAGE DATA ##########################
Save_MBL_LCL = MBLNo
Save_WorkNo_LCL = WorkNo
data_file_path = r"C:\Users\nhatn\Downloads\Python\KPCFS-AutoTest\ATLP Intergration\Data\Record.py"

# Write the updated data back to the file
with open(data_file_path, "a") as data_file:
    data_file.write("Save_HBL_LCL = ")
    json.dump(Save_HBL_LCL, data_file)
    data_file.write("\n")

    data_file.write("Save_MBL_LCL = ")
    json.dump(Save_MBL_LCL, data_file)
    data_file.write("\n")

    data_file.write("Save_WorkNo_LCL = ")
    json.dump(Save_WorkNo_LCL, data_file)
    data_file.write("\n")
######################################################
# Make a POST request with the data
print(url,'\n')
response = requests.post(url, headers=headers, json=updated_data)

if response.status_code == 200:
    response_data =json.loads(response.text)
    if(response_data.get("code")=="1"):
       print("POST request successful!",'\n')
       print("Response content with Work No: ",WorkNo,"and M.BL is: ",MBLNo)
       print("Total Qty:",TotalQty,'|',"Total Weight:",TotalWgt,'|',"Total CBM:",TotalCbm)
       DraftInvoice=Function.find_unique_invoice_numbers(response_data)
       Totalamount=Function.calculate_total_amount(response_data)
       with open(data_file_path, "a") as data_file:
          data_file.write("Save_DraftInv_LCL = ")
          json.dump(', '.join(DraftInvoice), data_file)
          data_file.write("\n")
          data_file.write("Save_Totalamount_LCL = ")
          json.dump(str(Totalamount), data_file)
          data_file.write("\n")
       print(json.dumps(response_data, indent=2))
    else:
        print("POST request not successful")
        print(json.dumps(response_data, indent=2))
else:
    print("POST request failed with status code:", response.status_code)
    print("Response content:", response.text)
    




