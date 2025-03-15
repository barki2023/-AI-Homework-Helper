import streamlit as st
import openai
import os

# Load OpenAI API key from Streamlit secrets or environment variable
openai.api_key = st.secrets["openai"]["api_key"] if "openai" in st.secrets else os.getenv("OPENAI_API_KEY")

# Streamlit app title
st.title("AI Homework Helper 📚")

# Dropdown for subject selection
subject = st.selectbox("Choose a subject:", ["Math", "Science", "History", "English"])

# Input field for user question
question = st.text_area("Enter your homework question:")

# Button to get AI-generated answer
if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a valid question.")
    elif not openai.api_key:
        st.error("API key is missing. Please configure it in Streamlit secrets or as an environment variable.")
    else:
        try:
            # Use the updated OpenAI API method
            client = openai.OpenAI()
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": f"Subject: {subject}\nQuestion: {question}"}]
            )
            
            # Display the AI-generated answer
            answer = response.choices[0].message.content
            st.success("Here’s the answer:")
            st.write(answer)

        except openai.OpenAIError as e:
            st.error(f"Error: {e}")

