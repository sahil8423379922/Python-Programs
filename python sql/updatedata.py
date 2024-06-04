import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

#Created a Table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#Inserting data in DB
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()


updatedb="UPDATE customers SET address = 'Ramadevi' WHERE name='John'"
mycursor.execute(updatedb)

mydb.commit()

updatedb ="UPDATE customers SET address = %s WHERE name=%s"
val =('Ramadevi','John')
mycursor.execute(updatedb,val)
mydb.commit()