#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ldibowsk
"""
import mysql.connector
import sys


def print_main():
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='itzero',
                                         user='root',
                                         password='toor')

        cursor = connection.cursor()
        sql_select_query = """SELECT * from customers where id = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (id,))
        # fetch result
        records = cursor.fetchall()

        for row in records:
            print("name = ", row[0], )
            print("address  = ", row[1], "\n")


    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))    

def main():
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='itzero',
                                         user='root',
                                         password='toor')

        sql_select_Query = "SELECT * from customers"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        with open('outputfile1.txt', 'w') as f:
            sys.stdout = f
            print("Total number of rows in table: ", cursor.rowcount)

            print("\nPrinting each row")
            for row in records:
                print("name = ", row[0], )
                print("address  = ", row[1], "\n")

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)

def create_db():
        connection = mysql.connector.connect(host='localhost',
                                         database='itzero',
                                         user='root',
                                         password='toor')

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE mydatabase")


def show_db():
        connection = mysql.connector.connect(host='localhost',
                                         database='itzero',
                                         user='root',
                                         password='toor')

        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES")
        
if __name__ == '__main__':
    main()