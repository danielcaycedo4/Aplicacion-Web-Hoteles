import sqlite3

def get_all_ciudades():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ciudades')
    ciudades = cursor.fetchall()
    conn.close()
    return ciudades
