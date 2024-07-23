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

def create_booking(user_id, schedule_id, seats_booked):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Bookings (user_id, schedule_id, booking_time, seats_booked) VALUES (%s, %s, NOW(), %s)",
                (user_id, schedule_id, seats_booked)
            )
            conn.commit()
            print(f"Booking created successfully for user_id {user_id} and schedule_id {schedule_id}.")
        except Error as e:
            print(f"Failed to create booking: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database.")

if __name__ == "__main__":
    # Test the function with sample data
    create_booking(user_id=1, schedule_id=1, seats_booked=3)
