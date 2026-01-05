import streamlit as st
from logic_gateway import military_grade_wipe, get_file_hash, log_audit, redact_pii_data
import time

def show_database():
    st.title("📂 Forensic WORM Lab")
    
    if st.sidebar.button("Enable 30-Min JIT Access"):
        st.session_state.jit_expiry = time.time() + 1800
        st.success("JIT Access Granted.")

    uploaded_file = st.file_uploader("Upload Evidence", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        file_hash = get_file_hash(uploaded_file.getvalue())
        st.info(f"🛡️ WORM LOCK HASH: {file_hash}")
        log_audit("Investigator", f"Uploaded {uploaded_file.name}", "SUCCESS")
        
        # PII Redacted Preview
        st.subheader("Sanitized Data Preview")
        st.code(redact_pii_data("Sensitive Entry: 123456789012"))

        if st.button("DoD SECURE SHRED"):
            military_grade_wipe()
            st.rerun()