import mysql.connector
mydb=mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="sms2"
)

#1 Get list of all teachers with their classrooms and student count in each classrooms

mycursor=mydb.cursor()
sql="""
    SELECT
        t.teacher_id,
        t.fname,
        c.class_id,
        c.c_name AS class_name,
        COUNT(e.student_id)
    FROM
        teachers t
    JOIN
        classroom c ON t.teacher_id = c.teacher_id
    LEFT JOIN
        enrollments2 e ON c.class_id = e.class_id
    GROUP BY
        t.teacher_id, c.class_id
    ORDER BY
        t.teacher_id, c.class_id;
    """
mycursor.execute(sql)
myresult = mycursor.fetchall()
for i in myresult:
    print(i)



#2 Get list of students with attendance in a classroom (take input as classroomId)
# class_id = int(input("Enter class ID: "))
# mycursor=mydb.cursor()
# sql="""
#         SELECT
#             s.student_id,
#             s.fname,
#             a.attendance_date,
#             a.present
#         FROM students s
#         LEFT JOIN attendance a ON s.student_id = a.student_id
#         WHERE a.class_id = %s
# """

# # cursor.execute(query, (classroom_id,))
# mycursor.execute(sql,(class_id,))
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)





#3 Get list of students with their classrooms and courses (take input courseId)

# course_id = (input("Enter Course ID: "))
# mycursor = mydb.cursor()
# sql = """
# SELECT
#             s.student_id,
#             s.fname,
#             cl.class_id,
#             cl.c_name,
#             c.course_id,
#             c.course
#         FROM
#             students s
#         JOIN
#             enrollments2 en ON s.student_id = en.student_id
#         JOIN
#             classroom cl ON en.class_id = cl.class_id
#         JOIN
#             course c ON cl.course_id = c.course_id
#         WHERE
#             c.course_id = %s;
# """
# mycursor.execute(sql,(course_id,))
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)



#4 Get list of all Courses and average result of each course

# mycursor=mydb.cursor()
# sql="""
# SELECT
#     c.course_id,
#     c.course,
#     AVG(g.g_value) AS average_result
# FROM
#     courses c
# LEFT JOIN
#     classroom cl ON c.course_id = cl.course_id
# LEFT JOIN
#     enrollments2 e ON cl.class_id = e.class_id
# LEFT JOIN
#     grades3 g ON e.e_id = g.e_id
# GROUP BY
#     c.course_id, c.course
# ORDER BY
#     c.course_id;
# """
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)


#5 Get list of students with exam results in percentage%
# mycursor=mydb.cursor()
# sql = """
#         SELECT
#             s.student_id,
#             s.fname,
#             e.exam_name,
#             r.marks,
#             e.max_marks,
#             (r.marks/e.max_marks) * 100 AS percentage
#         FROM
#             students s
#         JOIN
#             enrollments2 en ON s.student_id = en.student_id
#         JOIN
#             exam e ON en.class_id = e.class_id
#         LEFT JOIN
#             results r ON s.student_id = r.student_id
# """
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)




#6 Get list of Classrooms with teacher’s names, grade,section, classname, year & course

# mycursor=mydb.cursor()
# sql = """
#         SELECT
#             cl.class_id,
#             t.fname,
#             t.lname,
#             t.dob,
#             cl.c_name,
#             cl.section,
#             c.course
#         FROM
#             classroom cl
#         JOIN
#             teachers2 t ON cl.teacher_id = t.teacher_id
#         JOIN
#             course c ON cl.course_id = c.course_id;
# """
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)



#7 Get list of teachers and avg marks of students studying under them
# mycursor=mydb.cursor()
# sql = """
# SELECT
#     t.teacher_id,
#     t.fname,
#     t.lname,
#     AVG(g.g_value) AS avg_marks
# FROM
#     teachers t
# JOIN
#     classroom c ON t.teacher_id = c.teacher_id
# JOIN
#     enrollments2 e ON c.class_id = e.class_id
# JOIN
#     grades3 g ON e.e_id = g.e_id
# GROUP BY
#     t.teacher_id, t.fname, t.lname;
# """
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)



#8 Get list of students studying in a year (take year as input)
# year_input = input("enter year: ")
# mycursor=mydb.cursor()
# sql = """
#     SELECT
#         s.student_id,
#         s.fname,
#         s.lname,
#         e.e_date
#     FROM
#         students s
#     JOIN
#         enrollments2 e ON s.student_id = e.student_id
#     JOIN
#         classroom c ON e.class_id = c.class_id
#     WHERE
#         e.e_date = %s
# """
# mycursor.execute(sql,(year_input,))
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)


#9 Get exam timetable for students coursewise
# get_course_id=input("enter course id: ")
# mycursor=mydb.cursor()
# sql = """
#      SELECT
#             ex.exam_id,
#             ex.exam_name,
#             ex.exam_date,
#             c.course_id,
#             c.course
#         FROM
#             exam ex
#         JOIN
#             course c ON ex.course_id = c.course_id
#         WHERE
#             c.course_id = %s
#         ORDER BY
#             ex.exam_date;
#         """
# mycursor.execute(sql,(get_course_id,))
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)



#10 Get all data (course, exam results, teacher,grade, etc) of a student using studentId (take studentId as input)
# get_student_id=input("student id: ")
# mycursor=mydb.cursor()
# sql = """
#         SELECT
#             s.student_id,
#             s.fname,
#             s.lname,
#             c.course_id,
#             c.course,
#             e.exam_id,
#             e.exam_name,
#             r.marks,
#             g.g_id,
#             g.g_value
#         FROM
#             students s
#         JOIN
#             enrollments2 en ON s.student_id = en.student_id
#         LEFT JOIN
#             exam e ON en.class_id = e.class_id
#         JOIN
#             course c ON e.course_id = c.course_id
#         LEFT JOIN
#             results r ON s.student_id = r.student_id
#         LEFT JOIN
#             grades3 g ON r.g_id = g.g_id
#         WHERE
#             s.student_id = %s;
#
# """
# mycursor.execute(sql,(get_student_id,))
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)
    # print(f"Teacher ID: {i['teacher_id']}, Teacher Name: {i['fname']}")
    # print(f"Class ID: {i['class_id']}, Classroom Name: {i['c_name']}")
    # print(f"Student Count: {i['student_count']}")
    # print("")




