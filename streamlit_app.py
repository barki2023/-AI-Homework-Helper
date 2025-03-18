import streamlit as st
import requests

# Replace this with your Hugging Face API key
API_KEY = "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"

# Function to get AI response
def get_answer(question):
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.post(
            "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",  
            headers=headers,
            json={"inputs": question}
        )
        
        result = response.json()
        
        # If an error occurs, show it
        if "error" in result:
            return f"Error: {result['error']}"
        
        # Extract generated text from response
        return result[0]['summary_text'] if isinstance(result, list) else "No valid response received."
    
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("AI Homework Helper")
question = st.text_input("Enter your homework question:")

if st.button("Get Answer"):
    answer = get_answer(question)
    st.write(answer)  # Show response
