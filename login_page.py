import streamlit as st
from logic_gateway import validate_access, log_access_attempt

def show_login(version):
    # CSS aur Voice Script ka integration
    st.markdown(f"""
        <style>
        .glow-text {{
            text-align: center;
            color: #fff;
            text-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14, 0 0 30px #39FF14;
            font-family: 'Courier New', Courier, monospace;
        }}
        /* Cyber Neon Blue Button */
        div.stButton > button:first-child {{
            background-color: #000000;
            color: #00f3ff;
            border: 2px solid #00f3ff;
            border-radius: 5px;
            box-shadow: 0 0 10px #00f3ff;
            width: 100%;
            font-weight: bold;
        }}
        </style>
        
        <script>
        function welcomeVoice() {{
            // Browser ki voice API
            const msg = new SpeechSynthesisUtterance("Access Granted. Welcome Admin.");
            msg.rate = 0.9; 
            window.speechSynthesis.speak(msg);
        }}
        </script>
        
        <h1 class='glow-text'>INVESTIGATION TOOL v{version}</h1>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align:center; color:#39FF14;'>CREATED BY CYBER COPS</h3>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1,2,1])
    with col:
        # Department Selection - 'Admin Only' update
        dept = st.selectbox("SELECT DEPARTMENT", ["Admin Only"]) 
        
        pwd = st.text_input("V-KEY", type="password", placeholder="Enter Security Key")
        
        if st.button("AUTHORIZE SYSTEM"):
            if validate_access(pwd):
                # Voice play karne ke liye invisible HTML component
                st.components.v1.html("<script>welcomeVoice();</script>", height=0)
                log_access_attempt(dept, "SUCCESS")
                st.session_state.auth = True
                st.rerun()
            elif pwd:
                log_access_attempt(dept, "FAILED")
                st.error("ACCESS DENIED")