import psycopg2
from psycopg2 import sql 
from dotenv import load_dotenv
import os 

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# Create table 
cur.execute('''
    CREATE TABLE IF NOT EXISTS robot_data (
        id SERIAL PRIMARY KEY,
        video_url TEXT,
        audio_url TEXT,
        motion TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')


conn.commit()
cur.close()
conn.close()

print("Database initialized successfully!")

