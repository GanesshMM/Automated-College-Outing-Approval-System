from flask import Flask, render_template, jsonify, request
from database import load_students_from_db, load_student_from_db
from mail import email_data

app = Flask(__name__)

@app.route("/")
def hello():
  students = load_students_from_db()
  return render_template('home.html', students=students)

@app.route("/api/students")
def student_list():
  students = load_students_from_db()
  return jsonify(students)

@app.route("/student/<id>")
def show_student(id):
  student = load_student_from_db(id)
  if not student:
    return "Not Found", 404
  return render_template('studentpage.html', 
                         student = student)

@app.route("/student/<id>/apply", methods=['post'])
def apply_to_student(id):
  data = request.form
  email_data(id, data)
  return render_template('outing_form_submit.html',
                         data=data)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
