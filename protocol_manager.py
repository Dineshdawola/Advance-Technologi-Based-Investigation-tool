import streamlit as st

def load_cyber_cops_protocols():
    """Custom Protocols for ms-excel, ms-word & CyberCops Protocol"""
    # manifest.json v1.0.0.10 logic
    st.session_state['manifest_version'] = "1.0.0.10-CC"
    
    # protocols.json origins logic
    st.session_state['allowed_origins'] = [
        "https://onedrive.live.com", 
        "https://sharepoint.com",
        "cybercops://secure-launch"
    ]
    
    return "🛡️ Protocols 1.0.0.10: LOCKED"

def is_protocol_safe(url):
    # Cmd aur powershell ko block karne ka logic
    blocked = ["cmd:", "powershell:", "regedit:"]
    return not any(b in url for b in blocked)