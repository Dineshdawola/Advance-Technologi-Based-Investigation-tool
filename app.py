import streamlit as st
from login_page import show_login
from logic_gateway import secure_data_wipe, log_audit
from rules_config import get_system_rules

if 'auth' not in st.session_state:
    st.session_state.auth = False
if 'mfa_verified' not in st.session_state:
    st.session_state.mfa_verified = False

rules = get_system_rules()

if not st.session_state.auth:
    show_login(rules['Version'])
else:
    # Multi-Factor Authentication Layer
    if not st.session_state.mfa_verified:
        st.warning("🛡️ SECOND LAYER AUTHENTICATION REQUIRED")
        otp = st.text_input("Enter Hardware Token / OTP", type="password")
        if st.button("VERIFY IDENTITY"):
            if otp == "0000": # Agency Demo Token
                st.session_state.mfa_verified = True
                log_audit("System", "MFA Verification", "SUCCESS")
                st.rerun()
            else:
                log_audit("Unknown", "MFA Failure", "CRITICAL ALERT")
                st.error("Invalid Token")
    else:
        # Main Software Interface
        st.sidebar.markdown(f"### 🛰️ GHOST PROTOCOL v{rules['Version']}")
        
        # Intrusion Detection System (Audit View)
        if st.sidebar.checkbox("Show Intrusion Logs"):
             st.code("\n".join(st.session_state.get('system_logs', [])), language="bash")

        if st.sidebar.button("EXIT & WIPE SYSTEM"):
            secure_data_wipe()
            st.rerun()