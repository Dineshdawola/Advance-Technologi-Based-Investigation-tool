import streamlit as st
from logic_gateway import validate_access, log_access_attempt

def show_login(version):
    # Animated Glow Title
    st.markdown(f"""
        <style>
        .glow-text {{
            text-align: center;
            color: #fff;
            text-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14, 0 0 30px #39FF14;
            font-family: 'Courier New', Courier, monospace;
        }}
        </style>
        <h1 class='glow-text'>INVESTIGATION TOOL v{version}</h1>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align:center; color:#39FF14;'>CREATED BY CYBER COPS</h3>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1,2,1])
    with col:
        dept = st.selectbox("SELECT DEPARTMENT", ["CDR Dept", "Cyber Cell", "Admin", "Forensic Lab"])
        pwd = st.text_input("V-KEY", type="password", placeholder="Enter Security Key")
        
        st.markdown("<p style='color:#39FF14; font-size:12px; text-align:center;'>● System Status: SECURE | Encryption: AES-256</p>", unsafe_allow_html=True)
        
        # Fixed logic: Only check on button click to avoid constant "Access Denied" alerts
        if st.button("AUTHORIZE SYSTEM"):
            if validate_access(pwd):
                log_access_attempt(dept, "SUCCESS")
                st.session_state.auth = True
                st.rerun()
            elif pwd:
                log_access_attempt(dept, "FAILED")
                st.error("ACCESS DENIED")