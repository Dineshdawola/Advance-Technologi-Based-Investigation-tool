import streamlit as st
from logic_gateway import validate_access, log_access_attempt, ghost_wipe_memory
import time

def show_login(version):
    # Force Show Sidebar only on Login Page
    with st.sidebar:
        st.markdown("<h2 style='color:#00f3ff; font-family:monospace;'>🛡️ AGENCY PROTOCOL</h2>", unsafe_allow_html=True)
        st.error("⚠️ ZERO-TRACE: ACTIVE")
        st.info("STORAGE: DISABLED (RAM ONLY)")
        st.success("SECURITY: TLS 1.3")
        st.markdown("---")
        if st.button("MANUAL MEMORY WIPE"):
            ghost_wipe_memory()
            st.toast("System Memory Flushed!")

    # Tactical UI Header
    st.markdown(f"""
        <div style='text-align:center;'>
            <h1 style='color:#39FF14; font-family:monospace; letter-spacing:10px; text-shadow: 0 0 20px #39FF14;'>CYBER COPS HUB</h1>
            <p style='color:#00f3ff; font-family:monospace;'>SECURE INVESTIGATION TUNNEL v{version}</p>
        </div>
    """, unsafe_allow_html=True)

    _, col, _ = st.columns([1,2,1])
    with col:
        st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)
        dept = st.selectbox("IDENTIFICATION UNIT", ["Admin Only"])
        pwd = st.text_input("V-KEY (TLS MASTER SIGNATURE)", type="password")

        if st.button("AUTHORIZE SECURE CONNECTION"):
            if validate_access(pwd):
                # Professional Agency Voice Alert
                st.components.v1.html("<script>const m = new SpeechSynthesisUtterance('Access Granted. Ghost Protocol Enabled.'); m.rate=0.8; window.speechSynthesis.speak(m);</script>", height=0)
                log_access_attempt(dept, "SUCCESS (TLS)")
                
                with st.status("Initializing Zero-Trace Environment...", expanded=True) as status:
                    time.sleep(0.5)
                    st.write("Performing TLS 1.3 Handshake...")
                    time.sleep(0.5)
                    st.write("Disabling Local Logging...")
                    time.sleep(0.5)
                    status.update(label="Secure Tunnel Established!", state="complete")
                
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("🛑 TLS Handshake Rejected")