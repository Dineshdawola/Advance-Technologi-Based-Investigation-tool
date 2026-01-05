import streamlit as st
from logic_gateway import validate_access, log_access_attempt
import time

def show_login(version):
    # Advanced CSS for Command Center Look
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
        
        .main-title {{
            text-align: center;
            color: #39FF14;
            font-family: 'Orbitron', sans-serif;
            text-shadow: 0 0 15px #39FF14;
            letter-spacing: 5px;
            margin-bottom: 0px;
        }}
        
        .digital-clock {{
            text-align: center;
            color: #00f3ff;
            font-family: 'Courier New', monospace;
            font-size: 20px;
            margin-top: -10px;
            margin-bottom: 20px;
        }}

        /* Scanning Line Animation */
        .scan-line {{
            width: 100%;
            height: 2px;
            background: #39FF14;
            box-shadow: 0 0 10px #39FF14;
            position: relative;
            animation: scan 3s linear infinite;
        }}
        @keyframes scan {{
            0% {{ top: 0px; opacity: 0; }}
            50% {{ opacity: 1; }}
            100% {{ top: 200px; opacity: 0; }}
        }}

        /* Neon Input Box */
        .stTextInput > div > div > input {{
            background-color: rgba(0, 0, 0, 0.7) !important;
            color: #00f3ff !important;
            border: 1px solid #00f3ff !important;
            box-shadow: 0 0 5px #00f3ff;
        }}
        </style>
        
        <script>
        function welcomeVoice() {{
            const msg = new SpeechSynthesisUtterance("Access Granted. Welcome Admin.");
            msg.rate = 0.9;
            window.speechSynthesis.speak(msg);
        }}
        </script>
        
        <h1 class='main-title'>CYBER COPS COMMAND v{version}</h1>
        <div class='digital-clock' id='clock'>SYSTEM TIME: {time.strftime('%H:%M:%S')}</div>
        <div class='scan-line'></div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("### 🛡️ SYSTEM METRICS")
    st.sidebar.write("● CPU: OPTIMAL")
    st.sidebar.write("● ENCRYPTION: ACTIVE")
    st.sidebar.write("● FIREWALL: PROTECTED")

    _, col, _ = st.columns([1,2,1])
    with col:
        st.markdown("<br>", unsafe_allow_html=True)
        dept = st.selectbox("IDENTIFICATION UNIT", ["Admin Only"])
        pwd = st.text_input("V-KEY (Biometric Bypass)", type="password", placeholder="Waiting for Security Key...")
        
        st.info("⚠️ NOTICE: All access attempts are recorded by Cyber Cops Security Engine.")
        
        if st.button("EXECUTE AUTHORIZATION"):
            if validate_access(pwd):
                st.components.v1.html("<script>welcomeVoice();</script>", height=0)
                log_access_attempt(dept, "SUCCESS")
                with st.spinner("Decrypting System Layers..."):
                    time.sleep(1)
                st.session_state.auth = True
                st.rerun()
            elif pwd:
                log_access_attempt(dept, "FAILED")
                st.error("❌ CRITICAL ERROR: UNAUTHORIZED V-KEY")