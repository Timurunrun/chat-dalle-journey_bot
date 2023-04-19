import sqlite3
import datetime
from datetime import timedelta

try:
    conn = sqlite3.connect('users_info.db')
    cursor = conn.cursor()
    conn.execute('PRAGMA foreign_keys = ON')
    conn.commit()
except Exception as e:
    print(e)
    
def is_user_exist(tg_id):
    return bool(len(cursor.execute('SELECT sys_id FROM users WHERE tg_id = ?', (tg_id,)).fetchall()))

def create_new_user(tg_id):
    today = datetime.date.today()
    cursor.execute('INSERT INTO users (tg_id, end_sub) VALUES (?, ?)', (tg_id, today,))
    conn.commit()

def sub_status(tg_id):
    end_sub = (cursor.execute('SELECT end_sub FROM users WHERE tg_id = ?', (tg_id,)).fetchone()[0])
    today = datetime.date.today()
    end_sub = datetime.datetime.strptime(end_sub, '%Y-%m-%d').date()
    return int((end_sub - today).days)

def sub_renewal(tg_id, days):
    end_sub = (cursor.execute('SELECT end_sub FROM users WHERE tg_id = ?', (tg_id,)).fetchone()[0])
    end_sub = datetime.datetime.strptime(end_sub, '%Y-%m-%d').date()
    end_sub = (end_sub + timedelta(days=days)).strftime('%Y-%m-%d')
    cursor.execute('UPDATE users SET end_sub = ? WHERE tg_id = ?', (end_sub, tg_id,))
    conn.commit()
