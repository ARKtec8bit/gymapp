import json
import random
import sqlite3


def load_data(filename):
    """
    Load data from a JSON file. If the file does not exist, return an empty dictionary.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_data(data, filename):
    """
    Save data to a JSON file.
    """
    pass


def get_random_exercise(data):
    workout = {}
    for category, groups in data.items():
        workout[category] = {}
        if isinstance(groups, dict):
            # If there are subcategories
            for group, exercises in groups.items():
                workout[category][group] = random.choice(exercises)
        else:  # If there are no subcategories
            workout[category] = random.choice(groups)
    return workout


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table():
    conn = create_connection('data/database.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS biometric_data (
            id INTEGER PRIMARY KEY,
            date TEXT,
            user TEXT,
            weight REAL,
            height REAL,
            chest REAL,
            hips REAL,
            waist REAL,
            shoulder REAL,
            left_bicep REAL,
            right_bicep REAL,
            left_forearm REAL,
            right_forearm REAL,
            left_leg REAL,
            right_leg REAL,
            left_calf REAL,
            right_calf REAL
        )
    """)
    conn.commit()
    conn.close()


def insert_data(date, user, weight, height, chest, hips, waist, shoulder, left_bicep, right_bicep, left_forearm, right_forearm, left_leg, right_leg, left_calf, right_calf):
    conn = create_connection('data/database.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO biometric_data (
            date, user, weight, height, chest, hips, waist, shoulder, left_bicep, right_bicep, left_forearm, right_forearm, left_leg, right_leg, left_calf, right_calf
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (date, user, weight, height, chest, hips, waist, shoulder, left_bicep, right_bicep, left_forearm, right_forearm, left_leg, right_leg, left_calf, right_calf))
    conn.commit()
    conn.close()


def get_data():
    conn = create_connection('data/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM biometric_data")
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_usernames():
    conn = create_connection('data/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT user FROM biometric_data")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]
