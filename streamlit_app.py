import streamlit as st
import requests
import os

# Get API key from environment variable
API_KEY = os.getenv("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")  

if not API_KEY:
    st.error("API key not found. Set 'HUGGINGFACE_API_KEY' in your environment.")

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
        return {"error": str(e)}

# Streamlit UI
st.title("AI Homework Helper")
question = st.text_input("Enter your homework question:")

if st.button("Get Answer"):
    answer = get_answer(question)
    st.json(answer)  # Show response as JSON for debugging
