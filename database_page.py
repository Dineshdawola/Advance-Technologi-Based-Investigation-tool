import streamlit as st
from logic_gateway import secure_data_wipe

def show_database():
    st.title("📂 Forensic Investigation Lab")
    st.warning("Privacy Alert: Uploaded data is processed in RAM and erased immediately.")

    uploaded_file = st.file_uploader("Upload CDR/Data File for Analysis", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        st.success("Data loaded in Secure Buffer.")
        
        # Yahan aapka analysis logic aayega
        st.write("File Name:", uploaded_file.name)
        
        # Data ko delete karne ka button
        if st.button("FINISH & ERASE DATA"):
            # Sabhi temporary variables clear karein
            secure_data_wipe(uploaded_file)
            st.success("All data has been wiped from system memory.")
            st.rerun()