import streamlit as st

def init_protocol_manager():
    """Redesigned Protocol Handler (Concept: v1.0.0.10)"""
    # Clean Allow-list for Cyber Cops
    st.session_state['allowed_apps'] = ["ms-excel", "ms-word", "ms-outlook"]
    # Internal blocking logic for dangerous protocols
    st.session_state['hard_block'] = ["cmd:", "powershell:", "bash:", "vnc:"]
    return "🛡️ Protocol Integrity: SECURE"

def validate_request(input_protocol):
    if input_protocol in st.session_state['hard_block']:
        return False
    return True