import streamlit as st
import requests
import json

API_KEY = "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"

def get_answer(question):
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.post(
            "https://api-inference.huggingface.co/models/google/gemini-pro",  
            headers=headers,
            json={"inputs": question}
        )

        if response.status_code != 200:
            return f"Error: API returned status code {response.status_code}"

        result = response.json()

        if "error" in result:
            return f"Error: {result['error']}"

        return result[0].get('generated_text', "No valid response received.")

    except json.decoder.JSONDecodeError:  # ✅ Fix: Added colon
        return "Error: Invalid JSON response."

st.title("AI Homework Helper")
question = st.text_input("Enter your homework question:")
if st.button("Get Answer"):
    answer = get_answer(question)
    st.write(answer)
