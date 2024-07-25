import mysql.connector as connection
try:
 
 mydb=connection.connect(host='localhost',user='root',passwd='pop4321',use_pure='')
 connection.autocommit=False
 print(mydb.is_connected())
 cursor=mydb.cursor()
 query="create database newDB1"
 cursor.execute(query)
 mydb.rollback()
 mydb.commit()
 mydb.close()
except Exception as e :
    print("error encountered")
    print(e)
