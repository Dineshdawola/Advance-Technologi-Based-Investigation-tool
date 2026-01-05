import streamlit as st
import gc
import datetime
import hashlib
import socket
import re

def get_file_hash(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

def redact_pii_data(text):
    text = re.sub(r'\b\d{12}\b', "XXXXXXXXXXXX", str(text))
    text = re.sub(r'\b\d{10}\b', "XXXXXX0000", str(text))
    return text

def military_grade_wipe():
    for key in list(st.session_state.keys()):
        st.session_state[key] = "0x00"
    st.session_state.clear()
    st.session_state.auth = False
    gc.collect()
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_system_ip():
    try: return socket.gethostbyname(socket.gethostname())
    except: return "Mobile Network"

def log_audit(user, action, status):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    if 'system_logs' not in st.session_state:
        st.session_state.system_logs = []
    entry = f"[{ts}] IP: {get_system_ip()} | {user}: {action} ({status})"
    st.session_state.system_logs.append(entry)

def validate_access(key):
    return key == "1234"