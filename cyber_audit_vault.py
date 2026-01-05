import sqlite3
import datetime

def log_investigation_activity(activity_name, activity_type):
    """Professional Audit Logging - Replacing cbfslogs.db logic"""
    conn = sqlite3.connect('E:/CDR Tool/cyber_cops_audit.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS AuditTrail 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       timestamp DATETIME, 
                       activity TEXT, 
                       type TEXT)''')
    
    cursor.execute("INSERT INTO AuditTrail (timestamp, activity, type) VALUES (?, ?, ?)", 
                   (datetime.datetime.now(), activity_name, activity_type))
    
    conn.commit()
    conn.close()