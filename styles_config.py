import streamlit as st
def apply_ui_styles():
    st.markdown("""
        <style>
        @media print { body { display: none; } }
        body { -webkit-user-select: none; user-select: none; }
        </style>
    """, unsafe_allow_html=True)