from flask import *

from models import *
from flask_sqlalchemy import SQLAlchemy
from function_set import json_convertion
from flask_migrate import Migrate

import json
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'


db.init_app(app)

migrate = Migrate(app,db)

with app.app_context():
    file = open("course.json")
    courses = json.load(file)["course_list"]

@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        with app.app_context():
            users = [i.username for i in Login.query.all()]
            if request.form['uname'] in users:
                if Login.query.filter_by(username = request.form['uname']).first().password == request.form['psw']:
                    if request.form['uname'] in [i.username for i in Teacher.query.all()]:
                        return redirect('admin')
                    else:
                        return redirect('student')
    return render_template('login.html')

@app.route('/student')
def student():
    return render_template('student.html')

# @app.route('/admin/homepage')
@app.route('/admin')
def admin_homepage():
    return render_template('index.html',title = 'home')

@app.route('/exams')
def exams():
    # return render_template('admin/exams_panel.html',title = 'exams')
    return render_template('index.html',title = 'exams')

@app.route('/results')
def results():
    return render_template('index.html',title = 'results')
@app.route('/students')
def students():
    return render_template('index.html')

@app.get('/examlist')
def examlist():
    with app.app_context():
        data = [i.row_all() for i in ExamSchedule.query.all()]
        return jsonify(data)




@app.get('/resultlist')
def result_examlist():
    with app.app_context():
        data = []
        attendance_subquery = db.session.query(
        Attendance.exam_id.distinct().label('exam_id'),
        db.func.count(db.func.distinct(Attendance.student_id)).label('attendance_count')
        )\
        .filter(Attendance.status == 1)\
        .group_by('exam_id')\
        .subquery()
        
        query = db.session.query(
        Results.exam_id.distinct().label('exam_id'),  # Take exam_id from Results
        ExamSchedule.exam_name,
        ExamSchedule.exam_date,
        attendance_subquery.c.attendance_count
        )\
        .join(ExamSchedule, Results.exam_id == ExamSchedule.exam_id)\
        .join(attendance_subquery, Results.exam_id == attendance_subquery.c.exam_id)\
        .group_by(Results.exam_id, ExamSchedule.exam_name, attendance_subquery.c.attendance_count)\
        .all()
        
        for i in query:
            data.append({'exam_id':i[0],'exam_name':i[1],'exam_date':i[2].strftime('%Y-%m-%d'),'attendance':i[3]})
        return jsonify(data)
    
    


@app.get('/studentlist')
def userlist():
    with app.app_context():
        data = []
        query = db.session.query(Student,Accounts.status).join(Accounts,Student.username == Accounts.username).all()
        for i in query:
            stud = i[0]
            status = i[1]
            data.append({'username':stud.username,
                         'name':stud.name,
                         'student_id':stud.student_id,
                         'reg_id':stud.reg_id,
                         'dob':stud.dob.strftime('%Y-%m-%d'),
                         'course':stud.course,
                         'status':status})
        return jsonify(data)

@app.get("/courselist")
def courselist():
    with app.app_context():
        global courses
        return jsonify(tuple(courses.keys()))
            

@app.route("/newexam",methods = ["post"])
def new_exam():
    print(request.json)
    data = request.json
    if data["name"] and data["date"] and data["time"] and data["duration"] and data["course_list"]:
        print(data)
    resp = {"request":"recived",
            }
    return jsonify({'server': 'recived'}),200

@app.put("/update_exam")
def update_exam():
    print(request.json)
    return jsonify("hello"),200
if __name__ == '__main__':
    app.run(debug=True,port=80)
