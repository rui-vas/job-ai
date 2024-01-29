import streamlit as st

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

# Add a title
st.title("My Profile")

# Add a form to submit your name and email address
with st.form("name_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Your name and email address have been submitted!")

# Add a form to submit all the links to your social media profiles
with st.form("social_form"):
    linkedin = st.text_input("LinkedIn")
    github = st.text_input("GitHub")
    twitter = st.text_input("Twitter")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Your social media profiles have been submitted!")

# Add a form to submit a PDF file of your CV
with st.form("cv_form"):
    cv = st.file_uploader("Upload your CV", type="pdf")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Your CV has been submitted!")
