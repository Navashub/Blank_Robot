import sqlite3
from models.robot_model import RobotData

DB_NAME = "robot_data.db"

def db_conn():
    return sqlite3.connect(DB_NAME)

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
    cur.execute('''SELECT * FROM robot_data WHERE id = ?''', (data_id))
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if row:
        return RobotData(id=row[0], video_url=row[1], audio_url=row[2], motion=row[3], timestamp=row[4])
    return None 

def create_robot_data(video_url, audio_url, motion):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''INSERT INTO robot_data (video_url, audio_url, motion) VALUES (?, ?, ?)''', (video_url, audio_url, motion))
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    conn.close()
    
    return new_id
    