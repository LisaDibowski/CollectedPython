import mysql.connector
import sys
´
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
    with open('outputfile.txt', 'w') as f:
        sys.stdout = f
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("name = ", row[0], )
            print("address  = ", row[1], "\n")

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)


