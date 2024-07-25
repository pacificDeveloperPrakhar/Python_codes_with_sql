import mysql.connector as connection
try:
 
 mydb=connection.connect(host='localhost',user='root',passwd='pop4321',use_pure='')
 connection.autocommit=False
 print(mydb.is_connected())
 cursor=mydb.cursor()
 queries=['use python_sql_learn','select * from customers']
 for query in queries:
    cursor.execute(query)
    result=cursor.fetchall()
 print(len(result))
 mydb.rollback()
 mydb.commit()
 mydb.close()
except Exception as e :
    print("error encountered")
    print(e)
