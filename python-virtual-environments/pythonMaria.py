#!/usr/bin/python
import html
import mysql.connector as mariadb
from mysql.connector import Error

class pythonMaria:
    def __init__(self):
        self.mrdb_connection = None
        self.mrdb_cursor = None

    def pythonMaria_getConnect(self):
        try:
            self.mrdb_connection
            if self.mrdb_connection is None:
                self.mrdb_connection = mariadb.connect(
                    host='localhost',
                    user='root',
                    password='110235',
                    database='msc-skl_db',
                    charset='utf8mb4'
                )
            
            return self.mrdb_connection
        except Error as e:
            print("Error connect mySQL : ",e)

    def pythonMaria_closeConnect(self):
        if self.mrdb_connection is None:
            print("CONNECTION IS NONE!")
        else:
            self.mrdb_connection.close()
            self.mrdb_connection = None

    def pythonMaria_SelectStar(self,table_name):
        try:
            temp_connection = self.pythonMaria_getConnect()
            mrcursor = temp_connection.cursor()
            mrcursor.execute("SELECT * FROM {}".format(table_name))
            tables = mrcursor.fetchall()
            return tables
        except Error as e:
            print("Error reading data from mySQL table: ",e)
        finally:
            print("MySQL select from star : ", table_name)

    def pythonmaria_innerjoin_cpoANDpro(self):
        temp_connection = self.pythonMaria_getConnect()
        mrcursor = temp_connection.cursor()
        mrcursor.execute("SELECT cpo.CustomerProductOrderID, cpo.CustomerProductOrderQuantity, cpo.CustomerProductOrderVat, cpo.ProductName, pro.ProductDescription, pro.ProductPrice FROM customerproductorder cpo JOIN product pro ON cpo.ProductName = pro.ProductName")
        cpoANDpro = mrcursor.fetchall()

        return cpoANDpro

    def pythonmaria_insert_customerorder(self,data):
        try:
            ins_connection = mariadb.connect(
                host='localhost',
                user='root',
                password='110235',
                database='msc-skl_db',
                charset='utf8mb4'
            )

            ins_cursor = ins_connection.cursor()
            insert_sql = "INSERT INTO customerproductorder (CustomerProductOrderId,CustomerProductOrderDate,ProductName,CustomerProductOrderQuantity,CustomerProductOrderVat,ClerkID,CustomerName) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            insert_val = (data[0], data[1], data[2], data[3], data[4], data[5], data[6])
            ins_cursor.execute(insert_sql,insert_val)

            ins_connection.commit()

            print(ins_cursor.rowcount, "record inserted")

        except Error as e:
            print("Error insert data to mySQL table : ",e)

    def pythonmaria_insert_quotation(self,data):
        try:
            ins_connection = mariadb.connect(
                host='localhost',
                user='root',
                password='110235',
                database='msc-skl_db',
                charset='utf8mb4'
            )

            #quo_id,quo_date,quo_total,quo_vat,quo_net,cpo_id
            ins_cursor = ins_connection.cursor()
            insert_sql = "INSERT INTO quotation (QuotationID,QuotationDate,QuotationTotalPrice,QuotationVatPrice,QuotationNetTotal,CustomerProductOrderID) VALUES (%s, %s, %s, %s, %s, %s)"
            insert_val = (data[0], data[1], data[2], data[3], data[4], data[5])
            ins_cursor.execute(insert_sql,insert_val)

            ins_connection.commit()

            print(ins_cursor.rowcount, "record inserted")

        except Error as e:
            print("Error insert data to mySQL table : ",e)

    
    def pythonMaria_Select(self,field_name,table_name):
        temp_connection = self.pythonMaria_getConnect()
        mrcursor = temp_connection.cursor()
        mrcursor.execute("SELECT {} FROM {}".format(field_name,table_name))
        rows = mrcursor.fetchall()
        print((rows))
        selected_list = ""
        for field_name in mrcursor:
            print("Employee ID: {}".format(field_name))
            selected_list = selected_list + ("Employee ID: {}".format(field_name)) + "\n"

        return rows

    def pythonMaria_Select2(self,field_name1,field_name2,table_name):
        temp_connection = self.pythonMaria_getConnect()
        mrcursor = temp_connection.cursor()
        mrcursor.execute("SELECT {},{} FROM {}".format(field_name1,field_name2,table_name))
        rows = mrcursor.fetchall()
        return rows    

    def convertTuple(tup): 
        str =  ''.join(tup) 
        return str

