import streamlit as st

def show_database():
    st.title("📂 Forensic Database")
    st.info("Status: Encrypted and Secure")
    
    # Placeholder for new tools as requested
    st.subheader("Active Modules")
    cols = st.columns(2)
    cols[0].button("Analyze CDR Records")
    cols[1].button("Search Mobile Database")