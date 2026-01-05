import streamlit as st
from logic_gateway import validate_access, log_access_attempt
import time

def show_login(version):
    # Sidebar ko hamesha dikhane ke liye permanent content
    with st.sidebar:
        st.markdown("<h2 style='color:#00f3ff; font-family:monospace;'>🛡️ AGENCY ACCESS</h2>", unsafe_allow_html=True)
        st.divider()
        st.write("● **UNIT:** Cyber Cops India")
        st.write("● **SEC:** TLS 1.3 Active")
        st.write("● **ENC:** AES-256 GCM")
        st.markdown("---")
        # Cursor Motion Visual
        st.markdown("""
            <div style='border:1px solid #39FF14; padding:10px; border-radius:5px; background:rgba(0,0,0,0.5);'>
                <p style='color:#39FF14; font-size:11px; font-family:monospace;'>
                [LIVE DATA FLOW]<br>
                > SYNC: ACTIVE<br>
                > TRACE: ENABLED
                </p>
            </div>
        """, unsafe_allow_html=True)

    # Main Interface UI
    st.markdown(f"""
        <div style='text-align:center;'>
            <h1 style='color:#39FF14; font-family:monospace; letter-spacing:8px; text-shadow: 0 0 20px #39FF14;'>CYBER COPS HUB</h1>
            <p style='color:#00f3ff; font-family:monospace;'>INVESTIGATION INTERFACE v{version}</p>
        </div>
    """, unsafe_allow_html=True)

    _, col, _ = st.columns([1,2,1])
    with col:
        st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)
        dept = st.selectbox("IDENTIFICATION", ["Admin Only"])
        pwd = st.text_input("V-KEY (Biometric Signature)", type="password", placeholder="Enter Agency Credentials...")

        if st.button("AUTHORIZE TLS CONNECTION"):
            if validate_access(pwd):
                # Professional Agency Voice Alert
                st.components.v1.html("<script>const m = new SpeechSynthesisUtterance('Access Granted. Welcome Agent.'); m.rate=0.8; window.speechSynthesis.speak(m);</script>", height=0)
                log_access_attempt(dept, "SUCCESS (TLS 1.3)")
                
                with st.spinner("Decrypting Agency Database..."):
                    time.sleep(1.5)
                st.session_state.auth = True
                st.rerun()
            elif pwd:
                log_access_attempt(dept, "FAILED (INTRUSION)")
                st.error("🛑 SECURITY ALERT: Unauthorized Signature Detected")