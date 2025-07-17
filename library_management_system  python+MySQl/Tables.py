import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="8092278097")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS library")
mycursor.execute("USE library")

mycursor.execute("SHOW TABLES LIKE 'BookRecord' ")
result=mycursor.fetchone()
if result : 
    pass
else : #if Table doesn't exists then it will be created
    mycursor.execute("""CREATE TABLE BookRecord(BookID varchar(10) PRIMARY KEY , BookName varchar(35) , Author varchar(30) , Publisher varchar(30)) """)


mycursor.execute("SHOW TABLES LIKE 'UserRecord' ")
result=mycursor.fetchone()
if result : 
    pass
else : #if Table doesn't exists then it will be created
    mycursor.execute("""CREATE TABLE UserRecord(UserID varchar(10) PRIMARY KEY, UserName varchar(20),
                            Password varchar(20), BookID varchar(10),FOREIGN KEY (BookID) REFERENCES BookRecord(BookID))""")
    mydb.commit()
    
mycursor.execute("SHOW TABLES LIKE 'AdminRecord' ")
result=mycursor.fetchone()
if result : 
    pass
else: #if Table doesn't exists then it will be created
    mycursor.execute("""CREATE TABLE AdminRecord(AdminID varchar(10) PRIMARY KEY, Password varchar(20))""")
    data4=("Anish8092","123")
    data5=("Sujeet123","786")
    data6=("Vk321","675")
    query2="INSERT INTO AdminRecord VALUES(%s, %s)"
    mycursor.execute(query2,data4)
    mycursor.execute(query2,data5)
    mycursor.execute(query2,data6)
    mydb.commit()
    
    
mycursor.execute("SHOW TABLES LIKE 'Feedback' ")
result=mycursor.fetchone()
if result : 
    pass
else : #if Table doesn't exists then it will be created
    mycursor.execute("""CREATE TABLE Feedback(Feedback varchar(100) PRIMARY KEY, Rating varchar(10))""")


    
