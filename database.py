import sqlite3

connection = sqlite3.connect("student.db")
print("database opend successfully.")

TABLE_NAME= "student_table"
STUDENT_ID= "student_id"
STUDENT_NAME= "student_name"
STUDENT_COLLEGE= "student_college"
STUDENT_ADDRESS= "student_address"
STUDENT_PHONE= "student_phone"

connection. execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID + " INTEGER PRIMARY KEY " + " AUTOINCREMENT, " + STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, "+ STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + "  INTEGER );")
print("table created successfully.")
connection. execute(" INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + " , "+ STUDENT_COLLEGE +" , "+ STUDENT_ADDRESS +" , "+ STUDENT_PHONE + ") VALUES ( 'Ajitesh' , 'RCE' , 'BAREILLY, UTTAR PRADESH' , 9639889763 ); ")
connection.commit()
cursor= connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
for row in cursor:
    print("student id is:", row[0])
    print("student  name is:", row[1])
    print("student college is:", row[2])
connection.close()
    
