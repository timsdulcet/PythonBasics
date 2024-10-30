import mysql.connector as con
from mysql.connector import Error
from mysql.connector.pooling import connect

try:
    connection = con.connect(
        host="localhost",
        user="root",
        password="",
        database="classicmodels",
        port=3307
    )
    if connection.is_connected():
        cursor = connection.cursor()
        # FIRST CODE TO RUN
        query = "CREATE TABLE attendance (id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(200),email VARCHAR(50),phone VARCHAR(20))"
        cursor.execute(query)
        
        # ----------SECOND CODE TO RUN
        query = "INSERT INTO attendance(name,email,phone) VALUES('Dotun','dotun@gmail.com','0908888888')"
        cursor.execute(query)
        connection.commit()
        if cursor.rowcount>0:
            print("attendance has been registered")
        else:
            print("attendance could not be registered")
        
        # ----------THIRD CODE TO RUN
        query = "DELETE FROM attendance WHERE id=3"
        cursor.execute(query)
        connection.commit()
        if cursor.rowcount>0:
            print("Data has been removed")
        else:
            print("Data could not be removed")
    else:
        print("Connection not succesful")
except Error as e:
    print("Error occured",e)