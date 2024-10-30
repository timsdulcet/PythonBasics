import mysql.connector

connection =  mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="classicmodels",
    port=3307
)
if(connection.is_connected()):
    print("Yipeee!! DB is connected o!")
else:
    print("DB could not be connected to")