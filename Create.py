from connect_db import Database


def create_tables():

    student_table = """
        CREATE TABLE student(
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            email VARCHAR(30),
            password VARCHAR(30),
            bio TEXT,
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now());
    """

    teacher_table = """
        CREATE TABLE teacher(
            teacher_id SERIAL PRIMARY KEY,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            email VARCHAR(30),
            password VARCHAR(30),
            bio TEXT,
            contact_url VARCHAR(50),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now());
    """

    language_table = """
        CREATE TABLE language(
            language_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now());
    """

    course_satus_table = """
        CREATE TABLE course_satus(
            course_status_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now());
    """

    lesson_status_table = """
        CREATE TABLE lesson_status(
            lesson_status_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now());
    """

    course_table = """
        CREATE TABLE course(
            course_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            description TEXT,
            rating FLOAT,
            price NUMERIC,
            student_active INT,
            teacher_id INT REFERENCES teacher(teacher_id),
            language_id INT REFERENCES language(language_id),
            course_status_id INT REFERENCES course_satus(course_status_id),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now());
    """

    comment_table = """
        CREATE TABLE comment(
            comment_id SERIAL PRIMARY KEY,
            feedback TEXT,
            student_id INT REFERENCES student(student_id),
            course_id INT REFERENCES course(course_id),
            create_date TIMESTAMP DEFAULT now());
    """

    payment_table = """
        CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            amount NUMERIC,
            course_id INT REFERENCES course(course_id),
            student_id INT REFERENCES student(student_id),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now());
    """

    assignment_table = """
        CREATE TABLE assignment(
            assignment_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            student_id INT REFERENCES student(student_id),
            lesson_id INT REFERENCES lesson(lesson_id),
            deadline DATE DEFAULT now(),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now());
    """

    group_table = """
        CREATE TABLE group_1(
            group_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            lesson_id INT REFERENCES lesson(lesson_id),
            student_id INT REFERENCES student(student_id),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now());
    """

    lesson_table = """
         CREATE TABLE lesson(
            lesson_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            description TEXT,
            lesson_time DATE DEFAULT now(),
            course_id INT REFERENCES course(course_id),
            lesson_status_id INT REFERENCES lesson_status(lesson_status_id),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now());
    """

    data = {
        "student_table" : student_table,
        "group_table" : group_table,
        "assignment_table" : assignment_table,
        "payment_table" : payment_table,
        "comment_table" : comment_table,
        "course_table" : course_table,
        "lesson_status_table" : lesson_status_table,
        "course_satus_table" : course_satus_table,
        "language_table" : language_table,
        "teacher_table" : teacher_table,
        "lesson_table" : lesson_table
    }


    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_tables()