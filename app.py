import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.scheduling import get_schedules
from backend.train_model import train_model, predict_seats
from backend.database import save_prediction

import streamlit as st
import json

def main():
    st.title("SwiftSeat Booking and Reservation")
    
    menu = ["Home", "Book Seat", "Real-Time Updates", "Optimized Routes"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    model = train_model()
    
    if choice == "Home":
        st.subheader("Welcome to SwiftSeat!")
        st.write("""
        SwiftSeat is a smart booking and reservation system designed to enhance your commuting experience in Nairobi.
        Our platform allows you to reserve seats in advance for public transport options such as buses and minivans,
        providing real-time updates and notifications to reduce waiting times and improve overall satisfaction.
        """)
        
        st.write("### Key Features:")
        st.markdown("""
        - **Advance Seat Booking**: Reserve your seat in advance to avoid long queues and ensure a hassle-free journey.
        - **Real-Time Updates**: Get live notifications about bus schedules, seat availability, and expected arrival times.
        - **Optimized Routes**: Our system optimizes pick-up and drop-off points to streamline traffic flow and reduce congestion.
        - **Efficient Seat Utilization**: Maximize seat usage by allowing multiple bookings based on journey details.
        """)
        
        st.image("C:/Users/jaymk/OneDrive/Desktop/swiftseat_model 2/static/SwiftSeat in action.jpg", caption="SwiftSeat in Action")

    elif choice == "Book Seat":
        st.subheader("Book a Seat")
        distance = st.number_input("Enter distance (in meters):")
        duration = st.number_input("Enter duration (in seconds):")
        duration_in_traffic = st.number_input("Enter duration in traffic (in seconds)", value=duration)  # Optional field
        
        if st.button("Predict Seats"):
            input_data = {
                'distance': distance,
                'duration': duration,
                'duration_in_traffic': duration_in_traffic
            }
            prediction = predict_seats(model, input_data)
            seat_number = np.random.randint(1, 100)  # Randomly assign a seat number for demo purposes
            price = 500  # Example of price
            
            save_prediction(distance, duration, duration_in_traffic, prediction)
            st.success(f"Your seat has been booked successfully! Seat Number: {seat_number}")
            st.write(f"**Price for booking:** KSh {price}")

            if st.button("Confirm Booking"):
                st.write("Booking confirmed! Thank you for using SwiftSeat.")
                st.write("Proceed to payment to complete your booking.")
                # integration with a payment gateway API for real transactions can be done here
                
    elif choice == "Real-Time Updates":
        st.subheader("Real-Time Updates")
        st.write("Here you can see the real-time updates for bus schedules and availability.")
        schedules = get_schedules()
        st.write("No schedules available at the moment.")

    elif choice == "Optimized Routes":
        st.subheader("Optimized Routes")
        st.write("This feature will provide you with optimized routes based on current traffic conditions and other factors.")
        st.write("**Feature to be implemented:** Integration with a traffic API for real-time route optimization.")

if __name__ == '__main__':
    main()
