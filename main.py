import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user= "root",
    passwd="Hathout98",
    database="Company"
)
mycursor=myconn.cursor()
mycursor.execute("Select * from employee)

