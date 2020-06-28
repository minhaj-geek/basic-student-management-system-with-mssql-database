# basic-student-management-system-with-mssql-database

1. Database Configuration 

You need to Configure database First.
install mssql server on your machine.

Create a Database name "python_db" by Runnig Query of : 

create database python_db

the run sql script student_table_sql_query and then course_table_sql_query your database is maintanied.

2.Install pyodbc library in your python environment or interpreter

Configure pydboc to Connect to make things easy for you just make changes in following line of code written at start of python script.
conn=pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=;"  #Enter Server name
    "Database=;" #Enter Database name
    "Trusted_Connection=yes;"
)

just Enter you Server name and database name which is python_db


and the project will work on your machine.
