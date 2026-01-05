import streamlit as st

def apply_enterprise_styles():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.9), rgba(0,0,0,0.9)), 
                        url("https://images.unsplash.com/photo-1550751827-4bd374c3f58b");
            background-size: cover;
        }
        header, footer, #MainMenu {visibility: hidden;}
        .stButton>button {border: 1px solid #39FF14; color: #39FF14; background: black;}
        </style>
    """, unsafe_allow_html=True)