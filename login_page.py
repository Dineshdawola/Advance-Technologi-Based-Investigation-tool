import streamlit as st
from logic_gateway import validate_access, log_audit
import time

def show_login(version):
    st.markdown("<h1 style='text-align:center; color:#39FF14;'>ADVANCE TECHNOLOGY INVESTIGATION TOOL</h1>", unsafe_allow_html=True)
    
    with st.sidebar:
        st.markdown(f"<h4>SECURE TUNNEL v{version}</h4>", unsafe_allow_html=True)
        st.info("VOLATILE MEMORY ERASE: ACTIVE")

    _, col, _ = st.columns([1,2,1])
    with col:
        pwd = st.text_input("V-KEY (MANUAL INPUT ONLY)", type="password")
        if st.button("AUTHORIZE"):
            if validate_access(pwd):
                log_audit("Admin", "Login Attempt", "SUCCESS")
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("INVALID V-KEY")