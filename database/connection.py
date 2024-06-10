
DATABASE_NAME = './database/magazine.db'

def get_db_connection():
    import sqlite3
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn 

CURSOR = get_db_connection().cursor()
CONN = get_db_connection()
 