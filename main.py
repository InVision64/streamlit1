# app.py
import streamlit as st
import requests
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
if not SUPABASE_URL or not SUPABASE_KEY:
    st.error("Missing Supabase credentials")
    st.stop()
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

API_URL = "https://check1-ruddy.vercel.app" # Ensure the URL matches your FastAPI server

st.title("Streamlit and FastAPI Demo")

# Login
email = st.text_input("Email")
password = st.text_input("Password", type="password")
if st.button("Login"):
    try:
        res = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if res.session:
            st.session_state["token"] = res.session.access_token
            st.success("Logged in!")
        else:
            st.error("Login failed")
    except Exception as e:
        st.error(str(e))
        
# After login
if "token" in st.session_state:
    token = st.session_state["token"]
    # Example: Post data to FastAPI
    st.subheader("Add New Item")
    input_data = st.text_input("Name: ")
    if st.button("Add Todo"):
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(f"{API_URL}/add_todo", json={"data": input_data}, headers=headers)  # sends as JSON body
        if response.status_code == 200:
            st.success("Todo added successfully!")
            st.json(response.json())
        elif: response.status_code == 401:
            st.warning("Session expired. Login again.")
        elif:
            st.error(f"{response.status_code}: {response.text}")
        else:
            st.warning("Please enter a task before submitting!")
            
    # Example: Fetch data from FastAPI
    if st.button("Display"):
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{API_URL}/get_todo", headers=headers)
        if response.status_code == 200:
            for row in response.json():
                st.write(f"{row['id']} - {row['task']}")
        else:
            st.error(f"{response.status_code}: {response.text}")
