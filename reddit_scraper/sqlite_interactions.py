import sqlite3


def read_rows(reddit_urls: list, db_filepath: str="reddit_scraper.db") -> list:
    # Read rows based on input reddit urls
    conn = sqlite3.connect(db_filepath)
    cursor = conn.cursor()
    
    # Execute query
    qs = ", ".join("?" * len(reddit_urls))
    query = f"SELECT * FROM reddit_scraper WHERE reddit_url IN ({qs})"
    cursor.execute(query, reddit_urls)
    rows = cursor.fetchall()
    return rows
    

def put_rows(rows_to_write: list, db_filepath: str="reddit_scraper.db") -> None:
    # Connect and create cursor
    conn = sqlite3.connect(db_filepath)
    cursor = conn.cursor()

    # Setup query
    query = "INSERT INTO reddit_scraper (reddit_url, timestamp, total_member_count, total_online_count) VALUES (?, ?, ?, ?)"
    
    # Insert data into the table
    for entry in rows_to_write:
        reddit_url = entry["reddit_url"]
        timestamp = entry["timestamp"]
        total_member_count = entry["total_member_count"]
        total_online_count = entry["total_online_count"]

        cursor.execute(
            query,
            (reddit_url, timestamp, total_member_count, total_online_count),
        )

    conn.commit()
    conn.close()


def create_sqlite_db(db_filepath: str = "reddit_scraper.db") -> None:
    try:
        # Connect and create cursor
        conn = sqlite3.connect(db_filepath)
        cursor = conn.cursor()

        # Create the table  - delete old table if it exists
        cursor.execute("DROP TABLE IF EXISTS reddit_scraper")

        # Create the table
        query = """
            CREATE TABLE IF NOT EXISTS reddit_scraper (
                reddit_url TEXT,
                timestamp INTEGER,
                total_member_count INTEGER,
                total_online_count INTEGER
            );
        """
        cursor.execute(query)

        # Create index on reddit_url for faster retrieval
        query = "CREATE INDEX index_reddit_url ON reddit_scraper (reddit_url);"
        query = "CREATE INDEX index_reddit_timestamp ON reddit_scraper (timestamp);"
        cursor.execute(query)

        conn.commit()
        conn.close()
        print("SUCCESS: create_sqlite_db ran successfully")
    except Exception as e:
        print(f"FAILURE: create_sqlite_db failed with exception {e}")


if __name__ == "__main__":
    # Create db
    create_sqlite_db()
