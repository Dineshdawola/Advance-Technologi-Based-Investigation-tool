import streamlit as st
def show_logs():
    st.title("🖥️ System Access Logs")
    if 'system_logs' in st.session_state:
        st.code("\n".join(st.session_state.system_logs), language="bash")