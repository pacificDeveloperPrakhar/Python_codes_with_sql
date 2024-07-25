import mysql.connector as connection
import sys
try:
    mydb=connection.connect(host='localhost',user='root',passwd='pop4321',use_pure=True)
    connection.autocommit=False
    print(mydb.is_connected())

    queries=['use python_sql_learn','create table if not exists  customers(first_name char(10)  not null,last_name char(10),city char(20),email char(255)  not null)','insert into customers (first_name,last_name,city,email) values(%s,%s,%s,%s)']
    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Hank']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Martinez']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
    email_domains = ['example.com', 'mail.com', 'test.com', 'demo.com']
    values=[(first_name,last_name,city,email) for first_name in first_names for last_name in last_names for city in cities for email in email_domains]
    print(values)

    cursor=mydb.cursor()
    for query in queries:
        if "insert" in query.lower():
         cursor.executemany(query,values)
        else:
          cursor.execute(query)
        print("execued the query %s"%(query))
    mydb.commit()
    mydb.close()
    
except Exception as e:
    print(e)