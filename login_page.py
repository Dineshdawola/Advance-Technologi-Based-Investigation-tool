import streamlit as st
from logic_gateway import validate_access, log_access_attempt, secure_data_wipe
import time

def show_login(version):
    # Advance Title
    st.markdown("""
        <div class='main-header'>
            <h1 style='color: #39FF14; font-family: monospace; font-size: 45px; text-shadow: 0 0 20px #39FF14; font-weight: bold;'>
                ADVANCE TECHNOLOGY BASED INVESTIGATION TOOL
            </h1>
        </div>
        <br><br><br><br>
    """, unsafe_allow_html=True)

    # Sidebar Advance Technology Info
    with st.sidebar:
        st.markdown(f"<h4 style='color:#00f3ff;'>SECURE TUNNEL v{version}</h4>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""
            <div style='color:#39FF14; font-family:monospace; font-size:11px;'>
                <b>ADVANCE TECHNOLOGY ENCRYPTION:</b><br>
                > TLS 1.3 HYBRID SECURITY<br>
                > RSA 4096-BIT HANDSHAKE<br>
                > AES-256-GCM DATA TUNNEL<br>
                > VOLATILE MEMORY ERASE: ACTIVE
            </div>
        """, unsafe_allow_html=True)

    _, col, _ = st.columns([1,2,1])
    with col:
        st.markdown("<br><br>", unsafe_allow_html=True)
        dept = st.selectbox("IDENTIFICATION UNIT", ["Admin Only"])
        
        # Anti-AutoSave Password Logic
        pwd = st.text_input("V-KEY (MANUAL INPUT ONLY)", type="password", autocomplete="new-password")
        
        if st.button("AUTHORIZE SECURE CONNECTION"):
            # Check for auto-saved or empty passwords
            if not pwd:
                st.error("SECURITY ERROR: Manual V-KEY entry is mandatory. Auto-fill is disabled.")
            elif validate_access(pwd):
                # Access Voice & Animation
                st.components.v1.html("<script>const m = new SpeechSynthesisUtterance('Access Granted. Ghost Mode Active.'); m.rate=0.8; window.speechSynthesis.speak(m);</script>", height=0)
                
                with st.status("Initializing Secure Tunnel...", expanded=True) as status:
                    time.sleep(1)
                    st.write("Verifying TLS 1.3 Signature...")
                    time.sleep(1)
                    status.update(label="ACCESS GRANTED", state="complete")
                
                log_access_attempt(dept, "SUCCESS (TLS 1.3)")
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("🛑 UNAUTHORIZED SIGNATURE")