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
        chat_id BIGINT NOT NULL,
        full_name VARCHAR(50),
        phone_number VARCHAR(9),
        location_name VARCHAR(50))"""

        photos = """
        CREATE TABLE IF NOT EXISTS photos (
        id SERIAL PRIMARY KEY,
        chat_id BIGINT,
        foto_id VARCHAR(250),
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

    def get_user_chat_id(self, chat_id):
        query = f"SELECT * FROM users WHERE chat_id = {chat_id}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def get_photo_id(self, chat_id):
        query = f"SELECT * FROM photos WHERE chat_id = {chat_id} AND status = true"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def add_user_chat(self, data: dict):
        chat_id = data["chat_id"]
        full_name = data["full_name"]
        phone_number = data["phone_number"]
        location_name = data["location_name"]
        query = f"""INSERT INTO users (chat_id, full_name, phone_number, location_name) VALUES ({chat_id},'{full_name}','{phone_number}','{location_name}')"""
        self.cursor.execute(query)
        self.connect.commit()
        return True

    def update_photos_id(self, data: dict):
        chat_id = data["chat_id"]
        photo_id = data["photo_id"]
        query = f"""INSERT INTO photos (chat_id, foto_id, status) VALUES ({chat_id},'{photo_id}', true)"""
        self.cursor.execute(query)
        self.connect.commit()
        return True
