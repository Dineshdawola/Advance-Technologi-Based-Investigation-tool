import streamlit as st
import gc # Garbage Collector for memory cleaning

def validate_access(key):
    return key == "1234"

def ghost_wipe_memory():
    """System se saare temporary data aur session memory ko delete karta hai"""
    for key in list(st.session_state.keys()):
        if key != 'auth': # Sirf login status bachega
            del st.session_state[key]
    gc.collect() # RAM se data permanently flush karne ke liye

def log_access_attempt(dept, status):
    # Logs hamesha temporary session mein rahenge, file mein nahi save honge
    import datetime
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    entry = f"[{ts}] {dept} | {status} | TLS 1.3"
    
    if 'system_logs' not in st.session_state:
        st.session_state.system_logs = []
    st.session_state.system_logs.append(entry)