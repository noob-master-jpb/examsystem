from flask import *

from models import *
from flask_sqlalchemy import SQLAlchemy
from function_set import json_convertion
import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'



db.init_app(app)

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

@app.route('/admin')
def admin():
    return render_template('admin/homepage.html',title = 'home')

@app.route('/exams')
def exams():
    return render_template('admin/exams_panel.html',title = 'exams')

@app.get('/examlist')
def examlist():
    with app.app_context():
        data = [i.row_all() for i in ExamSchedule.query.all()]
        return jsonify(data)


@app.route('/results')
def results():
    return render_template('admin/results_panel.html',title = 'results')

@app.get('/result_examlist')
def result_examlist():
    with app.app_context():
        data=[]
        query = db.session.query(ExamSchedule.exam_name,ExamSchedule.exam_id,ExamSchedule.exam_date,db.func.count(Attendance.id))\
            .join(Attendance)\
                .filter(Attendance.status == 1)\
                    .group_by(ExamSchedule.exam_id).all()
        for i in query:
            data.append({'Exam_name':i[0],'Exam_id':i[1],'Exam_date':i[2].strftime('%Y-%m-%d'),'Attendance':i[3]})
        return data
    


@app.get('/studentlist')
def userlist():
    with app.app_context():
        data = [i.row_all() for i in Student.query.all()]
        return jsonify(data)


print(result_examlist())
            
if __name__ == '__main__':
    app.run(debug=True,port=80)
