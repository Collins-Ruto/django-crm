import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
)

# prepare cursor object
cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE collinsco")

print("All Done!")