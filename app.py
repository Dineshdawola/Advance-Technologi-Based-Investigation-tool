import streamlit as st
from login_page import show_login
from logic_gateway import secure_data_wipe
from rules_config import get_system_rules

if 'auth' not in st.session_state:
    st.session_state.auth = False
if 'mfa_verified' not in st.session_state:
    st.session_state.mfa_verified = False

rules = get_system_rules()

if not st.session_state.auth:
    show_login(rules['Version'])
else:
    # 2. Access Control: MFA Step
    if not st.session_state.mfa_verified:
        st.warning("🛡️ SECOND LAYER AUTHENTICATION REQUIRED")
        otp = st.text_input("Enter Agency OTP (Sent to registered device)", type="password")
        if st.button("VERIFY IDENTITY"):
            if otp == "0000": # Demo OTP
                st.session_state.mfa_verified = True
                st.rerun()
            else:
                st.error("Invalid Token")
    else:
        # Main Dashboard
        st.sidebar.markdown(f"### 🛰️ GHOST PROTOCOL v{rules['Version']}")
        # 3. Audit Logs View
        if st.sidebar.checkbox("View Detailed Audit Logs"):
            if 'system_logs' in st.session_state:
                st.code("\n".join(st.session_state.system_logs))

        if st.sidebar.button("EXIT & WIPE SYSTEM"):
            secure_data_wipe()
            st.rerun()