import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        passwd="your_password",
        database="your_database"
    )
    print("Connected to MySQL!")
    
    # Further operations like querying or inserting data
    
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("MySQL connection is closed")
