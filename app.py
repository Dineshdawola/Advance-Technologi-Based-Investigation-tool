import streamlit as st
from login_page import show_login
from infrastructure_manager import initialize_infrastructure # New Link
from security_audit_engine import initialize_certificate_security
from protocol_handler import initialize_protocol_security
from logic_gateway import military_grade_wipe, log_audit
from rules_config import get_system_rules

# Start All Security Engines
infra_status = initialize_infrastructure()
cert_status = initialize_certificate_security()
proto_status = initialize_protocol_security()
rules = get_system_rules()

if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    show_login(rules['Version'])
else:
    # Sidebar: Multi-Layer Security Dashboard
    st.sidebar.markdown("### 🛡️ SYSTEM SHIELD")
    st.sidebar.success(infra_status)   # WebView2 v10.34
    st.sidebar.info(cert_status)      # CRLSet 2025
    st.sidebar.warning(proto_status)  # Protocols v1.0.10
    
    st.sidebar.markdown("---")
    if st.sidebar.button("FORCE WIPE & SHUTDOWN"):
        military_grade_wipe()
        st.rerun()

    st.write("### Investigation Portal (Enterprise Secure Mode)")