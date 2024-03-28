from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    student = db.relationship('Student', backref='login', uselist=False)
    teacher = db.relationship('Teacher', backref='login', uselist=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.Text, db.ForeignKey('login.username', onupdate="CASCADE"), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    student_id = db.Column(db.Integer, unique=True, nullable=False)
    reg_id = db.Column(db.Text, unique=True, nullable=False)
    dob = db.Column(db.Date)
    course = db.Column(db.String(80))

    attendance = db.relationship('Attendance', backref='student')
    answers_col = db.relationship('AnswersCollected', backref='student')
    result = db.relationship('Results', backref='student')

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.Text, db.ForeignKey('login.username', onupdate="CASCADE"), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    teacher_id = db.Column(db.Integer, unique=True, nullable=False)

    q_paper = db.relationship('QuestionPaper', backref='teacher')

class ExamSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    exam_id = db.Column(db.Integer, unique=True, nullable=False)
    exam_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    duration = db.Column(db.Time)
    exam_name = db.Column(db.Text, nullable=False, unique=True)
    exam_status = db.Column(db.String(20), default='Upcoming')

    question_paper = db.relationship('QuestionPaper', backref='exam_schedule')
    attendance = db.relationship('Attendance', backref='exam_schedule')
    answers_col = db.relationship('AnswersCollected', backref='exam_schedule')
    result = db.relationship('Results', backref='exam_schedule')

class QuestionPaper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    exam_id = db.Column(db.Integer, db.ForeignKey('exam_schedule.exam_id', onupdate='CASCADE'), unique=True, nullable=False)
    q_paper_id = db.Column(db.Integer, unique=True, nullable=False)
    course = db.Column(db.String(50))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id', onupdate='CASCADE'))
    question_paper = db.Column(db.LargeBinary, nullable=False)

    answer_key = db.relationship('AnswerKey', backref='question_paper')

class AnswerKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    q_paper_id = db.Column(db.Integer, db.ForeignKey('question_paper.q_paper_id', onupdate='CASCADE'), unique=True)
    answer = db.Column(db.LargeBinary)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    att_id = db.Column(db.Integer, unique=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', onupdate="CASCADE"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam_schedule.exam_id', onupdate="CASCADE"), nullable=False)
    status = db.Column(db.Integer, nullable=False)

class AnswersCollected(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    ans_id = db.Column(db.Integer, unique=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam_schedule.exam_id', onupdate="CASCADE"), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', onupdate="CASCADE"), nullable=False)
    answer_produced = db.Column(db.LargeBinary)

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    result_id = db.Column(db.Integer, unique=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', onupdate='CASCADE'), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam_schedule', onupdate='CASCADE'), nullable=False)
    overall_result = db.Column(db.Integer, nullable=True, default=None)
    evaluated_paper = db.Column(db.Text, nullable=True)

    
# with app.app_context():
#     db.create_all()