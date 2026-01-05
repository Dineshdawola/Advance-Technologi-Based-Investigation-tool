import streamlit as st
from logic_gateway import military_grade_wipe, get_file_hash, log_audit, redact_pii_data
import time

def show_database():
    st.title("📂 Forensic Evidence Vault")
    
    if st.sidebar.button("Activate JIT Access (30m)"):
        st.session_state.jit_expiry = time.time() + 1800
        st.success("JIT Timer Started.")

    uploaded_file = st.file_uploader("Upload Data (WORM Secure)", type=['csv', 'xlsx'])
    if uploaded_file:
        f_hash = get_file_hash(uploaded_file.getvalue())
        st.info(f"🛡️ EVIDENCE LOCK HASH: {f_hash}")
        
        # PII Redaction Feature
        st.subheader("Data Privacy (PII Masked)")
        st.code(redact_pii_data("Suspect ID: 123456789012, Phone: 9876543210"))

        if st.button("MILITARY WIPE DATA"):
            military_grade_wipe()
            st.rerun()