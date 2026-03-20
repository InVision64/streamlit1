import streamlit as st
import requests
import json

st.title("ToDoList")

# Define the local API URL (replace with your deployed API URL on Render)
API_URL = "https://check1-dun-six.vercel.app/tasks/"

# Streamlit widgets for user input
option = st.selectbox(
    "Select operation",
    ("add", "subtract", "multiply", "divide")
)
x = st.slider("Value of x", 0, 100, 20)
y = st.slider("Value of y", 0, 100, 10)

# Button to trigger the API call
if st.button("Calculate"):
    # Prepare the input data as a dictionary, then dump to JSON string
    inputs = {"tasks": option}
    
    try:
        # Send a POST request to the API
        response = requests.post(url=API_URL, data=json.dumps(inputs))
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            st.success(f"The result is: {result['result']}")
        else:
            st.error(f"API request failed with status code {response.status_code}")
            st.json(response.json())
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while connecting to the API: {e}")

st.caption("Make sure your backend API is running and accessible at the specified URL.")
