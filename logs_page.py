import streamlit as st

def show_logs():
    st.title("🖥️ System Access Logs")
    
    # Check agar logs hain ya nahi
    if 'system_logs' in st.session_state and st.session_state.system_logs:
        # Logs dikhane ke liye terminal box
        log_text = "\n".join(reversed(st.session_state.system_logs))
        st.code(log_text, language="bash")
        
        # Naya feature: Logs clear karne ka button
        if st.button("🗑️ CLEAR ALL LOGS"):
            st.session_state.system_logs = []
            st.success("Logs successfully cleared.")
            st.rerun()
    else:
        st.info("No recent access attempts detected.")
    
    st.divider()
    st.code("Security Shield: ACTIVE\nIntruder Monitoring: ON", language="bash")