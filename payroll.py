import streamlit as st

# Title
st.title("Employee Payroll Management System")

st.header("Employee Details")

# Employee Information
emp_id = st.text_input("Employee ID")
name = st.text_input("Employee Name")
department = st.selectbox("Department", ["HR", "Finance", "IT", "Marketing", "Sales"])
designation = st.text_input("Designation")

st.header("Salary Details")

# Salary Inputs
basic_salary = st.number_input("Basic Salary", min_value=0)
hra = st.number_input("HRA", min_value=0)
da = st.number_input("DA", min_value=0)
bonus = st.number_input("Bonus", min_value=0)
deduction = st.number_input("Deductions", min_value=0)

# Calculate Payroll
if st.button("Generate Payroll"):

    gross_salary = basic_salary + hra + da + bonus
    net_salary = gross_salary - deduction

    st.subheader("Payroll Summary")

    st.write("Employee ID:", emp_id)
    st.write("Employee Name:", name)
    st.write("Department:", department)
    st.write("Designation:", designation)

    st.write("Basic Salary:", basic_salary)
    st.write("HRA:", hra)
    st.write("DA:", da)
    st.write("Bonus:", bonus)
    st.write("Deductions:", deduction)

    st.success(f"Net Salary: {net_salary}")