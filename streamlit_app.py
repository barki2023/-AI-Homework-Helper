import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Streamlit UI
st.title("AI Homework Helper 📚")

st.write("Choose a subject:")
subject = st.selectbox("Choose a subject:", ["Math", "Science", "History", "English"])

st.write("Enter your homework question:")
user_input = st.text_area("Enter your homework question:")

if st.button("Get Answer"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use the latest available model
                messages=[{"role": "system", "content": "You are a helpful AI tutor."},
                          {"role": "user", "content": f"Subject: {subject}\nQuestion: {user_input}"}]
            )
            answer = response["choices"][0]["message"]["content"]
            st.success("Answer:")
            st.write(answer)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
