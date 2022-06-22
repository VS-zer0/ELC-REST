from flask import Flask, request
from flask_restful import Api, Resource
from models import db, Student, Course, CourseCompletion, Category, Material, Test, TestResults, Task, Ans, StudentAns
import schemas
from schemas import ma

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:elc12345@localhost/elc'
db.init_app(app)
ma.init_app(app)
api = Api(app)


class StudentList(Resource):
    def get(self):
        students = Student.query.all()
        return schemas.students_schema.dump(students)

    def post(self):
        new_student = Student(
            email=request.json['email'],
            password=request.json['password'],
            firstname=request.json['firstname'],
            lastname=request.json['lastname'],
            midname=request.json['midname'],
            stream_num=request.json['stream_num'],
            group_num=request.json['group_num']
        )
        db.session.add(new_student)
        db.session.commit()
        return schemas.student_schema.dump(new_student)


api.add_resource(StudentList, '/students')


class StudentById(Resource):
    def get(self, id):
        student = Student.query.get_or_404(id)
        return schemas.student_schema.dump(student)

    def patch(self, id):
        student = Student.query.get_or_404(id)
        if 'email' in request.json:
            student.email = request.json['email']
        if 'password' in request.json:
            student.password = request.json['password']
        if 'firstname' in request.json:
            student.firstname = request.json['firstname']
        if 'lastname' in request.json:
            student.lastname = request.json['lastname']
        if 'midname' in request.json:
            student.midname = request.json['midname']
        if 'stream_num' in request.json:
            student.stream = request.json['stream_num']
        if 'group_num' in request.json:
            student.group = request.json['group_num']
        db.session.commit()
        return schemas.student_schema.dump(student)

    def delete(self, id):
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        return 'Student data deleted'


api.add_resource(StudentById, '/students/<int:id>')


class StudentStatus(Resource):
    def get(self, id):
        status = CourseCompletion.query.filter_by(student_id=id)
        return schemas.completions_schema.dump(status)

    def post(self):
        new_status = CourseCompletion(
            student_id=id,
            course_id=request.json['course_id']
        )
        db.session.add(new_status)
        db.session.commit()
        return schemas.completion_schema.dump(new_status)


api.add_resource(StudentStatus, '/students/<int:id>/status')


class StudentStatusByCourse(Resource):
    def get(self, id, course_id):
        status = CourseCompletion.query.filter_by(course_id=course_id, student_id=id).first()
        return schemas.completion_schema.dump(status)

    def delete(self, id, course_id):
        status = CourseCompletion.query.filter_by(course_id=course_id, student_id=id).first()
        db.session.delete(status)
        db.session.commit()
        return 'Student left the course'


api.add_resource(StudentStatusByCourse, '/students/<int:id>/status/<int:course_id>')


class StudentTests(Resource):
    def get(self, id):
        tests = TestResults.query.filter_by(student_id=id)
        return schemas.results_schema.dump(tests)

    def post(self, id):
        new_test = TestResults(
            student_id=id,
            test_id=request.json['test_id']
        )
        db.session.add(new_test)
        db.session.commit()
        return schemas.result_schema.dump(new_test)


api.add_resource(StudentTests, '/students/<int:id>/tests')


class StudentTestsById(Resource):
    def get(self, id, test_id):
        test = TestResults.query.filter_by(student_id=id, test_id=test_id).first()
        return schemas.result_schema.dump(test)


api.add_resource(StudentTestsById, '/students/<int:id>/tests/<int:test_id>')


class StudentAnswers(Resource):
    def get(self, id, test_id):
        att_id = TestResults.query.filter_by(student_id=id, test_id=test_id).order_by(
            -TestResults.attempt_id).first().attempt_id
        ansrs = StudentAns.query.filter_by(attempt_id=att_id)
        return schemas.student_ansrs_schema.dump(ansrs)

    def post(self, id, test_id):
        att_id = TestResults.query.filter_by(student_id=id, test_id=test_id).order_by(
            -TestResults.attempt_id).first().attempt_id
        new_ans = StudentAns(
            attempt_id=att_id,
            task_id=request.json['task_id'],
            ans_chosen=request.json['ans_chosen']
        )
        db.session.add(new_ans)
        db.session.commit()
        return schemas.student_ans_schema.dump(new_ans)


api.add_resource(StudentAnswers, '/students/<int:id>/tests/<int:test_id>/answers')


class StudentAnsByTask(Resource):
    def get(self, id, test_id, task_id):
        att_id = TestResults.query.filter_by(student_id=id, test_id=test_id).order_by(
            -TestResults.attempt_id).first().attempt_id
        ans = StudentAns.query.filter_by(attempt_id=att_id, task_id=task_id).first()
        return schemas.student_ans_schema.dump(ans)


api.add_resource(StudentAnsByTask, '/students/<int:id>/tests/<int:test_id>/answers/<int:task_id>')


class CourseList(Resource):
    def get(self):
        courses = Course.query.all()
        return schemas.courses_schema.dump(courses)

    def post(self):
        new_course = Course(
            name=request.json['name']
        )
        db.session.add(new_course)
        db.session.commit()
        return schemas.course_schema.dump(new_course)


api.add_resource(CourseList, '/courses')


class CourseById(Resource):
    def get(self, id):
        course = Course.query.get_or_404(id)
        return schemas.course_schema.dump(course)

    def patch(self, id):
        course = Course.query.get_or_404(id)
        course.name = request.json['name']
        db.session.commit()
        return schemas.course_schema.dump(course)

    def delete(self, id):
        course = Course.query.get_or_404(id)
        db.session.delete(course)
        db.session.commit()
        return 'Course data deleted'


api.add_resource(CourseById, '/courses/<int:id>')


class CategoriesInCourse(Resource):
    def get(self, id):
        cats = Category.query.filter_by(course_id=id)
        return schemas.categories_schema.dump(cats)

    def post(self, id):
        new_cat = Category(
            course_id=id,
            name=request.json['name'],
            descr=request.json['descr']
        )
        db.session.add(new_cat)
        db.session.commit()
        return schemas.category_schema.dump(new_cat)


api.add_resource(CategoriesInCourse, '/courses/<int:id>/categories')


class CourseCatsById(Resource):
    def get(self, id, cat_id):
        cat = Category.query.get_or_404(cat_id)
        return schemas.category_schema.dump(cat)

    def patch(self, id, cat_id):
        cat = Category.query.get_or_404(cat_id)
        if 'name' in request.json:
            cat.name = request.json['name']
        if 'descr' in request.json:
            cat.password = request.json['descr']
        db.session.commit()
        return schemas.category_schema.dump(cat)

    def delete(self, id, cat_id):
        cat = Category.query.get_or_404(cat_id)
        db.session.delete(cat)
        db.session.commit()
        return 'Category data deleted'


api.add_resource(CourseCatsById, '/courses/<int:id>/categories/<int:cat_id>')


class CourseStatus(Resource):
    def get(self, id):
        status = CourseCompletion.query.filter_by(course_id=id)
        return schemas.completions_schema.dump(status)

    def post(self):
        new_status = CourseCompletion(
            student_id=request.json['student_id'],
            course_id=id
        )
        db.session.add(new_status)
        db.session.commit()
        return schemas.completion_schema.dump(new_status)


api.add_resource(CourseStatus, '/courses/<int:id>/status')


class CourseStatusByStudent(Resource):
    def get(self, id, student_id):
        status = CourseCompletion.query.filter_by(course_id=id, student_id=student_id).first()
        return schemas.completion_schema.dump(status)

    def delete(self, id, student_id):
        status = CourseCompletion.query.filter_by(course_id=id, student_id=student_id).first()
        db.session.delete(status)
        db.session.commit()
        return 'Student removed from course'


api.add_resource(CourseStatusByStudent, '/courses/<int:id>/status/<int:student_id>')


class MatsInCat(Resource):
    def get(self, id, cat_id):
        mats = Material.query.filter_by(category_id=cat_id)
        return schemas.materials_schema.dump(mats)

    def post(self, id, cat_id):
        new_mat = Material(
            category_id=cat_id,
            name=request.json['name'],
            type=request.json['type'],
            link=request.json['link']
        )
        db.session.add(new_mat)
        db.session.commit()
        return schemas.material_schema.dump(new_mat)


api.add_resource(MatsInCat, '/courses/<int:id>/categories/<int:cat_id>/materials')


class MatsInCatById(Resource):
    def get(self, id, cat_id, mat_id):
        mat = Material.query.get_or_404(mat_id)
        return schemas.material_schema.dump(mat)

    def patch(self, id, cat_id, mat_id):
        mat = Material.query.get_or_404(mat_id)
        if 'name' in request.json:
            mat.name = request.json['name']
        if 'type' in request.json:
            mat.type = request.json['type']
        if 'link' in request.json:
            mat.link = request.json['link']
        db.session.commit()
        return schemas.material_schema.dump(mat)

    def delete(self, id, cat_id, mat_id):
        mat = Material.query.get_or_404(mat_id)
        db.session.delete(mat)
        db.session.commit()
        return 'Material data deleted'


api.add_resource(MatsInCatById, '/courses/<int:id>/categories/<int:cat_id>/materials/<int:mat_id>')


class TestsInCat(Resource):
    def get(self, id, cat_id):
        tests = Test.query.filter_by(category_id=cat_id)
        return schemas.tests_schema.dump(tests)

    def post(self, id, cat_id):
        new_test = Test(
            category_id=cat_id,
            name=request.json['name'],
            date_of_pasage=request.json['date_of_passage']
        )
        db.session.add(new_test)
        db.session.commit()
        return schemas.test_schema.dump(new_test)


api.add_resource(TestsInCat, '/courses/<int:id>/categories/<int:cat_id>/tests')


class TestsInCatById(Resource):
    def get(self, id, cat_id, test_id):
        test = Test.query.get_or_404(test_id)
        return schemas.test_schema.dump(test)

    def patch(self, id, cat_id, test_id):
        test = Test.query.get_or_404(test_id)
        if 'name' in request.json:
            test.name = request.json['name']
        if 'date_of_passage' in request.json:
            test.date_of_passage = request.json['date_of_passage']
        db.session.commit()
        return schemas.test_schema.dump(test)

    def delete(self, id, cat_id, test_id):
        test = Test.query.get_or_404(test_id)
        db.session.delete(test)
        db.session.commit()
        return 'Test deleted'


api.add_resource(TestsInCatById, '/courses/<int:id>/categories/<int:cat_id>/tests/<int:test_id>')


class ResultsInTest(Resource):
    def get(self, id, cat_id, test_id):
        results = TestResults.query.filter_by(test_id=test_id)
        return schemas.results_schema.dump(results)


api.add_resource(ResultsInTest, '/courses/<int:id>/categories/<int:cat_id>/tests/<int:test_id>/results')


class ResultInTestById(Resource):
    def get(self, id, cat_id, test_id, att_id):
        res = TestResults.query.get_or_404(att_id)
        return schemas.result_schema.dump(res)


api.add_resource(ResultInTestById, '/courses/<int:id>/categories/<int:cat_id>/tests/<int:test_id>/results'
                                   '/<int:att_id>')


class TasksInTest(Resource):
    def get(self, id, cat_id, test_id):
        tasks = Task.query.filter_by(test_id=test_id)
        return schemas.tasks_schema.dump(tasks)

    def post(self, id, cat_id, test_id):
        new_task = Task(
            test_id=test_id,
            task_descr=request.json['task_descr']
        )
        db.session.add(new_task)
        db.session.commit()
        return schemas.task_schema.dump(new_task)


api.add_resource(TasksInTest, '/courses/<int:id>/categories/<int:cat_id>/tests/<int:test_id>/tasks')


class TasksInTestById(Resource):
    def get(self, id, cat_id, test_id, task_id):
        task = Task.query.get_or_404(task_id)
        return schemas.task_schema.dump(task)

    def patch(self, id, cat_id, test_id, task_id):
        task = Task.query.get_or_404(task_id)
        task.task_descr = request.json['task_descr']
        db.session.commit()
        return schemas.task_schema.dump(task)

    def delete(self, id, cat_id, test_id, task_id):
        task = Test.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return 'Task removed'


api.add_resource(TasksInTestById, '/courses/<int:id>/categories/<int:cat_id>/tests/<int:test_id>/tasks/<int:task_id>')


class AnsInTask(Resource):
    def get(self, id, cat_id, test_id, task_id):
        ansrs = Ans.query.filter_by(task_id=task_id)
        return schemas.ansrs_schema.dump(ansrs)

    def post(self, id, cat_id, test_id, task_id):
        new_ans = Ans(
            task_id=task_id,
            ans_text=request.json['ans_text'],
            ans_correct=request.json['ans_correct']
        )
        db.session.add(new_ans)
        db.session.commit()
        return schemas.ans_schema.dump(new_ans)


api.add_resource(AnsInTask, '/courses/<int:id>/categories/<int:cat_id>/tests/<int:test_id>/tasks/<int:task_id>/answers')


class AnsInTaskById(Resource):
    def get(self, id, cat_id, test_id, task_id, ans_id):
        ans = Ans.query.filter_by(task_id=task_id, ans_id=ans_id).first()
        return schemas.ans_schema.dump(ans)

    def patch(self, id, cat_id, test_id, task_id, ans_id):
        ans = Ans.query.filter_by(task_id=task_id, ans_id=ans_id).first()
        if 'ans_text' in request.json:
            ans.ans_text = request.json['ans_text']
        if 'ans_correct' in request.json:
            ans.ans_correct = request.json['ans_correct']
        db.session.commit()
        return schemas.ans_schema.dump(ans)

    def delete(self, id, cat_id, test_id, task_id, ans_id):
        ans = Ans.query.filter_by(task_id=task_id, ans_id=ans_id).first()
        db.session.delete(ans)
        db.session.commit()
        return 'Answer removed'


api.add_resource(AnsInTaskById, '/courses/<int:id>/categories/<int:cat_id>/tests/<int:test_id>/tasks/<int:task_id'
                                '>/answers/<int:ans_id>')


class AttInTask(Resource):
    def get(self, id, cat_id, test_id, task_id):
        att = StudentAns.query.filter_by(task_id=task_id)
        return schemas.student_ansrs_schema.dump(att)


api.add_resource(AttInTask, '/courses/<int:id>/categories/<int:cat_id>/tests/<int:test_id>/tasks/<int:task_id>'
                            '/attempts')


class AttInTaskById(Resource):
    def get(self, id, cat_id, test_id, task_id, att_id):
        att = StudentAns.query.filter_by(attempt_id=att_id, task_id=task_id).first()
        return schemas.student_ans_schema.dump(att)


api.add_resource(AttInTaskById, '/courses/<int:id>/categories/<int:cat_id>/tests/<int:test_id>/tasks/<int:task_id'
                                '>/attempts/<int:att_id>')


if __name__ == '__main__':
    app.run()
