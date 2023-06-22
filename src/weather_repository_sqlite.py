import sqlite3
database_path=""

def init_db(database):
    global database_path
    database_path=database
    con = sqlite3.connect(database_path)
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS cities(id, name, temperature, rain_probability)"
    )




def create(weather):
    con = sqlite3.connect(database_path)
    try:
        cur = con.cursor()
        cur.execute(
            """
            INSERT INTO cities ("id", "name", "temperature", "rain_probability") 
            VALUES (?, ?, ?, ?);
            """,
            [
                weather["id"],
                weather["name"],
                weather["temperature"],
                weather["rain_probability"],
            ],
        )
        # {'id': 'MNG', 'name': 'Managua', 'temperature': 38, 'rain_probability': 0.7}
        con.commit()
    finally:
        con.close()


def update(weather):
    con = sqlite3.connect(database_path)
    try:
        cur = con.cursor()
        cur.execute(
            """
            UPDATE cities 
               SET "name"=?, "temperature"=?, "rain_probability"=?
             WHERE "id"=?
            """,
            [
                weather["name"],
                weather["temperature"],
                weather["rain_probability"],
                weather["id"],
            ],
        )
        con.commit()
    finally:
        con.close()


def read(id):
    con = sqlite3.connect(database_path)
    try:
        cur = con.cursor()
        res = cur.execute("SELECT * FROM cities WHERE id=?", [id])
        row = res.fetchone()
        # (BIO, Bilbao. 19, 0.6)
        city = {
            "id": row[0],
            "name": row[1],
            "temperature": row[2],
            "rain_probability": row[3],
        }

        return city
    finally:
        con.close()


def read_all():
    con = sqlite3.connect(database_path)
    try:
        cur = con.cursor()
        res = cur.execute("SELECT * FROM cities")
        resultado = res.fetchall()
        print(resultado)
        return resultado
    finally:
        con.close()


def delete(id):
    con = sqlite3.connect(database_path)
    try:
        cur = con.cursor()
        res = cur.execute("DELETE * FROM cities WHERE id=?", [id])
        
        return res
    finally:
        con.close()