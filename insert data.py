from datetime import datetime,time
from app import db,app  # Assuming you have your SQLAlchemy instance named db
from models import Login, Student, Teacher, ExamSchedule, QuestionPaper, AnswerKey, Attendance, AnswersCollected, Results

# Sample Login data
logins = [
    Login(username='johndoe', password='123'),
    Login(username='janesmith', password='123'),
    Login(username='mrsmith', password='123'),
    Login(username='alicejohnson', password='123'),
    Login(username='mrsjohnson', password='123'),
    Login(username='bobbrown', password='123'),
    Login(username='emilywilson', password='123'),
    Login(username='drjohn', password='123'),
    Login(username='profwilson', password='123'),
    Login(username='johnson', password='123'),
    Login(username='drmillers', password='123')
]

# Sample Student data
students = [
    Student(username='johndoe', name='John Doe', student_id=1001, reg_id='REG001', dob=datetime(2000, 1, 1), course='Computer Science'),
    Student(username='janesmith', name='Jane Smith', student_id=1002, reg_id='REG002', dob=datetime(2001, 2, 2), course='Mathematics'),
    Student(username='alicejohnson', name='Alice Johnson', student_id=1003, reg_id='REG003', dob=datetime(2002, 3, 3), course='Physics'),
    Student(username='bobbrown', name='Bob Brown', student_id=1004, reg_id='REG004', dob=datetime(2003, 4, 4), course='Chemistry'),
    Student(username='emilywilson', name='Emily Wilson', student_id=1005, reg_id='REG005', dob=datetime(2004, 5, 5), course='Biology')
]

# Sample Teacher data
teachers = [
    Teacher(username='mrsmith', name='Mr. Smith', teacher_id=2001),
    Teacher(username='mrsjohnson', name='Mrs. Johnson', teacher_id=2002),
    Teacher(username='drjohn', name='Dr. John', teacher_id=2003),
    Teacher(username='profwilson', name='Prof. Wilson', teacher_id=2004),
    Teacher(username='drmillers', name='Dr. Miller', teacher_id=2005)
]

# Sample ExamSchedule data
exams = [
    ExamSchedule(exam_id=1, exam_date=datetime(2024, 1, 15).date(), start_time=time(9, 0, 0), end_time=time(12, 0, 0), duration=time(3, 0, 0), exam_name='Semester 1', exam_status='Upcoming'),
    ExamSchedule(exam_id=2, exam_date=datetime(2024, 2, 15).date(), start_time=time(9, 0, 0), end_time=time(12, 0, 0), duration=time(3, 0, 0), exam_name='Semester 2', exam_status='Upcoming'),
    ExamSchedule(exam_id=3, exam_date=datetime(2024, 3, 15).date(), start_time=time(9, 0, 0), end_time=time(12, 0, 0), duration=time(3, 0, 0), exam_name='Semester 3', exam_status='Upcoming'),
    ExamSchedule(exam_id=4, exam_date=datetime(2024, 4, 15).date(), start_time=time(9, 0, 0), end_time=time(12, 0, 0), duration=time(3, 0, 0), exam_name='Semester 4', exam_status='Upcoming'),
    ExamSchedule(exam_id=5, exam_date=datetime(2024, 5, 15).date(), start_time=time(9, 0, 0), end_time=time(12, 0, 0), duration=time(3, 0, 0), exam_name='Semester 5', exam_status='Upcoming')
]
# Sample QuestionPaper data
question_papers = [
    QuestionPaper(exam_id=1, q_paper_id=101, course='Computer Science', teacher_id=2001, question_paper=b'Binary Data 1'),
    QuestionPaper(exam_id=2, q_paper_id=102, course='Mathematics', teacher_id=2002, question_paper=b'Binary Data 2'),
    QuestionPaper(exam_id=3, q_paper_id=103, course='Physics', teacher_id=2003, question_paper=b'Binary Data 3'),
    QuestionPaper(exam_id=4, q_paper_id=104, course='Chemistry', teacher_id=2004, question_paper=b'Binary Data 4'),
    QuestionPaper(exam_id=5, q_paper_id=105, course='Biology', teacher_id=2005, question_paper=b'Binary Data 5')
]

# Sample AnswerKey data
answer_keys = [
    AnswerKey(q_paper_id=101, answer=b'Answer Data 1'),
    AnswerKey(q_paper_id=102, answer=b'Answer Data 2'),
    AnswerKey(q_paper_id=103, answer=b'Answer Data 3'),
    AnswerKey(q_paper_id=104, answer=b'Answer Data 4'),
    AnswerKey(q_paper_id=105, answer=b'Answer Data 5')
]

# Sample Attendance data
attendances = [
    Attendance(att_id=1, student_id=1001, exam_id=1, status=1),
    Attendance(att_id=2, student_id=1002, exam_id=1, status=1),
    Attendance(att_id=3, student_id=1003, exam_id=1, status=0),
    Attendance(att_id=4, student_id=1004, exam_id=1, status=0),
    Attendance(att_id=5, student_id=1005, exam_id=1, status=0)
]

# Sample AnswersCollected data
answers_collected = [
    AnswersCollected(ans_id=1, exam_id=1, student_id=1001, answer_produced=b'Produced Answer 1'),
    AnswersCollected(ans_id=2, exam_id=1, student_id=1002, answer_produced=b'Produced Answer 2'),
    AnswersCollected(ans_id=3, exam_id=1, student_id=1003, answer_produced=b'Produced Answer 3'),
    AnswersCollected(ans_id=4, exam_id=1, student_id=1004, answer_produced=b'Produced Answer 4'),
    AnswersCollected(ans_id=5, exam_id=1, student_id=1005, answer_produced=b'Produced Answer 5')
]

# Sample Results data
results = [
    Results(result_id=1, student_id=1001, exam_id=1,overall_result = 80,evaluated_paper='sample data'),
    Results(result_id=2, student_id=1002, exam_id=1,overall_result = 80,evaluated_paper='sample data'),
    Results(result_id=3, student_id=1003, exam_id=1,overall_result = 80,evaluated_paper='sample data'),
    Results(result_id=4, student_id=1004, exam_id=1,overall_result = 80,evaluated_paper='sample data'),
    Results(result_id=5, student_id=1005, exam_id=1,overall_result = 80,evaluated_paper='sample data')
]

# Add data to the database
with app.app_context():
    for obj in logins + students + teachers + exams + question_papers + answer_keys + attendances + answers_collected + results:
        db.session.add(obj)
    db.session.commit()
