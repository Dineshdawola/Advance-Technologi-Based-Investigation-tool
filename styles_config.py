import streamlit as st

def apply_enterprise_styles():
    st.markdown("""
        <style>
        /* India's Best Agency Dark Theme */
        .stApp {
            background: radial-gradient(circle at center, #011111 0%, #000000 100%) !important;
        }

        /* Sidebar Always Fixed & Professional Glow */
        section[data-testid="stSidebar"] {
            position: fixed !important;
            height: 100vh !important;
            width: 300px !important;
            background: #050505 !important;
            border-right: 2px solid #00f3ff;
            z-index: 1000;
        }

        section[data-testid="stSidebar"]:hover {
            border-right: 2px solid #39FF14;
            box-shadow: 5px 0 25px rgba(57, 255, 20, 0.2);
        }

        header, footer, #MainMenu {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)