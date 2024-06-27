import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'django',
    passwd = 'Django_100'
)

# prepare a cursor object

cursorObject = dataBase.cursor()

#create the database
cursorObject.execute("CREATE DATABASE crmdata")

print("Data base created")
