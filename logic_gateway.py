import streamlit as st
import datetime
import gc

def validate_access(key):
    # Agency Master Key
    return key == "1234"

def secure_data_wipe():
    """System memory (RAM) se saare temporary records ko turant erase karne ke liye"""
    for key in list(st.session_state.keys()):
        if key != 'auth': 
            del st.session_state[key]
    gc.collect() # Garbage collector memory flush karega

def log_access_attempt(dept, status):
    # Logs hamesha temporary rahenge, disk par save nahi honge
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    entry = f"[{timestamp}] {dept} | {status} | TLS 1.3"
    
    if 'system_logs' not in st.session_state:
        st.session_state.system_logs = []
    st.session_state.system_logs.append(entry)