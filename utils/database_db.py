import psycopg2 as db
from main.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS

class Database:

    def __init__(self):
        self.connect = db.connect(
            database=DB_NAME,
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASS
        )
        self.cursor = self.connect.cursor()

    def create_table(self):
        user_table = """
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(50),
        phone_number VARCHAR(9),
        location_name VARCHAR(50))"""

        photos = """
        CREATE TABLE IF NOT EXISTS photos (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(id),
        status BOOLEAN DEFAULT false)"""

        like = """
        CREATE TABLE IF NOT EXISTS likes (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(id),
        photo INT REFERENCES photos(id),
        is_like BOOLEAN DEFAULT false)"""

        self.cursor.execute(user_table)
        self.cursor.execute(photos)
        self.cursor.execute(like)

        self.connect.commit()


