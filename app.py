import streamlit as st

# Title
st.title("Railway Reservation System")

st.header("Passenger Details")

# Passenger Name
name = st.text_input("Passenger Name")

# Train Number
train_no = st.text_input("Train Number")

# From and To Stations
from_station = st.text_input("From Station")
to_station = st.text_input("To Station")

# Date of Journey
date = st.date_input("Date of Journey")

# Class Selection
travel_class = st.selectbox(
    "Select Class",
    ["Sleeper", "AC", "First Class"]
)

# Number of Passengers
passengers = st.number_input("Number of Passengers", min_value=1, max_value=10)

# Booking Button
if st.button("Book Ticket"):
    st.success("Ticket Booked Successfully!")

    st.write("### Booking Details")
    st.write("Passenger Name:", name)
    st.write("Train Number:", train_no)
    st.write("From:", from_station)
    st.write("To:", to_station)
    st.write("Date:", date)
    st.write("Class:", travel_class)
    st.write("Passengers:", passengers)