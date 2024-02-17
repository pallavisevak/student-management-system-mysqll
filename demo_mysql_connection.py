import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
#we can access db when making connection
 #database="mydatabase"
)
# A cursor is used to interact with the database by executing SQL queries.
mycursor=mydb.cursor()

#create table
# mycursor=mydb.cursor()
# mycursor.execute("CREATE TABLE customer (name VARCHAR(255), address VARCHAR(255))")

# primary key: each record has its own unique id
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# If the table already exists, use the ALTER TABLE keyword
# Create primary key on an existing table:
# mycursor.execute("ALTER TABLE customer ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


#insert data into table
# sql=" INSERT INTO customer (name,address) VALUES(%s,%s)"
# val=("john","ahmedabad 22")
# mycursor.execute(sql,val)
# mydb.commit()  #It is required to make the changes, otherwise no changes are made to the table.
# print(mycursor.rowcount,"record inserted")


# Insert Multiple Rows: executemany()
# second parameter of the executemany() method is a list of tuples, containing the data you want to insert:

# sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
#
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")


#we can get the id of the row by entering the data to the table
# sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)
# mydb.commit()
# print("1 record inserted, ID:", mycursor.lastrowid)

#select data from databse and display as result
# mycursor.execute("SELECT * FROM customer")
# myresult = mycursor.fetchall()
# for i in myresult:
#   print(i)

#to select some of the column
# mycursor.execute("SELECT name FROM customer")
# myresult = mycursor.fetchall()
# for i in myresult:
#   print(i)

#fetch first row
# mycursor.execute("SELECT * FROM customer")
# myresult = mycursor.fetchone()
# print(myresult)

#fetch particular row(filterout)
# sql = "SELECT * FROM customer WHERE address ='Park Lane 38'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for i in myresult:
#   print(i)


# Wildcard Characters(%)
# You can also select the records that starts, includes, or ends with a given letter or phrase.
# sql = "SELECT * FROM customer WHERE address LIKE '%way%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for i in myresult:
#   print(i)


# sql = "SELECT * FROM customer WHERE address = %s"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()
# for i in myresult:
#   print(i)


#order by :sort the result in ascending or descending order
# sql = "SELECT * FROM customer ORDER BY name"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for i in myresult:
#   print(i)
#       or

# sql = "SELECT * FROM customer ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for i in myresult:
#   print(i)

# delete record
# sql = "DELETE FROM customer WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

#to prevent from sql injection
# sql = "DELETE FROM customer WHERE address = %s"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")


#delete existing table
# sql = "DROP TABLE customers"
# mycursor.execute(sql)

# DROP ONLY IF EXIST
# sql = "DROP TABLE IF EXISTS customers"
# mycursor.execute(sql)

#update data
# sql = "UPDATE customer SET address = 'Canyon 123' WHERE address = 'Valley 345'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")

         # or prevent from mysql injection
# sql = "UPDATE customer SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")

#limit the data
# mycursor.execute("SELECT * FROM customer LIMIT 5")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# limit data from another position
# mycursor.execute("SELECT * FROM customer LIMIT 5 OFFSET 2")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


#create databse
#mycursor.execute("CREATE  DATABASE mydatabase")


#to show database
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)

# to check if table exist
# mycursor.execute("SHOW TABLES")
# for i in mycursor:
#     print(i)

