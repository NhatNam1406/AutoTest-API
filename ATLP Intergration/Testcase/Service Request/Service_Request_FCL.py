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
    "jobType": "IFCL_STRG",
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
        "iso": "{{Sztp}}",
        "containerNo": "{{CNTR[i]}}",
        "operator": "RHS",
        "returnTerminal": "AEKHL",
        "expiryDate": "{{ExpiryDate}}",
        "requestedDate": "{{RequestDate}}",
        "timeSlotNo": "{{Timeslot}}"
}
#####################################################
Items={
          "type": "{{Worktype}}",
          "mblNumber": "{{MBL}}",
          "containerNo": "{{CNTR[i]}}",
          "sealNo": "6536767",
          "iso": "{{Sztp}}",
          "cargoTypeDesc": "{{Cargotype}}",
          "consigneeName": "Consignee Name",
          "consigneeEmail": "Consignee Email",
          "consigneePhone": "Consignee Phone",
          "quantity": "{{TotalQty[i]}}",
          "totalWeight": "{{TotalWgt[i]}}",
          "totalVolume": "{{TotalCbm[i]}}",
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
              "parentId": "{{CNTR[i]}}",
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
# Make adjust for number of HBL and Container here
num_duplicates  =   3
items_list      =  []
containers_list =  []

for i in range(1, num_duplicates + 1):
    item = Function.increment_placeholders(Items, i)
    item["containerNo"] = f"{{{{CNTR[{i}]}}}}"
    houseBLs_copy = houseBLs.copy()
    houseBL = Function.increment_placeholders(houseBLs_copy, i)
    item["houseBLs"] = [houseBL]
    items_list.append(item)
    ############################
    container = Container.copy()
    container["containerNo"] = f"{{{{CNTR[{i}]}}}}"
    containers_list.append(container)

Result = {"items": items_list}
Result2={"manifestDetails":Result}
Result3 = {"containers": containers_list}
Result4=Function.update_dict(ServiceRequest,Jobrecap,ShipmentDetail,Result3,Result2,DocumentList)
Result5={"serviceRequest":Result4}
Finaldata=Function.update_dict(data,Agentinfo,Result5)
################################################
variables = {
    "WorkNo": "",
    "PTNRNAME": "MICCO LOGISTICS - SOLE PROPRIETORSHIP L.L.C",
    "PTNRCODE": "MICC",
    "UCID": "000084",
    ##################
    "HBL[i]":"",
    "Cargotype":"GP",
    "Cargotype[i]":"GP",
    "CargoCode[i]":"C20",
    "MBL": "",
    "CNTR[i]": "",
    ##################
    "ExpiryDate":"",
    "RequestDate":"",
    "Timeslot":"1",
    "RandomDoc": "",
    "remark": "",
    ##################
    "TotalQty[i]":"",
    "TotalWgt[i]":"",
    "TotalCbm[i]":"",
    "Qty[i]":"",
    "Wgt[i]":"",
    "Cbm[i]":"",
}
################################################
Qty, Wgt, Cbm, TotalQty, TotalWgt, TotalCbm= Function.generate_variables_FCL(num_duplicates)
# Assign variables for each index
# Amount of Qty,Cbm,Wgt and Total are the same in FCL
Save_HBL_QTY={}
for i in range(1,num_duplicates+1):
    variables[f"Qty[{i}]"]        =  str(Qty[i-1])
    variables[f"Wgt[{i}]"]        =  str(Wgt[i-1])
    variables[f"Cbm[{i}]"]        =  str(Cbm[i-1])
    variables[f"TotalQty[{i}]"]   =  str(Qty[i-1])
    variables[f"TotalWgt[{i}]"]   =  str(Wgt[i-1]) 
    variables[f"TotalCbm[{i}]"]   =  str(Cbm[i-1])
    ############ The Qty of HBL Storage here #########
    Save_HBL_QTY[f"Qty[{i}]"]     = str(Qty[i-1])
    Save_HBL_QTY[f"Wgt[{i}]"]     = str(Wgt[i-1])
    Save_HBL_QTY[f"Cbm[{i}]"]     = str(Cbm[i-1])
######################################################
Save_HBL_Information={}
for i in range(1,num_duplicates+1):
    variables[f"HBL[{i}]"] = Function.generate_random_string()
    variables[f"CargoCode[{i}]"] = str("C20")
    variables[f"Cargotype[{i}]"] = str("GP")
    ###### The HBL Storage here #################
    Save_HBL_Information[f"HBL{i}"]    = variables[f"HBL[{i}]"]
    Save_HBL_Information[f"Cargotype{i}"]    = str("GP")
    Save_HBL_Information[f"CargoCode{i}"]    = str("C20")
######################################################
Save_Cntr_List=[]
container_numbers = Function.generate_multiple_container(num_duplicates)
for i, CNTR in enumerate(container_numbers, start=1):
    variables["CNTR[" + str(i) + "]"] = CNTR
    Save_Cntr_List.append(CNTR) # The Container List Storage here

################ Save Information of HBL as Dictionary ########################
Save_HBL_FCL = {}
for i in range(1, num_duplicates + 1):
    Save_HBL_FCL[f"HBL[{i}]"]       = Save_HBL_Information[f"HBL{i}"]
    Save_HBL_FCL[f"Cargotype[{i}]"] = Save_HBL_Information[f"Cargotype{i}"]
    Save_HBL_FCL[f"CargoCode[{i}]"] = Save_HBL_Information[f"CargoCode{i}"]
    Save_HBL_FCL[f"Qty[{i}]"] = Save_HBL_QTY[f"Qty[{i}]"]
    Save_HBL_FCL[f"Wgt[{i}]"] = Save_HBL_QTY[f"Wgt[{i}]"]
    Save_HBL_FCL[f"Cbm[{i}]"] = Save_HBL_QTY[f"Cbm[{i}]"]
    Save_HBL_FCL[f"ContainerNo[{i}]"] = Save_Cntr_List[i-1]
######################################################
WorkNo=variables["WorkNo"] = Function.generate_random_string()
MBLNo=variables["MBL"]     = Function.generate_random_string()
variables["RandomDoc"]     = Function.generate_random_string()
variables["remark"] = "This is the Remark"
FutureDate = variables["RequestDate"] = Function.generate_future_date(days=7)
FutureDatePlus=datetime.strptime(FutureDate, '%Y-%m-%d') + timedelta(days=3)
ExpiryDate=FutureDatePlus.strftime('%Y-%m-%dT00:00:00')
variables["ExpiryDate"]=ExpiryDate
######################################################
variables["DirectDelivery"]="No"
variables["PartialCheck"]="No"
variables["Sztp"]="45G0"
variables["Worktype"]="IFCL"
################### STORAGE DATA ##########################
Save_MBL_FCL = MBLNo
Save_WorkNo_FCL = WorkNo
data_file_path = r"C:\Users\nhatn\Downloads\Python\KPCFS-AutoTest\ATLP Intergration\Data\Record.py"

# Write the updated data back to the file
with open(data_file_path, "a") as data_file:
    data_file.write("Save_HBL_FCL = ")
    json.dump(Save_HBL_FCL, data_file)
    data_file.write("\n")

    data_file.write("Save_MBL_FCL = ")
    json.dump(Save_MBL_FCL, data_file)
    data_file.write("\n")

    data_file.write("Save_WorkNo_FCL = ")
    json.dump(Save_WorkNo_FCL, data_file)
    data_file.write("\n")

    data_file.write("Save_No_Cntr_FCL = ")
    json.dump(num_duplicates, data_file)
    data_file.write("\n")

######################################################
updated_data = Function.replace_placeholders(Finaldata, variables)
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
          data_file.write("Save_DraftInv_FCL = ")
          json.dump(', '.join(DraftInvoice), data_file)
          data_file.write("\n")
          data_file.write("Save_Totalamount_FCL = ")
          json.dump(str(Totalamount), data_file)
          data_file.write("\n")
       print(json.dumps(response_data, indent=2))
    else:
        print("POST request not successful")
        print(json.dumps(response_data, indent=2))
else:
    print("POST request failed with status code:", response.status_code)
    print("Response content:", response.text)







