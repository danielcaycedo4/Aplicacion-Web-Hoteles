import sqlite3

def get_all_habitaciones():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM habitaciones')
    habitaciones = cursor.fetchall()
    conn.close()
    return habitaciones

def get_habitaciones_by_hotel(hotel_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM habitaciones WHERE hotel_id = ?', (hotel_id,))
    habitaciones = cursor.fetchall()
    conn.close()
    return habitaciones
