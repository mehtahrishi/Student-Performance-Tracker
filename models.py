from app import mongo

# Student Model (Collection)
def create_student(name, roll_number):
    student_data = {
        "name": name,
        "roll_number": roll_number,
    }
    student = mongo.db.students.insert_one(student_data)  # Inserting into the 'students' collection
    return student.inserted_id

# Grade Model (Collection)
def create_grade(student_id, subject, grade):
    grade_data = {
        "student_id": student_id,
        "subject": subject,
        "grade": grade,
    }
    grade = mongo.db.grades.insert_one(grade_data)  # Inserting into the 'grades' collection
    return grade.inserted_id

# To get all grades for a student
def get_grades_for_student(student_id):
    grades = mongo.db.grades.find({"student_id": student_id})
    return list(grades)  # Return grades as a list

# To get student by roll_number
def get_student_by_roll_number(roll_number):
    student = mongo.db.students.find_one({"roll_number": roll_number})
    return student  # Return the student document
