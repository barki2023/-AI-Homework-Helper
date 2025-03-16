import streamlit as st
import requests
import os

# Load Hugging Face API Key from environment variable
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Function to get AI response
def get_answer(question):
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.post(
            "https://api-inference.huggingface.co/models/gpt2",
            headers=headers,
            json={"inputs": question}
        )
        return response.json()
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("AI Homework Helper")
question = st.text_input("Enter your homework question:")

if st.button("Get Answer"):
    answer = get_answer(question)
    st.write(answer)
