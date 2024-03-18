import psycopg2 as db
import os
from dotenv import load_dotenv
load_dotenv()

class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database=os.getenv("DATABASE"),
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD")
        )

        cursor = database.cursor()

        cursor.execute(query)
        data = ["insert", "delete", "update", "create"]
        if query_type in data:
            database.commit()
            if query_type == "insert":
                return "INSERTED"

            elif query_type == "delete":
                return "DELETE"

            elif query_type == "update":
                return "UPDATED"

            elif query_type == "create":
                return "CREATED"

        else:
            return cursor.fetchall()