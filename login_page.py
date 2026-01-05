import streamlit as st
from logic_gateway import validate_access, log_access_attempt, secure_data_wipe
import time

def show_login(version):
    # Sidebar always visible logic
    with st.sidebar:
        st.markdown("<h2 style='color:#00f3ff; font-family:monospace;'>🛡️ AGENCY HUB</h2>", unsafe_allow_html=True)
        st.error("⚠️ ZERO-TRACE: ACTIVE")
        st.info("PROTOCOL: TLS v1.3")
        st.markdown("---")
        if st.button("MANUAL MEMORY WIPE"):
            secure_data_wipe()
            st.toast("Memory Flushed!")

    # Tactical UI Header
    st.markdown(f"""
        <div style='text-align:center;'>
            <h1 style='color:#39FF14; font-family:monospace; letter-spacing:10px; text-shadow: 0 0 20px #39FF14;'>CYBER COPS HUB</h1>
            <p style='color:#00f3ff; font-family:monospace;'>SECURE TUNNEL v{version}</p>
        </div>
    """, unsafe_allow_html=True)

    _, col, _ = st.columns([1,2,1])
    with col:
        st.markdown("<br>", unsafe_allow_html=True)
        dept = st.selectbox("IDENTIFICATION", ["Admin Only"])
        pwd = st.text_input("V-KEY (TLS MASTER SIGNATURE)", type="password")

        if st.button("AUTHORIZE TLS CONNECTION"):
            if validate_access(pwd):
                # Professional Agency Voice Alert
                st.components.v1.html("<script>const m = new SpeechSynthesisUtterance('Access Granted. Ghost Mode Active.'); m.rate=0.8; window.speechSynthesis.speak(m);</script>", height=0)
                log_access_attempt(dept, "SUCCESS")
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("🛑 SECURITY ALERT: Unauthorized Access")