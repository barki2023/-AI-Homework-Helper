import streamlit as st
import openai

# Set API Key directly (replace with your actual API key)
openai.api_key = "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"
# Function to get AI response
def get_answer(question):
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("AI Homework Helper")
question = st.text_input("Enter your homework question:")

if st.button("Get Answer"):
    answer = get_answer(question)
    st.write(answer)
