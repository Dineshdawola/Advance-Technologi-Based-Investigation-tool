import streamlit as st

def apply_enterprise_styles():
    st.markdown("""
        <style>
        /* Anti-Screenshot Protection */
        @media print { body { display: none; } }
        body { 
            -webkit-touch-callout: none; -webkit-user-select: none; 
            -khtml-user-select: none; -moz-user-select: none; 
            -ms-user-select: none; user-select: none;
        }

        /* Sidebar Always Fixed & No Hide Button */
        [data-testid="stSidebarNav"] { pointer-events: none; }
        button[kind="headerNoPadding"] { display: none !important; }
        section[data-testid="stSidebar"] {
            position: fixed !important;
            background: #050505 !important;
            border-right: 2px solid #00f3ff;
            width: 320px !important;
            visibility: visible !important;
        }

        /* Title Positioning */
        .main-header {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            text-align: center;
            z-index: 100;
        }
        </style>
        
        <script>
        // Detection for Screenshots
        document.addEventListener('keyup', (e) => {
            if (e.key == 'PrintScreen' || (e.ctrlKey && e.key == 'p')) {
                navigator.clipboard.writeText('ACCESS BLOCKED');
                alert('SECURITY VIOLATION: Unauthorized screen capture attempt.');
            }
        });
        </script>
    """, unsafe_allow_html=True)