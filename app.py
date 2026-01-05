import streamlit as st
from login_page import show_login
from database_page import show_cdr_analysis
from virtual_storage_logic import init_virtual_safe_mount
from automation_engine import initialize_automation_engine
from cyber_engine_logic import init_isolated_runtime

# Multi-Layer Startup
init_virtual_safe_mount()     # Replaces CBFS Pro dependencies
init_isolated_runtime()      # Replaces WebView2 manual dependencies
initialize_automation_engine() # Replaces Selenium-manager manual logic

if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    show_login("5.0.1")
else:
    page = st.sidebar.selectbox("Navigate", ["Dashboard", "CDR Analysis (Page 4)", "System Logs"])
    
    if page == "CDR Analysis (Page 4)":
        show_cdr_analysis()