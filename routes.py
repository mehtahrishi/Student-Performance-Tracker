from flask import Flask, render_template, request, redirect, url_for
from app import mongo
from bson.objectid import ObjectId

# Initialize Flask App
app = Flask(__name__)

# Home Page - List All Students
@app.route('/')
def home():
    students = mongo.db.students.find()  # Query all students from MongoDB
    return render_template('student_list.html', students=students)  # Pass students to template

# Add Student Route
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll_number = request.form['roll_number']

        # Check if roll number already exists
        if mongo.db.students.find_one({"roll_number": roll_number}):
            return "Error: Roll number already exists!", 400  

        # Create new student document
        new_student = {
            "name": name,
            "roll_number": roll_number,
        }
        # Insert new student into MongoDB
        student = mongo.db.students.insert_one(new_student)

        # Add grades if provided
        subjects = ['math', 'science', 'english']
        for subject in subjects:
            grade_value = request.form.get(subject)
            if grade_value:
                try:
                    new_grade = {
                        "student_id": student.inserted_id,  # Reference the student _id
                        "subject": subject.capitalize(),
                        "grade": float(grade_value)
                    }
                    # Insert grade into grades collection
                    mongo.db.grades.insert_one(new_grade)
                except ValueError:
                    return "Error: Invalid grade input!", 400

        return redirect(url_for('home'))

    return render_template('add_student.html')

# View Student Details & Calculate Average
@app.route('/student/<student_id>')
def student_details(student_id):
    student = mongo.db.students.find_one({"_id": ObjectId(student_id)})
    if not student:
        return "Student not found!", 404

    # Convert the Cursor to a list
    grades = list(mongo.db.grades.find({"student_id": ObjectId(student_id)}))

    # Calculate average grade
    total_grades = 0
    grade_count = 0
    for grade in grades:
        total_grades += grade["grade"]
        grade_count += 1

    average_grade = round(total_grades / grade_count, 2) if grade_count > 0 else "N/A"

    return render_template('student_details.html', student=student, grades=grades, average_grade=average_grade)

# Run App
if __name__ == '__main__':
    app.run(debug=True)
