#To install mysql on m/c or to setup mysql using python follow below steps

#Open command prompt > pip3 install mysql-connector

import mysql.connector

mydb = mysql.connector.connect("hostname", "usernmae", "passsword", "dbname")

mycursor = mydb.cursor()

mycursor.execute("show databases")
mycursor.execute("select * from student")

result = mycursor.fetchall()

for i in result:
    print(i)