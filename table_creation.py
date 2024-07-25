import mysql.connector as connection
try:
    mydb=connection.connect(host='localhost',user='root',passwd='pop4321',use_pure=True)
    connection.autocommit=False
    print(mydb.is_connected())
    queries=['use python_sql_learn','create table if not exists  customers(first_name char(10) unique not null,last_name char(10),city char(20))','insert into customers (first_name,last_name,city) values(\'john\',\'smith\',\'california\')']
    cursor=mydb.cursor()
    for query in queries:
        cursor.execute(query)
        print("execued the query %s"%(query))
    mydb.commit()
    mydb.close()
    
except Exception as e:
    print(e)