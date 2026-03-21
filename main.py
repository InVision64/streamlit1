# app.py
import streamlit as st
import requests

API_URL = "https://check1-ruddy.vercel.app" # Ensure the URL matches your FastAPI server

st.title("Streamlit and FastAPI Demo")

# Example: Post data to FastAPI
st.subheader("Add New Item")
input_data = st.text_input("Name: ")
if st.button("Add Todo"):
    if input_data:
        response = requests.post(f"{API_URL}/add_todo/", json={"data": input_data})  # sends as JSON body
        if response.status_code == 200:
            st.success("Todo added successfully!")
            st.json(response.json())
        else:
            st.error(f"Failed to add todo. Status code: {response.status_code}")
    else:
        st.warning("Please enter a task before submitting!")
# Example: Fetch data from FastAPI
if st.button("Display"):
    response = requests.get(f"{API_URL}/get_todo")
    if response.status_code == 200:
        #st.write(response.json())
        data = response.json()
        for row in data:
            st.write(f"{row['id']} - {row['task']}")
    else:
        st.error("Failed to fetch message from API")
