import streamlit as st
from logic_gateway import military_grade_wipe, get_file_hash, log_audit, redact_pii_data
import time

def show_database():
    st.title("📂 Forensic Evidence Lab")
    
    # JIT Access Activation
    if st.sidebar.button("Request 30-Min JIT Access"):
        st.session_state.jit_expiry = time.time() + 1800
        st.success("Access Granted for 30 Minutes.")

    uploaded_file = st.file_uploader("Upload Data File", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        file_hash = get_file_hash(uploaded_file.getvalue())
        st.info(f"🛡️ WORM LOCK HASH: {file_hash}")
        
        # PII Redaction Feature
        st.subheader("Data Privacy (PII Masked)")
        st.code(redact_pii_data("Investigation Lead: Rahul, ID: 123456789012"))

        if st.button("DoD SECURE SHRED"):
            military_grade_wipe()
            st.rerun()