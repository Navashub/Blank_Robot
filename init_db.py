import sqlite3


conn = sqlite3.connect("robot_data.db")
cur = conn.cursor()

# Create table 
cur.execute('''
    CREATE TABLE IF NOT EXISTS robot_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        video_url TEXT,
        audio_url TEXT,
        motion TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')


# cur.execute('''
#     INSERT INTO robot_data (video_url, audio_url, motion) 
#     VALUES ( 'FORWARD')
# ''')


conn.commit()
cur.close()
conn.close()

print("Database initialized successfully!")

