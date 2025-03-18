import streamlit as st
import requests
import json

# Replace this with your Hugging Face API key
API_KEY = "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"

# Function to get AI response
def get_answer(question):
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.post(
            "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct",  
            headers=headers,
            json={"inputs": question}
        )
        
        # Check if response is empty
        if response.status_code != 200:
            return f"Error: API returned status code {response.status_code}"

        result = response.json()
        
        # If an error occurs, show it
        if "error" in result:
            return f"Error: {result['error']}"

        # Extract generated text from response
        return result[0]['generated_text'] if isinstance(result, list) else "No valid response received."
    
    except json.decoder.JSONDecodeError:
        return "Error: Empty response from API."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("AI Homework Helper")
question = st.text_input("Enter your homework question:")

if st.button("Get Answer"):
    answer = get_answer(question)
    st.write(answer)  # Show response
