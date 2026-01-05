import streamlit as st
import gc
import datetime
import hashlib

def get_file_hash(file_bytes):
    """Digital Fingerprinting (SHA-256) for Data Integrity"""
    return hashlib.sha256(file_bytes).hexdigest()

def apply_data_masking(text):
    """Data Masking for Privacy"""
    if len(text) <= 4: return "****"
    return text[:2] + "*" * (len(text)-4) + text[-2:]

def validate_access(key):
    # Agency Master Key (Future: MFA integration)
    return key == "1234"

def secure_data_wipe(file_obj=None):
    st.session_state.clear()
    st.session_state.auth = False
    gc.collect()

def log_access_attempt(dept, user, action, status):
    """Detailed Audit Logs for Traceability"""
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if 'system_logs' not in st.session_state:
        st.session_state.system_logs = []
    log_entry = f"[{ts}] USER: {user} | ACTION: {action} | STATUS: {status}"
    st.session_state.system_logs.append(log_entry)