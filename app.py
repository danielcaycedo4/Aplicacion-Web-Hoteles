from flask import Flask
from controllers.main_controller import main_bp
import sqlite3
import os

app = Flask(__name__)

# Registrar blueprints
app.register_blueprint(main_bp)

# Inicializar base de datos
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    sql_files = sorted([f for f in os.listdir('bd') if f.endswith('.sql')])
    
    for sql_file in sql_files:
        with open(os.path.join('bd', sql_file), 'r') as f:
            cursor.executescript(f.read())
    
    conn.commit()
    conn.close()

init_db()

if __name__ == '__main__':
    app.run(debug=True)
