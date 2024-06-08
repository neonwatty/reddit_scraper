import sqlite3
import pandas as pd
from datetime import datetime


def read_all_rows(db_filepath: str="reddit_scraper.db") -> list:
    # Read rows based on input reddit urls
    conn = sqlite3.connect(db_filepath)
    cursor = conn.cursor()
    
    # Execute query
    query = "SELECT * FROM reddit_scraper"
    cursor.execute(query)
    rows = cursor.fetchall()
    processed_rows = []
    for row in rows:
        entry = {}
        entry["reddit_url"] = row[0]        
        entry["timestamp"] = datetime.fromtimestamp(row[1]).strftime("%Y-%m-%d %H:%M:%S")
        entry["total_member_count"] = row[2]
        entry["total_online_count"] = row[3]
        processed_rows.append(entry)
    processed_rows = pd.DataFrame(processed_rows, columns=["reddit_url", "timestamp", "total_member_count", "total_online_count"])
    return processed_rows
    