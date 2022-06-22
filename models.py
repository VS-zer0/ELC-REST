from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)
    firstname = db.Column(db.String(45), nullable=False)
    lastname = db.Column(db.String(45), nullable=False)
    midname = db.Column(db.String(45))
    stream_num = db.Column(db.Integer, nullable=False)
    group_num = db.Column(db.Integer, nullable=False)


class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)


class CourseCompletion(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), primary_key=True)
    completion_score = db.Column(db.Integer, nullable=False)
    completion_status = db.Column(db.String(12), nullable=False)


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'))
    name = db.Column(db.String(45), nullable=False)
    descr = db.Column(db.Text)


class Material(db.Model):
    mat_id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    name = db.Column(db.String(250), nullable=False)
    type = db.Column(db.String(12), nullable=False)
    link = db.Column(db.Text, nullable=False)


class Test(db.Model):
    test_id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    name = db.Column(db.String(250), nullable=False)
    number_of_tasks = db.Column(db.Integer, nullable=False)
    date_of_passage = db.Column(db.DateTime)


class TestResults(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
    test_id = db.Column(db.Integer, db.ForeignKey('test.test_id'))
    attempt_id = db.Column(db.Integer, primary_key=True)
    tasks_completed = db.Column(db.Integer, default=0)
    test_score = db.Column(db.Integer, default=0)


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.test_id'))
    task_descr = db.Column(db.Text, nullable=False)


class Ans(db.Model):
    task_id = db.Column(db.Integer, db.ForeignKey('task.task_id'), primary_key=True)
    ans_id = db.Column(db.Integer, primary_key=True)
    ans_text = db.Column(db.Text, nullable=False)
    ans_correct = db.Column(db.Boolean, default=False)


class StudentAns(db.Model):
    attempt_id = db.Column(db.Integer, db.ForeignKey('test_results.attempt_id'), primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.task_id'), primary_key=True)
    ans_chosen = db.Column(db.Integer)
