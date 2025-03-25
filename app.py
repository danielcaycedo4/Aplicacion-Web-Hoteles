from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Inicializar base de datos
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    with open('bd/init_db.sql', 'r') as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
