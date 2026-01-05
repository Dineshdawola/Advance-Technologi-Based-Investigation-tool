import streamlit as st

def apply_enterprise_styles():
    st.markdown("""
        <style>
        /* Agency Dark Theme */
        .stApp {
            background: radial-gradient(circle at center, #011111 0%, #000000 100%);
        }
        
        /* Always Show Sidebar on Main Page */
        section[data-testid="stSidebar"] {
            position: fixed !important;
            visibility: visible !important;
            background: #050505 !important;
            border-right: 1px solid #00f3ff;
            box-shadow: 5px 0 20px rgba(0, 243, 255, 0.1);
        }
        
        /* Cursor move hone par sidebar highlight */
        section[data-testid="stSidebar"]:hover {
            border-right: 2px solid #39FF14;
        }

        header, footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)