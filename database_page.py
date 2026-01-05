import streamlit as st
import pandas as pd
from intelligence_engine import get_handset_details
from tower_analysis_logic import parse_bts_cdr
from logic_gateway import secure_pii_masking

def show_cdr_analysis():
    st.title("🛰️ Enterprise CDR Forensic Lab (v5.0.1)")
    
    uploaded_file = st.file_uploader("Upload CDR/BTS Data", type=['xml'])

    if uploaded_file:
        df = parse_bts_cdr(uploaded_file)
        
        # 1. New Feature: Automatic Handset Identification
        if 'IMEIA' in df.columns:
            st.subheader("📱 Suspect Device Intelligence")
            sample_imei = str(df['IMEIA'].iloc[0])[:8] # First 8 digits
            device_info = get_handset_details(sample_imei)
            st.write(f"**Identified Device:** {device_info}")

        # 2. New Feature: Professional Excel Export (Replacing ClosedXML.dll)
        st.subheader("📊 Export & Reporting")
        if st.button("Generate Professional Forensic Excel"):
            # Using original Python logic for legal Excel creation
            df_masked = df.copy()
            df_masked['CALLINGA'] = df_masked['CALLINGA'].apply(secure_pii_masking)
            df_masked.to_excel("CyberCops_Forensic_Report.xlsx", index=False)
            st.success("✅ Report generated with Cyber Cops Security Protocol.")

        # 3. Data Visualization (Replacing MapCommenFunctions.dll)
        st.subheader("🗺️ Call Mapping & Frequency")
        if 'FIRSTCELLIDA' in df.columns:
            tower_counts = df['FIRSTCELLIDA'].value_counts().head(10)
            st.bar_chart(tower_counts)
            st.info("Analysis: Top towers identified for suspect tracking.")

        st.dataframe(df.head(50))