#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='toor', database= 'it_data', host ='localhost', port='3306')

create_cursor = mariadb_connection.cursor()

create_cursor.execute("CREATE DATABASE it_data")

create_cursor.execute("SHOW DATABASES")

create_cursor.execute("CREATE TABLE python_creation_table (COLUMN1 VARCHAR(2), COLUMN2 Int)")

create_cursor.execute("SHOW TABLES")

for x in create_cursor:
    print(x)

