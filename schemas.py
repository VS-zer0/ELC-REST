from flask_marshmallow import Marshmallow
from models import Student, Course, CourseCompletion, Category, Material, Test, TestResults, Task, Ans, StudentAns

ma = Marshmallow()


class StudentSchema(ma.Schema):
    class Meta:
        fields = ("student_id", "email", "password", "firstname", "lastname", "midname", "stream_num", "group_num")
        model = Student

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


class CourseSchema(ma.Schema):
    class Meta:
        fields = ("course_id", "name")
        model = Course

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)


class CompletionSchema(ma.Schema):
    class Meta:
        fields = ("student_id", "course_id", "completion_score", "completion_status")
        model = CourseCompletion

completion_schema = CompletionSchema()
completions_schema = CompletionSchema(many=True)


class CategorySchema(ma.Schema):
    class Meta:
        fields = ("category_id", "course_id", "name", "descr")
        model = Category

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


class MaterialSchema(ma.Schema):
    class Meta:
        fields = ("mat_id", "category_id", "name", "type", "link")
        model = Material

material_schema = MaterialSchema()
materials_schema = MaterialSchema(many=True)


class TestSchema(ma.Schema):
    class Meta:
        fields = ("test_id", "category_id", "name", "number_of_tasks", "date_of_passage")
        model = Test

test_schema = TestSchema()
tests_schema = TestSchema(many=True)


class ResultSchema(ma.Schema):
    class Meta:
        fields = ("attempt_id", "student_id", "test_id", "tasks_completed", "test_score")
        model = TestResults

result_schema = ResultSchema()
results_schema = ResultSchema(many=True)


class TaskSchema(ma.Schema):
    class Meta:
        fields = ("task_id", "test_id", "task_descr")
        model = Task

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


class AnsSchema(ma.Schema):
    class Meta:
        fields = ("task_id", "ans_id", "ans_text", "ans_correct")
        model = Ans

ans_schema = AnsSchema()
ansrs_schema = AnsSchema(many=True)


class StudentAnsSchema(ma.Schema):
    class Meta:
        fields = ("attempt_id", "task_id", "ans_chosen")
        model = StudentAns

student_ans_schema = StudentAnsSchema()
student_ansrs_schema = StudentAnsSchema(many=True)

