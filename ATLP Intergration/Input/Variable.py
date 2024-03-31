import random
import cx_Oracle
# Authority
username='raizo'
password='PassW0rd!$'
#################################################################################
# DB connection
connection = cx_Oracle.connect(user="CFS_LOCAL", password="success", dsn="orcl19")
cursor = connection.cursor()
querry=" SELECT PTNR_CODE,IF_ID FROM TB_PTNR WHERE PTNR_TYPE = 'FWD' AND PAYMENT_TYPE='M' AND IF_ID IS NOT NULL "
cursor.execute(querry)
rows= cursor.fetchall()
##############################
UCID= [row[1] for row in rows]
UCID_CASH=random.choice(UCID)
##############################
PTNR= [row[0] for row in rows]
PTNR_CASH=random.choice(PTNR)
###############################
querry=" SELECT PTNR_CODE,IF_ID FROM TB_PTNR WHERE PTNR_TYPE = 'FWD' AND PAYMENT_TYPE='C' AND IF_ID IS NOT NULL "
cursor.execute(querry)
rows= cursor.fetchall()
##############################
UCID= [row[1] for row in rows]
UCID_CREDIT=random.choice(UCID)
##############################
PTNR= [row[0] for row in rows]
PTNR_CREDIT=random.choice(PTNR)
cursor.close()
connection.close()
#################################################################################
# Variable
Paymentmethod = ['CASH', 'CHEQUE', 'CREDITCARD', 'DEBITCARD', 'BANKTRANSFER', 'OTHERS', 'POS', 'MQ_CREDITCARD', 'MQ_CHEQUE', 'MQ_CASH', 'MQ_IBANKING', 'MQ_POS', 'MQ_OTHERS'];



#################################################################################
# Host
hostlocal='http://localhost:8082/ws/rest/'
host=hostlocal
# Endpoint
endpoint_token='get-token?username={{username}}&password={{password}}'
endpoint_token= endpoint_token.replace('{{username}}', username).replace('{{password}}', password)
endpoint_servicerequest='service-requests'
endpoint_companytype='company-types'
endpoint_cntr_appoinments='container-appointments?'
endpoint_service_charges_status='service-charges-status'




