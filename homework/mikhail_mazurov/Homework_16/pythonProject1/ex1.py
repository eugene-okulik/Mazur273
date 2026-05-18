import dotenv
import csv
import os
import mysql.connector as mysql


dotenv.load_dotenv()


file_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
print(homework_path)
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
print(eugene_file_path)

with open(eugene_file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    new_data = []
    for row in file_data:
        new_data.append(row)
    print(new_data)


db = mysql.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
)
cursor = db.cursor(dictionary=True)

delta_data = []


for row in new_data:
    query = """
    SELECT
        s.name,
        s.second_name,
        g.title AS group_title,
        b.title AS book_title,
        sub.title AS subject_title,
        l.title AS lesson_title,
        m.value AS mark_value
    FROM students s
    JOIN `groups` g ON s.group_id = g.id
    JOIN books b ON s.id = b.taken_by_student_id
    JOIN marks m ON s.id = m.student_id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjects sub ON l.subject_id = sub.id
    WHERE s.name = %s
      AND s.second_name = %s
      AND g.title = %s
      AND b.title = %s
      AND sub.title = %s
      AND l.title = %s
      AND m.value = %s
    """

    value = (
        row["name"],
        row["second_name"],
        row["group_title"],
        row["book_title"],
        row["subject_title"],
        row["lesson_title"],
        row["mark_value"],
    )

    cursor.execute(query, value)
    result = cursor.fetchall()
    if result is None:
        delta_data.append(row)

print(delta_data)
# самопроверка не прошла - мне выдает все 4 строки как уникальные. через ДБивер тоже не нашел в бр вторую строку
db.close()
