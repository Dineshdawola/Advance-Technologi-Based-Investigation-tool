import streamlit as st
from login_page import show_login
from database_page import show_database
from logs_page import show_logs
from security_engine import apply_security_shield, monitor_screenshot_attempts
from styles_config import apply_enterprise_styles
from logic_gateway import validate_access
from rules_config import get_system_rules

# Enterprise Initialization
apply_enterprise_styles()
apply_security_shield()
monitor_screenshot_attempts()

# Fetch rules for versioning
rules = get_system_rules()

if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    # Error Fix: Passing the version string here
    show_login(rules['Version']) 
else:
    st.sidebar.title("🛡️ CYBER COPS HUB")
    st.sidebar.markdown(f"**Security:** {rules['Security']}")
    
    choice = st.sidebar.radio("ENTERPRISE MODULES", ["Investigation Lab", "System Diagnostics"])
    
    if st.sidebar.button("SECURE LOGOUT"):
        st.session_state.auth = False
        st.rerun()

    if choice == "Investigation Lab":
        show_database()
    else:
        show_logs()