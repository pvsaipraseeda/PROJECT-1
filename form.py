import streamlit as st
import pandas as pd
import os


st.title("Student Registration Form")

with st.form("registration_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name1 = st.text_input("First Name")
    with col2:
        name2 = st.text_input("Last Name")
    
    name3 = st.text_input("Email")
    name4 = st.text_input("Password", type="password")
    name5 = st.text_input("Confirm Password", type="password")
    name6 = st.text_area("Address")
    
    submit = st.form_submit_button("Submit")


if submit:
    if name4 != name5:
        st.error("Passwords do not match ❌")
    else:
        st.success("Registration Successful ✅")
        st.write(name1, name2, name3, name6)