from flask import Flask, request, jsonify
import sqlite3
import os



app = Flask(__name__)
def crear_tabla():
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
crear_tabla()
# Crear la base de datos si no existe

DATABASE = "database.db"

def conectar_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Usuario registrado exitosamente"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"message": "Login exitoso"})
    else:
        return jsonify({"message": "Credenciales incorrectas"}), 401

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
