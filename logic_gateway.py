import datetime

def validate_access(key):
    return key == "1234"

def log_access_attempt(dept, status):
    # Yeh logs ko session state mein temporary save karega
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] DEPT: {dept} | STATUS: {status}"
    
    if 'system_logs' not in st.session_state:
        st.session_state.system_logs = []
    st.session_state.system_logs.append(log_entry)