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

new_book1 = '''
    INSERT INTO books (title, taken_by_student_id)
    VALUES (%s, %s)
'''
cursor.execute(new_book1, ('Лучше плохо, чем никак', student_id))
first_book_id = cursor.lastrowid
print(first_book_id)

new_book2 = '''
    INSERT INTO books (title, taken_by_student_id)
    VALUES (%s, %s)
'''
cursor.execute(new_book1, ('Плохо, переделывай', student_id))
sec_book_id = cursor.lastrowid
print(sec_book_id)

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

new_subj1 = '''
    INSERT INTO subjects (title)
    VALUES (%s)
'''
cursor.execute(new_subj1, ('Стоицизм',))
new_subj1_id = cursor.lastrowid
print(new_subj1_id)

new_subj2 = '''
    INSERT INTO subjects (title)
    VALUES (%s)
'''
cursor.execute(new_subj2, ('Лежацизм',))
new_subj2_id = cursor.lastrowid
print(new_subj2_id)

new_lesson1_1 = '''
    INSERT INTO lessons (title, subject_id)
    VALUES (%s, %s)
'''
cursor.execute(new_lesson1_1, ('Урок1Предмет1', new_subj1_id))
new_lesson1_1_id = cursor.lastrowid
print(new_lesson1_1_id)

new_lesson1_2 = '''
    INSERT INTO lessons (title, subject_id)
    VALUES (%s, %s)
'''
cursor.execute(new_lesson1_2, ('Урок2Предмет1', new_subj1_id))
new_lesson1_2_id = cursor.lastrowid
print(new_lesson1_2_id)

new_lesson2_1 = '''
    INSERT INTO lessons (title, subject_id)
    VALUES (%s, %s)
'''
cursor.execute(new_lesson2_1, ('Урок1Предмет2', new_subj2_id))
new_lesson2_1_id = cursor.lastrowid
print(new_lesson2_1_id)

new_lesson2_2 = '''
    INSERT INTO lessons (title, subject_id)
    VALUES (%s, %s)
'''
cursor.execute(new_lesson2_2, ('Урок2Предмет2', new_subj2_id))
new_lesson2_2_id = cursor.lastrowid
print(new_lesson2_2_id)

mark_lesson1_1 = '''
    INSERT INTO marks (value, lesson_id, student_id)
    VALUES (%s, %s, %s)
'''
cursor.execute(mark_lesson1_1, ('1', new_lesson1_1_id, student_id))
mark_lesson1_1_id = cursor.lastrowid
print(mark_lesson1_1_id)

mark_lesson1_2 = '''
    INSERT INTO marks (value, lesson_id, student_id)
    VALUES (%s, %s, %s)
'''
cursor.execute(mark_lesson1_2, ('2', new_lesson1_2_id, student_id))
mark_lesson1_2_id = cursor.lastrowid
print(mark_lesson1_2_id)

mark_lesson2_1 = '''
    INSERT INTO marks (value, lesson_id, student_id)
    VALUES (%s, %s, %s)
'''
cursor.execute(mark_lesson2_1, ('3', new_lesson2_1_id, student_id))
mark_lesson2_1_id = cursor.lastrowid
print(mark_lesson2_1_id)

mark_lesson2_2 = '''
    INSERT INTO marks (value, lesson_id, student_id)
    VALUES (%s, %s, %s)
'''
cursor.execute(mark_lesson2_2, ('4', new_lesson2_2_id, student_id))
mark_lesson2_2_id = cursor.lastrowid
print(mark_lesson2_2_id)

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
