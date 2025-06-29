import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (update user and password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Replace with your MySQL password if you have one
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
