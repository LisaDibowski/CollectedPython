#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 02:52:00 2021

@author: ldibowsk
"""
import mysql.connector
#import sys

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="toor",
  database="itzero",
)

#create a curser
mycursor = mydb.cursor()

#create a database
#mycursor.execute("CREATE DATABASE itzero")

# # # CHECK IF DATABASE EXISTS
#mycursor.execute("SHOW DATABASES")


# CREATE TABLE 
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# # # check if table exists
#mycursor.execute("SHOW TABLES")

# # # create table with primary key
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))") 

# # # ALTER TABLE to create primary key on existing table
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 

# # # INSERT record INTO
#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("John", "Highway 21")
#mycursor.execute(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record inserted.")

# # # insert many
#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = [
#       ('Peter', 'Lowstreet 4'),
#       ('Amy', 'Apple st 652'),
#       ('Hannah', 'Mountain 21'),
#       ('Michael', 'Valley 345'),
#       ('Sandy', 'Ocean blvd 2'),
#]       
#mycurso#r.executemany(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "was inserted.") 

     
     
#for x in mycursor:
#  print(x) 

#mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM customers")

#myresult = mycursor.fetchall()

#mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM customers")

#myresult = mycursor.fetchone()

#print(myresult) 

for x in myresult:
  print(x)
