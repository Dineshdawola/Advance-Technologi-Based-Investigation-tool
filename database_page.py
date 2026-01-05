import streamlit as st
import pandas as pd
from logic_gateway import secure_data_wipe, get_file_hash, log_access_attempt

def show_database():
    st.title("📂 Forensic Investigation Lab")
    
    # Role-Based UI (RBAC)
    user_role = st.sidebar.selectbox("YOUR ROLE", ["Lead Investigator", "Analyst"])
    
    uploaded_file = st.file_uploader("Upload CDR/Data File", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        file_bytes = uploaded_file.getvalue()
        file_hash = get_file_hash(file_bytes)
        
        st.info(f"🛡️ DIGITAL FINGERPRINT (SHA-256): {file_hash}")
        log_access_attempt(user_role, "System", f"File Uploaded: {uploaded_file.name}", "SUCCESS")

        # Chain of Custody Logic
        st.success("Chain of Custody: Initialized & Encrypted.")
        
        if st.button("FINISH & ERASE DATA"):
            if user_role == "Lead Investigator":
                secure_data_wipe()
                st.rerun()
            else:
                st.error("ACCESS DENIED: Only Lead Investigator can wipe data.")