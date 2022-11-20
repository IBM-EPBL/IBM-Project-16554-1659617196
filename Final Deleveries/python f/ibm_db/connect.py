from sqlite3 import connect, sqlite_version_info
import ibm_db 

hostname="2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
uid="ctj72194" 
pwd="EGwHtBozwfT7NDG6"
drivers="{IBM DB2 ODBC DRIVER}" 
db="bludb" 
port="32328" 
cert="cert.crt" 
dsn=( "DATABASE={0};" "HOSTNAME={1};" "PORT={2};" "UID={3};" "SECURITY=SSL;" "SSLServerCertificate={4};" "PWD={5};").format(db,hostname,port,uid,cert,pwd) 
print(dsn)

def list_all(db2):
    sql="SELECT * FROM user"
    stmt=ibm_db.exec_immediate(db2,sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print ("The ID is :", dictionary["NAME"])
        print ("The Name is:",dictionary["EMAIL"],"\n")
        dictionary = ibm_db.fetch_both(stmt)

def insert_values(conn,name,email):
    sql="INSERT INTO user VALUES ('{}','{}')".format(name,email)
    stmt = ibm_db.exec_immediate(db2,sql)
    print("Number of affected rows:",ibm_db.num_rows(stmt),"\n")

try:
     db2=ibm_db.connect(dsn," "," ") 
     print("connected to database")
     

except:
     print( "Unable to connect")
