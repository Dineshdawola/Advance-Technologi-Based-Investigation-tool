import streamlit as st

def apply_security_shield():
    st.markdown("""
        <script>
        document.addEventListener('contextmenu', e => e.preventDefault());
        document.onkeydown = function(e) {
            if(e.keyCode == 123 || (e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 74))) return false;
            if(e.ctrlKey && e.keyCode == 85) return false;
        };
        </script>
    """, unsafe_allow_html=True)

def monitor_screenshot_attempts():
    st.markdown("""
        <script>
        document.addEventListener('keyup', (e) => {
            if (e.key === 'PrintScreen' || (e.ctrlKey && e.key === 'p')) {
                alert('⚠️ SECURITY ALERT: Screenshot Attempt Detected! Activity logged and sent to Cyber Cops Developer.');
            }
        });
        </script>
    """, unsafe_allow_html=True)