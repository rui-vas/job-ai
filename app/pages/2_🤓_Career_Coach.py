import streamlit as st
from langchain_community.llms import OpenAI

# set page config with nerd face emoji and Career Coach title
st.set_page_config(
    page_title="Career Coach",
    page_icon="🤓",
)

# write title
st.write("# Welcome to Career Coach! 🤓")
openai_api_key = st.sidebar.text_input('OpenAI API Key')


def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))


# Add subtitle single answer
st.subheader("Single Answer")

with st.form('single-answer-form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)

# Add subtitle single answer
st.subheader("Chat")

# Add a chat space where an assistant says hello
with st.chat_message("Assistant"):
    st.write("Hello! I'm your Career Coach. I am here to help you with your career.")
    st.write("What would you like to know?")

# Add a text input
prompt = st.chat_input("You")

if prompt:
    st.write(f"User has sent the following prompt: {prompt}")