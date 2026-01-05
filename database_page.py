import streamlit as st
from logic_gateway import secure_data_wipe, get_file_hash, log_audit

def show_database():
    st.title("📂 Forensic Investigation Lab")
    
    # Role-Based Access Control (RBAC)
    role = st.sidebar.selectbox("Access Level", ["Lead Investigator", "Field Agent"])
    
    uploaded_file = st.file_uploader("Upload Evidence (CDR/XLSX)", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        # Digital Fingerprinting logic
        file_bytes = uploaded_file.getvalue()
        f_hash = get_file_hash(file_bytes)
        
        st.info(f"🛡️ EVIDENCE HASH (SHA-256): {f_hash}")
        log_audit(role, f"Uploaded: {uploaded_file.name}", "HASH VERIFIED")

        if st.button("FINISH & ERASE DATA"):
            if role == "Lead Investigator":
                secure_data_wipe()
                st.success("Chain of Custody Maintained. Memory Wiped.")
                st.rerun()
            else:
                st.error("SECURITY ALERT: Unauthorized wipe attempt logged.")
                log_audit(role, "Wipe Attempt", "DENIED")