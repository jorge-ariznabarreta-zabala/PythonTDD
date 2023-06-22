import mysql.connector

# con = sqlite3.connect("wheather.db")
con = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="weather"
)

cur = con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS cities(id VARCHAR(3) PRIMARY KEY, name VARCHAR(20), temperature INT, rain_probability FLOAT)"
)
