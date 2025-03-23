from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Flask-Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

# Database Models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_number = db.Column(db.String(20), unique=True, nullable=False)
    grades = db.relationship('Grade', backref='student', lazy=True)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.Float, nullable=False)

# Initialize Database
with app.app_context():
    db.create_all()

# Home Page - List All Students
@app.route('/')
def home():
    students = Student.query.all()
    return render_template('student_list.html', students=students)  # Use a correct list template

# Add Student Route
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll_number = request.form['roll_number']

        # Check if roll number already exists
        if Student.query.filter_by(roll_number=roll_number).first():
            return "Error: Roll number already exists!", 400  

        new_student = Student(name=name, roll_number=roll_number)
        db.session.add(new_student)
        db.session.commit()

        # Add Grades if provided
        subjects = ['math', 'science', 'english']
        for subject in subjects:
            grade_value = request.form.get(subject)
            if grade_value:
                try:
                    new_grade = Grade(student_id=new_student.id, subject=subject.capitalize(), grade=float(grade_value))
                    db.session.add(new_grade)
                except ValueError:
                    return "Error: Invalid grade input!", 400

        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add_student.html')

# View Student Details & Calculate Average
@app.route('/student/<int:student_id>')
def student_details(student_id):
    student = Student.query.get_or_404(student_id)
    grades = Grade.query.filter_by(student_id=student_id).all()

    # Calculate average grade
    if grades:
        total = sum(grade.grade for grade in grades)
        average_grade = round(total / len(grades), 2)
    else:
        average_grade = "N/A"

    return render_template('student_details.html', student=student, grades=grades, average_grade=average_grade)

# Run App
if __name__ == '__main__':
    app.run(debug=True)
