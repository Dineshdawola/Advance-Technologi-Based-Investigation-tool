import streamlit as st

def initialize_protocol_handler():
    """AutoLaunch Protocol Guard v1.0.0.10 - LOCKED"""
    # Allow-list from your protocols.json
    st.session_state['allowed_apps'] = ["ms-word", "ms-excel", "ms-powerpoint"]
    # Block-list for high-security investigation
    st.session_state['blocked_commands'] = ["cmd:", "powershell:", "regedit:"]
    
    return "🛡️ Protocol Guard: LOCKED"

def validate_protocol(protocol):
    if protocol in st.session_state['blocked_commands']:
        return "BLOCK", "🚨 Attempted Malicious Command Execution!"
    return "ALLOW", "Safe Connection"