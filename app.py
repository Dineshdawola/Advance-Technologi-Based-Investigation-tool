import streamlit as st
import time
from login_page import show_login
from logic_gateway import military_grade_wipe, log_audit, get_system_ip
from rules_config import get_system_rules

if 'auth' not in st.session_state: st.session_state.auth = False
if 'jit_expiry' not in st.session_state: st.session_state.jit_expiry = None

rules = get_system_rules()
current_ip = get_system_ip()
ALLOWED_IPS = ["127.0.0.1", "192.168"] # IP Whitelisting

if not st.session_state.auth:
    show_login(rules['Version'])
else:
    # JIT Access Monitor
    if st.session_state.jit_expiry and time.time() > st.session_state.jit_expiry:
        military_grade_wipe()
        st.error("JIT Access Expired. Memory Sanitized.")
        st.stop()

    # Network Security
    if not any(current_ip.startswith(p) for p in ALLOWED_IPS):
        st.error(f"Unauthorized Network: {current_ip}"); st.stop()

    st.sidebar.markdown(f"### 🛰️ GHOST PROTOCOL v{rules['Version']}")
    if st.sidebar.button("MILITARY WIPE & EXIT"):
        military_grade_wipe()
        st.rerun()
    st.write("System Authorized. Monitoring Active.")