import streamlit as st

def show_logs():
    st.title("🖥️ System Access Logs")
    
    if 'system_logs' in st.session_state and st.session_state.system_logs:
        # Show logs in a terminal-style box
        log_text = "\n".join(reversed(st.session_state.system_logs))
        st.code(log_text, language="bash")
    else:
        st.info("No recent access attempts detected.")
    
    st.divider()
    st.code("Security Shield: ACTIVE\nIntruder Monitoring: ON", language="bash")