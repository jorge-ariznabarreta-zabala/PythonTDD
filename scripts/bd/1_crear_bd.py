import mysql.connector

# con = sqlite3.connect("wheather.db")
con = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)
cur = con.cursor()
cur.execute("CREATE DATABASE weather")
