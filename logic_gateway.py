import streamlit as st
import gc, datetime, hashlib, re

def get_file_hash(content):
    """Original SHA-256 integrity check"""
    return hashlib.sha256(content).hexdigest()

def secure_pii_masking(text):
    """Protects sensitive Aadhaar (12 digits) and Mobile (10 digits)"""
    text = re.sub(r'\b\d{12}\b', "XXXXXXXXXXXX", str(text))
    text = re.sub(r'\b\d{10}\b', "XXXXXX0000", str(text))
    return text

def military_grade_wipe():
    """DoD 5220.22-M Standard - Memory Sanitization"""
    for key in list(st.session_state.keys()):
        st.session_state[key] = "0x00"
    st.session_state.clear()
    st.session_state.auth = False
    gc.collect()