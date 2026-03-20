# app.py
import streamlit as st
import requests

API_URL = "https://check1-dun-six.vercel.app/tasks/" # Ensure the URL matches your FastAPI server

st.title("Streamlit and FastAPI Demo")

# Example: Fetch data from FastAPI
if st.button("Get Welcome Message"):
    response = requests.get(API_URL)
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.error("Failed to fetch message from API")

# Example: Post data to FastAPI
st.subheader("Add New Item")
name = st.text_input("Name")
#price = st.number_input("Price", min_value=0.0, format="%.2f")
if st.button("Add Inventory"):
    data = {"task": name}
    response = requests.post(f"{API_URL}inventory", json=data)
    if response.status_code == 200:
        st.success("Inventory added successfully!")
    else:
        st.error("Failed to add inventory")
