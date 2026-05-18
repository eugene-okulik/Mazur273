import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

new_student = '''
    INSERT INTO students (name, second_name)
    VALUES (%s, %s)
'''
cursor.execute(
    new_student,
    ('Alexandr', 'Turinov')
)
student_id = cursor.lastrowid
print(student_id)

new_books = '''
    INSERT INTO books (title, taken_by_student_id)
    VALUES (%s, %s)
'''
booklist = [
    ('Лучше плохо, чем никак', student_id),
    ('Плохо, переделывай', student_id)
]
cursor.executemany(new_books, booklist)

new_group = '''
    INSERT INTO `groups` (title, start_date, end_date)
    VALUES (%s, %s, %s)
'''
cursor.execute(new_group, ('тревожные сверхлюди', '15/05', '15/05'))
new_group_id = cursor.lastrowid
print(new_group_id)

upd_stud_group = '''
    UPDATE students
    SET group_id = %s
    WHERE id = %s
'''
cursor.execute(upd_stud_group, (new_group_id, student_id))

get_student = '''
    SELECT *
    FROM students
    WHERE id = %s
'''
cursor.execute(get_student, (student_id,))
student_info = cursor.fetchone()
print(student_info)  # смотрю что изменилась группа

new_subs = '''
    INSERT INTO subjects (title)
    VALUES (%s)
'''
subjects_list = ['Стоицизм', 'Лежацизм']
subject_ids = []
for i in subjects_list:
    cursor.execute(new_subs, (i,))
    subject_ids.append(cursor.lastrowid)
print(subject_ids)

new_lessons = '''
    INSERT INTO lessons (title, subject_id)
    VALUES (%s, %s)
'''

lessons_list = [
    ('Урок1Предмет1', subject_ids[0]),
    ('Урок2Предмет1', subject_ids[0]),
    ('Урок1Предмет2', subject_ids[1]),
    ('Урок2Предмет2', subject_ids[1]),
]

lesson_ids = []
for lesson in lessons_list:
    cursor.execute(new_lessons, lesson)
    lesson_ids.append(cursor.lastrowid)
print(lesson_ids)

marks = '''
    INSERT INTO marks (value, lesson_id, student_id)
    VALUES (%s, %s, %s)
'''

marks_list = [
    ('1', lesson_ids[0], student_id),
    ('2', lesson_ids[1], student_id),
    ('3', lesson_ids[2], student_id),
    ('4', lesson_ids[3], student_id),
]

cursor.executemany(marks, marks_list)

result = '''
    SELECT
    s.second_name,
    s.name,
    g.title,
    b.title,
    m.value,
    l.title,
    sub.title
FROM students s
JOIN `groups` g
    ON s.group_id = g.id
JOIN books b
    ON s.id = b.taken_by_student_id
JOIN marks m
    ON s.id = m.student_id
JOIN lessons l
    ON m.lesson_id = l.id
JOIN subjects sub
    ON l.subject_id = sub.id
WHERE s.id = %s;
'''
cursor.execute(result, (student_id,))
result = cursor.fetchall()
print(result)

db.commit()
db.close()
