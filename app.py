import streamlit as st
import time
from login_page import show_login
from logic_gateway import military_grade_wipe, log_audit, get_system_ip
from rules_config import get_system_rules

# Session state initialization
if 'auth' not in st.session_state: st.session_state.auth = False
if 'jit_expiry' not in st.session_state: st.session_state.jit_expiry = None

rules = get_system_rules()

if not st.session_state.auth:
    show_login(rules['Version'])
else:
    # JIT Access Monitor (Abhi active hai par IP block nahi karega)
    if st.session_state.jit_expiry and time.time() > st.session_state.jit_expiry:
        military_grade_wipe()
        st.error("⌛ JIT Access Expired. Session Sanitized.")
        st.stop()

    st.sidebar.markdown(f"### 🛰️ GHOST PROTOCOL v{rules['Version']}")
    
    # Audit Logs (Previous logic kept)
    if st.sidebar.checkbox("View Audit Logs"):
        st.code("\n".join(st.session_state.get('system_logs', [])))

    if st.sidebar.button("MILITARY WIPE & EXIT"):
        military_grade_wipe()
        st.rerun()

    st.write("### Investigation Dashboard (Network Shield: On Hold)")