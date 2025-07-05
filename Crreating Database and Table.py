import mysql.connector

def Create_DB():
    Con=mysql.connector.connect(host="localhost",user="root",password="Ayaan#@$2014")
    try:
        if Con.is_connected():
            cur=Con.cursor()
            Q="CREATE DATABASE Employees"
            cur.execute(Q)
            print("Employees database created successfully")
    except:
        print("Databse name already exist")
        Con.close()

def Create_Table():
    Con=mysql.connector.connect(host="localhost",user="root",password="Ayaan#@$2014",database="Employees")
    if Con.is_connected():
        cur=Con.cursor()
        Q="CREATE TABLE EMP(ENO INT PRIMARY KEY,ENAME VARCHAR(20),GENDER VARCHAR(3),SALARY INT);"
        cur.execute(Q)
        print("Emp Table created successfully")
    else:
        print("Table Name already exists")
        Con.close()

ch='y'
while ch=='y' or ch=='Y':
    print("\nInterfacing Python with mysql")
    print("1. To Create Database")
    print("2. To Create Table")
    opt=int(input("Enter your choice:"))
    if opt==1:
        Create_DB()
    elif opt==2:
        Create_Table()
    else:
        print("Invalid Choice")
    opt=input("Do you want to perform another operation(y/n):")
