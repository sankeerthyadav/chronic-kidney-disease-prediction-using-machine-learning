
import streamlit as st
from about import show_about
from user_instructions import show_instructions
from model import show_model  # Make sure you have created this function in model.py
from medicalinfo import show_medicalinfo

# Set page config
st.set_page_config(page_title="CKD Prediction App", layout="centered")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About The Project", "User Instructions", "Medical Reference", "Model"])

# Conditional rendering
if page == "About The Project":
    show_about()

elif page == "User Instructions":
    show_instructions()

elif page == "Medical Reference":
    show_medicalinfo()

elif page == "Model":
    show_model()
