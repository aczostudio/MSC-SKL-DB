#!/usr/bin/python
import html
import mysql.connector as mariadb
from mysql.connector import Error

mrdb_connection = None
mrdb_cursor = None

def pythonMaria_getConnect():
    try:
        global mrdb_connection
        if mrdb_connection is None:
            mrdb_connection = mariadb.connect(
                host='localhost',
                user='root',
                password='110235',
                database='msc-skl_db',
                charset='utf8mb4'
            )
        
        return mrdb_connection
    except Error as e:
        print("Error connect mySQL : ",e)

def pythonMaria_closeConnect():
    if mrdb_cursor is None:
        print("CURSOR IS NONE!")
    else:
        mrdb_cursor.close()
    if mrdb_connection is None:
        print("CONNECTION IS NONE!")
    else:
        mrdb_connection.close()

def pythonMaria_Select(field_name,table_name):
    temp_connection = pythonMaria_getConnect()
    mrcursor = temp_connection.cursor()
    mrcursor.execute("SELECT {} FROM {}".format(field_name,table_name))
    rows = mrcursor.fetchall()
    print((rows))
    selected_list = ""
    for field_name in mrcursor:
        print("Employee ID: {}".format(field_name))
        selected_list = selected_list + ("Employee ID: {}".format(field_name)) + "\n"

    #pythonMaria_closeConnect()
    return rows

def pythonMaria_Select2(field_name1,field_name2,table_name):
    temp_connection = pythonMaria_getConnect()
    mrcursor = temp_connection.cursor()
    mrcursor.execute("SELECT {},{} FROM {}".format(field_name1,field_name2,table_name))
    rows = mrcursor.fetchall()
    #print((rows))
    # selected_list = ""
    # for field_name in mrcursor:
    #     # print("Employee ID: {}".format(field_name))
    #     selected_list = selected_list + ("Employee ID: {}".format(field_name)) + "\n"

    #pythonMaria_closeConnect()
    return rows    

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str

def pythonMaria_SelectStar(table_name):
    try:
        temp_connection = pythonMaria_getConnect()
        mrcursor = temp_connection.cursor()
        mrcursor.execute("SELECT * FROM {}".format(table_name))
        tables = mrcursor.fetchall()
        # print(type(tables[0]))
        # print("Total number of rows in product is: ", mrcursor.rowcount)

        # print("\nPrinting each producct record: ",len(tables))
        # for row in tables:
        #     print("Prod_Code = ", row[0])
        #     print("Prod_Desc = ", row[1])
        #     print("Prod_Price  = ", row[2])
        #     print("Prod_Unit  = ", row[3])
        #     print("Prod_Amount = ", row[4], "\n")
                    
        return tables
    except Error as e:
        print("Error reading data from mySQL table: ",e)
    finally:
        print("MySQL select from star : ", table_name)
        #if(mrdb_connection.is_connected()):
            #temp_connection = None
            #pythonMaria_closeConnect()
            #print("MySQL select from star")
# print(pythonMaria_Select("Employee_Id", "employee"))

def pythonmaria_insert_customerorder(data):
    try:
        ins_connection = mariadb.connect(
            host='localhost',
            user='root',
            password='110235',
            database='msc-skl_db',
            charset='utf8mb4'
        )

        # ins_connection = pythonMaria_getConnect()
        ins_cursor = ins_connection.cursor()
        insert_sql = "INSERT INTO customerproductorder (CustomerProductOrderId,CustomerProductOrderDate,ProductName,CustomerProductOrderQuantity,CustomerProductOrderVat,ClerkID,CustomerName) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        insert_val = (data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        ins_cursor.execute(insert_sql,insert_val)

        ins_connection.commit()

        print(ins_cursor.rowcount, "record inserted")

    except Error as e:
        print("Error insert data to mySQL table : ",e)
    finally:
        print("Insert Success")

def pythonmaria_insert_quotation(data):
    try:
        ins_connection = mariadb.connect(
            host='localhost',
            user='root',
            password='110235',
            database='msc-skl_db',
            charset='utf8mb4'
        )

        # ins_connection = pythonMaria_getConnect()
        ins_cursor = ins_connection.cursor()
        insert_sql = "INSERT INTO quotation (QuotationID,QuotationDate,QuotationTotalPrice,CustomerProductOrderID) VALUES (%s, %s, %s, %s)"
        insert_val = (data[0], data[1], data[2], data[3])
        ins_cursor.execute(insert_sql,insert_val)

        ins_connection.commit()

        print(ins_cursor.rowcount, "record inserted")

    except Error as e:
        print("Error insert data to mySQL table : ",e)
    finally:
        print("Insert Success")

