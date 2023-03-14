import mysql.connector
#--------------------------------------
#variables
flag=1
flag1=1
flag3=1
flag4=0
password=1234
Students=[]
id=0
name1=0
mths=2
phys=3
eng=4
chem=5
prog=6
stCode=0
nameup=0
gradeup=0
#Notes:
#1-Database and table were created on mysql Command line, Query for databse-->create database sms;
#Query for table creation-->create table students(
    #student_id int autoincrement=1180000,
    #student_name varchar(20),
    #maths int,
    #physics int,
    #English int,
    #chemistry int,
    #programming int
    #primary key(student_id)
#)
#---------------------------used Functions------------------------
#Check the Password
def CheckPassword():
    i = 0
    print("-----------------------------")
    while 1:
        PassUser = int(input("Please Enter The password:"))
        if PassUser == password:
            x=1
            return x
        print("Wrong Password! Please Enter The password Again:")
        i += 1
        if i==3:
            x=0
            return x


#mycurser.execute("select * from students")
#myresult=mycurser.fetchall()
#for x in myresult:
#    print(x[0],x[1]," ",x[2],x[3],x[4],x[5],x[6])
#myresult=mycurser.fetchall()
#print(myresult[6][prog])

#------------------Main Classes------------------------
#class student is not used
class Student:
    no_of_student=0
    def __init__(self,name,maths,physics,English,Chemistry,Programming):
        self.__name=name
        self.__maths=maths
        self.__physics=physics
        self.__English=English
        self.__Chemistry=Chemistry
        self.__Programming=Programming
        Student.no_of_student+=1
#------------------------------------------------------------------------
#Main Function
while flag==1:
    passcheck=CheckPassword()
    if passcheck==0:
        print("----------------------")
        print("You Are not Admin")
        print("----------------------")
        flag=0
    else:
        print("----------------------------Welcome Admin-----------------------------------")
        while flag1==1:
            myconn=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Hathout98",
            database='sms'
            )
            mycurser=myconn.cursor()
            print("1-Enter New Student\n2-Search certain Student\n3-Display students Data\n4-Edit Student Data\n5-Delete Student data\n6-Exit Program")
            z=int(input("Enter Your Choice:"))
            if z==1:
                name=input("Enter Student name:")
                maths=int(input("Enter Maths Grades:"))
                Physics=int(input("Enter Physics Grades:"))
                English=int(input("Enter English Grades:"))
                Chemistry=int(input("Enter Chemistry Grades:"))
                Programming=int(input("Enter Programming Grades:"))
                sqlInsert="insert into students(Student_name,maths,physics,English,Chemistry,Programming)values(%s,%s,%s,%s,%s,%s)"
                datanew=(name,maths,Physics,English,Chemistry,Programming)
                mycurser.execute(sqlInsert,datanew)
                myconn.commit()
                print('---------------------------------------------------------------------------------------------------')
            elif z==2:
                code=input("Please Enter Student ID:")
                sqlSearch=f"select *from students where student_id={code}"
                mycurser.execute(sqlSearch)
                myresult=mycurser.fetchall()
                print("Student_id \t  Name \t\t  Maths\t \t Physics\tEnglish      Chemistry\t Programming")
                for x in myresult:
                    print(f"{x[0]}\t \t {x[1]}\t  {x[2]}\t \t {x[3]}\t \t {x[4]}\t     {x[5]}\t         \t{x[6]}")
                    print('---------------------------------------------------------------------------------------------------')
            elif z==3:
                mycurser.execute("select*from students")
                myresult=mycurser.fetchall()
                print('---------------------------------------------------------------------------------------------------')
                print("Student_id \t Name \t\t  Maths\t \t Physics\tEnglish      Chemistry\t\tProgramming")
                for x in myresult:
                     print(f"{x[0]}\t \t {x[1]}\t  {x[2]}\t \t {x[3]}\t \t {x[4]}\t     {x[5]}\t         \t{x[6]}")
                print('---------------------------------------------------------------------------------------------------')
            elif z==4:
                stCode=int(input("Enter Student ID:"))
                req=int(input("1-Student name\n2-Maths Grade\n3-Physics Grade\n4-English Grade\n5-Chemistry Grade\n6-Programming Grade\nEnter your Choice:"))
                if req==1:
                    nameup=input("Enter New Name:")
                    sqlup="update students set Student_name=%swhere student_id=%s"
                    data=(nameup,stCode)
                    mycurser.execute(sqlup,data)
                    myconn.commit()
                elif req==2:
                    gradeup=input("Enter New Grade:")
                    sqlup="update students set maths=%swhere student_id=%s"
                    data=(gradeup,stCode)
                    mycurser.execute(sqlup,data)
                    myconn.commit()
                elif req==3:
                    gradeup=input("Enter New Grade:")
                    sqlup="update students set physics=%swhere student_id=%s"
                    data=(gradeup,stCode)
                    mycurser.execute(sqlup,data)
                    myconn.commit()
                elif req==4:
                    gradeup=input("Enter New Grade:")
                    sqlup="update students set English=%swhere student_id=%s"
                    data=(gradeup,stCode)
                    mycurser.execute(sqlup,data)
                    myconn.commit()
                elif req==5:
                    gradeup=input("Enter New Grade:")
                    sqlup="update students set Chemistry=%swhere student_id=%s"
                    data=(gradeup,stCode)
                    mycurser.execute(sqlup,data)
                    myconn.commit()
                elif req==6:
                    gradeup=input("Enter New Grade:")
                    sqlup="update students set programming=%swhere student_id=%s"
                    data=(gradeup,stCode)
                    mycurser.execute(sqlup,data)
                    myconn.commit()
                
            elif z==5:
                stCode=input("Please Enter Student Code:")
                sqldel=f"delete from students where student_id={stCode}"
                mycurser.execute(sqldel)
                myconn.commit()        
            else:
                flag1=0
                flag=0