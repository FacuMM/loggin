import sqlite3



def crear_tabla():
    #Intentamos crar la tabla desde controles
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """)

        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
print("Base de datos inicializada correctamente")
