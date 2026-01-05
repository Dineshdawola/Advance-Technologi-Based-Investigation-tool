import sqlite3
import pandas as pd
import streamlit as st

def get_handset_details(imei_prefix):
    """Original Logic to fetch handset company/model using first 8 digits of IMEI"""
    conn = sqlite3.connect('E:/CDR Tool/CDR.db')
    query = f"SELECT HCompany, HModel FROM Handsetmasterold WHERE HCode = '{imei_prefix}'"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df if not df.empty else "Unknown Device"

def get_location_by_pincode(pincode):
    """Maps Pincode to City/District for forensic verification"""
    conn = sqlite3.connect('E:/CDR Tool/CDR.db')
    query = f"SELECT City FROM Pincode_db WHERE Pincode = {pincode}"
    res = pd.read_sql_query(query, conn)
    conn.close()
    return res