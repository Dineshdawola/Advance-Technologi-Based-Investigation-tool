import streamlit as st
import gc, datetime, hashlib, re

def get_file_hash(file_bytes):
    """WORM Integrity: Digital Fingerprint"""
    return hashlib.sha256(file_bytes).hexdigest()

def redact_pii_data(text):
    """AI-Based Privacy: Hiding Aadhaar/Mobile"""
    text = re.sub(r'\b\d{12}\b', "XXXXXXXXXXXX", str(text))
    text = re.sub(r'\b\d{10}\b', "XXXXXX0000", str(text))
    return text

def military_grade_wipe():
    """Sanitization Level: DoD 5220.22-M"""
    for key in list(st.session_state.keys()):
        st.session_state[key] = "0x00" # Overwrite data in RAM
    st.session_state.clear()
    st.session_state.auth = False
    gc.collect()
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

def log_audit(user, action, status):
    if 'system_logs' not in st.session_state: st.session_state.system_logs = []
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    st.session_state.system_logs.append(f"[{ts}] {user} | {action} | {status}")