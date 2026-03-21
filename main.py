# app.py
import streamlit as st
import requests

API_URL = "https://check1-seven.vercel.app" # Ensure the URL matches your FastAPI server

st.title("Streamlit and FastAPI Demo")

# Example: Post data to FastAPI
st.subheader("Add New Item")
input = st.text_input("Name: ")
#price = st.number_input("Price", min_value=0.0, format="%.2f")
if st.button("Submit"):
    if input:
        #data = {"task": name}
        response = requests.post(f"{API_URL}/add_todo", json={"data": input})
        if response.status_code == 200:
            st.success("Inventory added successfully!")
        else:
            st.error("Failed to add inventory")

# Example: Fetch data from FastAPI
if st.button("Display"):
    response = requests.get(f"{API_URL}/get_todo")
    if response.status_code == 200:
        st.write()
    else:
        st.error("Failed to fetch message from API")
