from connect_db import Database


class Base:
    @staticmethod
    def select(table):
        query = f"SELECT * FROM {table}"
        return Database.connect(query, "select")

    @staticmethod
    def delete_id(table, id):
        query = f"DELETE FROM {table} WHERE student_id = {id}"
        return Database.connect(query, "delete")

    @staticmethod
    def update_id(table, colum_name, old_data, new_data):
        query = f"UPDATE {table} SET {colum_name} = {new_data} WHERE {colum_name} = '{old_data}'"
        return Database.connect(query, "update")

    @staticmethod
    def update(table, colum_name, old_data, new_data):
        query = f"UPDATE {table} SET {colum_name} = '{new_data}' WHERE {colum_name} = '{old_data}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete(table, column_name, data):
        query = f"DELETE FROM {table} WHERE {column_name} = '{data}'"
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(table, column_name, data):
        query = f"DELETE FROM {table} WHERE {column_name} = {data}"
        return Database.connect(query, "delete")


class Language(Base):
    def __init__(self, name):
        self.name = name

    def insert(self, table):
        query = f"INSERT INTO {table}(name) VALUES('{self.name}')"
        return Database.connect(query, "insert")


class Course(Base):
    def __init__(self, name, description, rating, price, student_active, teacher_id, language_id, course_status_id):
        self.name = name
        self.description = description
        self.rating = rating
        self.price = price
        self.student_active = student_active
        self.teacher_id = teacher_id
        self.language_id = language_id
        self.course_status_id = course_status_id


    @staticmethod
    def select(table):
        query = """
            SELECT course.course_id, course.name, course.description, course.rating, teacher.first_name, teacher.last_name, course_status.name, language.name, course.price FROM course
                INNER JOIN teacher
                    ON course.teacher_id = teacher.teacher_id
                INNER JOIN course_satatus
                    ON course.course_satatus_id = course.course_status_id
                INNER JOIN language
                    ON language.language_id = course.language_id
        """
        return Database.connect(query, "select")

    def insert(self, table):
        query = (f"INSERT INTO {table}(name, description, rating, student_active, teacher_id, language_id, price, course_status_id)"
                 f" VALUES('{self.name}', '{self.description}',  {self.rating},  {self.student_active},  {self.teacher_id},  {self.language_id},  {self.price},  {self.course_status_id})")
        return Database.connect(query, "insert")

