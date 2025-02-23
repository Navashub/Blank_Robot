import psycopg2
from psycopg2 import sql
from models.robot_model import RobotData
from dotenv import load_dotenv
import os 

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


def db_conn():
    return psycopg2.connect(DATABASE_URL)

def get_all_robot_data():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM robot_data''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    
    return [RobotData(id=row[0], video_url=row[1], audio_url=row[2], motion=row[3], timestamp=row[4]) for row in data]

def get_robot_data_by_id(data_id):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM robot_data WHERE id = %s''', (data_id))
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if row:
        return RobotData(id=row[0], video_url=row[1], audio_url=row[2], motion=row[3], timestamp=row[4])
    return None 

def create_robot_data(video_url, audio_url, motion):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''INSERT INTO robot_data (video_url, audio_url, motion) VALUES (%s, %s, %s) RETURNING id''', (video_url, audio_url, motion))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    
    return new_id
    
