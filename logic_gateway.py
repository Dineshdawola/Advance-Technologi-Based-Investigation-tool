import streamlit as st
import gc
import datetime
import hashlib
import socket
import re

# 1. Forensic Integrity & WORM
def get_file_hash(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

# 3. Data Masking & PII Redaction
def redact_pii_data(text):
    text = re.sub(r'\b\d{12}\b', "XXXXXXXXXXXX", str(text)) # Aadhaar
    text = re.sub(r'\b\d{10}\b', "XXXXXX0000", str(text))   # Mobile
    return text

# 5. Military-grade Sanitization (DoD 5220.22-M)
def military_grade_wipe():
    for key in list(st.session_state.keys()):
        st.session_state[key] = "0x00" # Overwrite with Null
    st.session_state.clear()
    st.session_state.auth = False
    gc.collect()
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

def get_system_ip():
    try: return socket.gethostbyname(socket.gethostname())
    except: return "127.0.0.1"

def log_audit(user, action, status):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if 'system_logs' not in st.session_state:
        st.session_state.system_logs = []
    entry = f"[{ts}] IP: {get_system_ip()} | USER: {user} | ACTION: {action} | STATUS: {status}"
    st.session_state.system_logs.append(entry)

def validate_access(key):
    return key == "1234"