import streamlit as st
import openai

# Load API key from Streamlit secrets
openai_client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Function to get AI response
def get_answer(question):
    try:
        response = openai.ChatCompletion.create(
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
