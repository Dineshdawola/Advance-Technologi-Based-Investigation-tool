import streamlit as st

def apply_enterprise_styles():
    st.markdown("""
        <style>
        /* India's Best Agency Intelligence Theme */
        .stApp {
            background: radial-gradient(circle at center, #001a1a 0%, #000000 100%);
            background-attachment: fixed;
        }

        /* Fixed Sidebar for Main Page Only */
        section[data-testid="stSidebar"] {
            position: fixed !important;
            height: 100vh !important;
            width: 280px !important;
            background: rgba(10, 10, 10, 0.95) !important;
            border-right: 2px solid #00f3ff;
            box-shadow: 5px 0 30px rgba(0, 243, 255, 0.2);
            z-index: 1000;
        }

        /* Cyber Cursor Interaction */
        section[data-testid="stSidebar"]:hover {
            border-right: 2px solid #39FF14;
            box-shadow: 5px 0 40px rgba(57, 255, 20, 0.3);
        }

        /* Hide elements for professional look */
        header, footer {visibility: hidden;}
        
        /* Tactical Buttons */
        div.stButton > button {
            border: 1px solid #00f3ff !important;
            background: transparent !important;
            color: #00f3ff !important;
            font-family: 'Courier New', monospace;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        </style>
    """, unsafe_allow_html=True)