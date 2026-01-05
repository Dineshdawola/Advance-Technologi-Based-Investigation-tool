import streamlit as st
from login_page import show_login
from logic_gateway import secure_data_wipe

# 1. Initialize Session State (Fixes AttributeError)
if 'auth' not in st.session_state:
    st.session_state.auth = False

# Software Rules
rules = {"Version": "5.0.1"}

# 2. Security & Navigation Logic
if not st.session_state.auth:
    show_login(rules['Version'])
else:
    # Sidebar Ghost Protocol Features
    st.sidebar.markdown("### 🛰️ GHOST PROTOCOL")
    if st.sidebar.button("EXIT & WIPE SYSTEM"):
        secure_data_wipe()
        st.session_state.auth = False
        st.rerun()
    
    st.success("You are now in a Secure Investigation Tunnel.")
    # Agle modules yahan add honge