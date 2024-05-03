from flask_sqlalchemy import SQLAlchemy
from datetime import *
db = SQLAlchemy()

class Login(db.Model):
    #unique identifer for every table
    id = db.Column(db.Integer, primary_key=True)

    #actual Columns 
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    #relationship for forgein key
#   <table_name>  <foregin_key format for flask sql alchemy>
    student = db.relationship('Student', backref='login')
    teacher = db.relationship('Teacher', backref='login',)
    account = db.relationship('Accounts', backref='login')
    
    def __getitem__(self, index):
        return {'username':self.username, 'password':self.password}[index]

class Accounts(db.Model):
    id = db.Column(db.Integer,primary_key=True)

    username = db.Column(db.Text,db.ForeignKey('login.username', onupdate="CASCADE"), unique=True, nullable=False)
    type = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    
    

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
    
    def row_all(self):
        return {
            'username':self.username,
            'name':self.name,
            'student_id':self.student_id,
        }
    # def __getitem__(self, index):
        return {'username':self.username, 'name':self.name, 'student_id':self.student_id, 'reg_id':self.reg_id, 'dob':self.dob, 'course':self.course}[index]
    
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.Text, db.ForeignKey('login.username', onupdate="CASCADE"), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    teacher_id = db.Column(db.Integer, unique=True, nullable=False)

    q_paper = db.relationship('QuestionPaper', backref='teacher')
    
    def __getitem__(self, index):
        return {'username':self.username, 'name':self.name, 'teacher_id':self.teacher_id}[index]

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
    
    def row_all(self):
        return {'exam_id':self.exam_id,
                'exam_date':self.exam_date.strftime("%Y-%m-%d"),
                'start_time':self.start_time.strftime("%H:%M:%S"),
                'end_time':self.end_time.strftime("%H:%M:%S"),
                'duration':self.duration.strftime("%H:%M:%S"),
                'exam_name':self.exam_name,'exam_status':self.exam_status}
        
    def __getitem__(self, index):
        return {'exam_id':self.exam_id,
                'exam_date':self.exam_date,'start_time':self.start_time,'end_time':self.end_time,
                'duration':self.duration,
                'exam_name':self.exam_name,'exam_status':self.exam_status}[index]

class QuestionPaper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    exam_id = db.Column(db.Integer, db.ForeignKey('exam_schedule.exam_id', onupdate='CASCADE'),nullable=False)
    q_paper_id = db.Column(db.Integer, unique=True, nullable=False)
    course = db.Column(db.String(50))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.teacher_id', onupdate='CASCADE'))
    question_paper = db.Column(db.LargeBinary, nullable=False)

    answer_key = db.relationship('AnswerKey', backref='question_paper')
    
    def __getitem__(self, index):
        return {'q_paper_id':self.q_paper_id, 'course':self.course, 'teacher_id':self.teacher_id, 'question_paper':self.question_paper}[index]

class AnswerKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    q_paper_id = db.Column(db.Integer, db.ForeignKey('question_paper.q_paper_id', onupdate='CASCADE'), unique=True)
    answer = db.Column(db.LargeBinary)
    
    def __getitem__(self, index):
        return {'q_paper_id':self.q_paper_id, 'answer':self.answer}[index]

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    att_id = db.Column(db.Integer, unique=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id', onupdate="CASCADE"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam_schedule.exam_id', onupdate="CASCADE"), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    
    def count_exam(self):
        return db.session.query(Attendance).filter_by(status=1).count()
    
    def __getitem__(self, index):
        return {'att_id':self.att_id, 'student_id':self.student_id, 'exam_id':self.exam_id, 'status':self.status}[index]
    


class AnswersCollected(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    ans_id = db.Column(db.Integer, unique=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam_schedule.exam_id', onupdate="CASCADE"), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id', onupdate="CASCADE"), nullable=False)
    answer_produced = db.Column(db.LargeBinary)
    
    def __getitem__(self, index):
        return {'ans_id':self.ans_id, 'exam_id':self.exam_id, 'student_id':self.student_id, 'answer_produced':self.answer_produced}[index]

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    result_id = db.Column(db.Integer, unique=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id', onupdate='CASCADE'), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam_schedule.exam_id', onupdate='CASCADE'), nullable=False)
    overall_result = db.Column(db.Integer, nullable=True, default=None)
    evaluated_paper = db.Column(db.Text, nullable=True)


    def row_all(self):
        return {'result_id':self.result_id,
                'student_id':self.student_id,
                'exam_id':self.exam_id,
                'overall_result':self.overall_result}
        
    def __getitem__(self, index):
        return {'result_id':self.result_id,'student_id':self.student_id, 'exam_id':self.exam_id, 
                'overall_result':self.overall_result, 'evaluated_paper':self.evaluated_paper}[index]
    




    
# with app.app_context():
#     db.create_all()