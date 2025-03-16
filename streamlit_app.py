import streamlit as st
import openai

# Set API Key directly
openai.api_key = "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"

# Function to get AI response
def get_answer(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("AI Homework Helper")
question = st.text_input("Enter your homework question:")

if st.button("Get Answer"):
    answer = get_answer(question)
    st.write(answer)
