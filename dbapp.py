#import necessary packages
import mysql.connector
import sqlalchemy

#Connect to mysql server,this is test hence encoding the credentials however for deployment consider encrypting the credentials or using secret vault.
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin"
)
mycursor = mydb.cursor() #Cursor to execute SQL statements

#Create Database
mycursor.execute("CREATE DATABASE mydatabase")

#close the connection
mydb.close()

#Updating mydb object with database name
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database = "mydatabase"
)
mycursor = mydb.cursor()
#Create table
mycursor.execute("CREATE TABLE products (Item VARCHAR(255), Item_description VARCHAR(255), Item_price INT, Item_count INT, Vendor VARCHAR(255), Vendor_address VARCHAR(255))")

#close the connection
mydb.close()
