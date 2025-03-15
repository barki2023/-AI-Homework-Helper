import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Homework Helper 📚🤖")

subject = st.selectbox("Choose a subject:", ["Math", "Science", "History", "English"])
question = st.text_area("Enter your homework question:")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question!")
    else:
        with st.spinner("Thinking... 🤔"):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Answer this {subject} question: {question}"}]
            )
            st.success(response["choices"][0]["message"]["content"])
