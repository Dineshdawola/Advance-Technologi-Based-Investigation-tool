import streamlit as st
from logic_gateway import validate_access

def show_login(version): # Version argument added here
    st.markdown(f"<h1 style='text-align:center; color:white;'>INVESTIGATION TOOL v{version}</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#39FF14;'>CREATED BY CYBER COPS</h3>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1,2,1])
    with col:
        pwd = st.text_input("V-KEY", type="password", placeholder="Enter Security Key")
        if st.button("AUTHORIZE SYSTEM"):
            if validate_access(pwd):
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("ACCESS DENIED")