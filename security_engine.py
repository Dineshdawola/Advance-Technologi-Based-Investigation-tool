import streamlit as st
def apply_enterprise_styles():
    st.markdown("""
        <style>
        .stApp { background: #000; color: #39FF14; }
        section[data-testid="stSidebar"] { border-right: 2px solid #00f3ff; }
        header, footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)