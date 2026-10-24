
import os
import mysql.connector

db = mysql.connector.connect(
    host=os.getenv("DB_HOST", "host.docker.internal"),
    port=int(os.getenv("DB_PORT", "3307")),
    user=os.getenv("DB_USER", "appuser"),
    password=os.getenv("DB_PASSWORD", "AppDemo123!"),
    database=os.getenv("DB_NAME", "names_db")
)

cursor = db.cursor()

name = input("Enter a name: ").strip()

if name:
    cursor.execute(
        "INSERT INTO people (name) VALUES (%s)",
        (name,)
    )
    db.commit()
    print(f"Saved: {name}")

cursor.execute("SELECT id, name FROM people")

print("\nNames stored in the database:")

for person in cursor.fetchall():
    print(person)

cursor.close()
db.close()
