#!/usr/bin/python3
""" interacting with an OracleDB, you can use sqlite3, which is packaged with Python. Create a new script to explore sqlite3"""
"""create a table within sqlite3"""
""" the interface is largely same as in cx_Oracle """

# importing module 
import sqlite3

# Create a table with sqlite3 
try:
    # Connect string format
    con = sqlite3.connect("test.db")

    # Now execute the sqlquery 
    cursor = con.cursor()

    # Creating a table student srollno heading which is number 
    try:
      cursor.execute("create table student(srollno number, name varchar2(10), efees number(10, 2))")
    except :
        print("Table already there")

    print("Table Created successful")
    insertsql='insert into student values (:num, :name, :fee)'
    cursor.execute(insertsql, {'num' : 10, 'name' :'kng', 'fee' : 1000 })
    print('inserted')

    selectsql='select * from student'
    cursor.execute( selectsql )
    for num , name, fee in cursor:
        print( f'fetched {num} {name} {fee}')


except Exception as e:
    print("There is a problem with sqlite", e)

# by writing finally if any error occurs 
# then also we can close the all database operation 
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

