import sqlite3

def get_all_hoteles():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM hoteles')
    hoteles = cursor.fetchall()
    conn.close()
    return hoteles

def get_hoteles_by_ciudad(ciudad_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM hoteles WHERE ciudad_id = ?', (ciudad_id,))
    hoteles = cursor.fetchall()
    conn.close()
    return hoteles
