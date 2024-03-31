import cx_Oracle
import random
####################### SET UP CONNECTION ORACLE DB #######################
# Connect to the Oracle database
conn = cx_Oracle.connect(user="CFS_LOCAL",password="success",dsn="orcl19")  # Service Name
cur = conn.cursor()
cur.execute("SELECT GNRL_CODE,GNRL_NM FROM TB_GNRL_CODE WHERE 1=1 AND GNRL_TYPE = 'TRT'")
rows = cur.fetchall()
random_row = random.choice(rows)
GNRL_CODE   = random_row[0]
GNRL_NM = random_row[1]
cur.close()
conn.close()