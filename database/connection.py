from database.connection import get_db_connection
conn = get_db_connection()

# Example usage
cursor = conn.cursor()
cursor.execute("SELECT * FROM authors") 
results = cursor.fetchall()
