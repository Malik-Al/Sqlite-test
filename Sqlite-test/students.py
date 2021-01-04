import sqlite3
conn = sqlite3.connect("students_db.db")

cursor = conn.cursor()
# cursor.execute("CREATE TABLE students (first_name TEXT, last_name TEXT, age INTEGER);")


# first_name = 'Jack'
# last_name = 'White'
# age = 23
# jane = ('Jane', 'Air', '18')

# students = [                 список данных
#     ('Jane', 'Air', 19),
#     ('Jane', 'Scott', 22),
#     ('Bob', 'Green', 20)
#  ]


# insert_query = "INSERT INTO students VALUES (?,?,?);"   безопасный выввод двнных 

# cursor.execute(insert_query, jane)

#for student in students:
#   cursor.execute(insert_query, student)   # создания таблиц через цикл 
# cursor.executemany(insert_query, students) 

# cursor.execute("SELECT * FROM students WHERE first_name IS 'James';") # перебор содержимого cursor
# for row in cursor:
#     print(row)

#cursor.execute("UPDATE students SET last_name = 'Austen' WHERE last_name IS 'White';") # обновления содержимое таблиц


cursor.execute("DELETE FROM  students WHERE last_name IS 'Green';") 

# print(cursor.fetchone())
cursor.execute("SELECT * FROM students;")
data = cursor.fetchall()                  # вывод таблиц
[print(row) for row in data]              # перебор данных   

conn.commit()
conn.close()