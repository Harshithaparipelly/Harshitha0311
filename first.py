import streamlit as st

with st.form("my_form"):
    col1, col2 = st.columns(2)

    with col1:
        first_name = st.text_input("First Name")

    with col2:
        second_name = st.text_input("Second Name")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")
    address = st.text_area("Enter your Address")

    submit = st.form_submit_button("Submit")

if submit:
    st.write("First Name:", first_name)
    st.write("Second Name:", second_name)
 

