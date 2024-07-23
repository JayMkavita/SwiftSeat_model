import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="sweatuser",
            password="strongpassword13",
            database="swiftseat"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def fetch_schedules():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Schedules")
        schedules = cursor.fetchall()
        conn.close()
        return schedules
    return []

def save_prediction(distance, duration, duration_in_traffic, predicted_seats):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO predictions (distance, duration, duration_in_traffic, predicted_seats)
                VALUES (%s, %s, %s, %s)
                """,
                (distance, duration, duration_in_traffic, predicted_seats)
            )
            conn.commit()
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
