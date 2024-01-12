from flask import *
from sqlite3 import *

app = Flask(__name__)
DATABASE = "database.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


class Database:
    def __init__(self,database) -> None:
            self.connection = database
            self.control = self.connection.cursor()
            

class Login(Database):
    def login_data_all(self):
        self.control.execute("""
                             select * from login;
                             """)
        return self.control.fetchall()
    
    def login_data_user(self,user,by ="username",what = '*'):
        self.control.execute(f"select {what} from login where {by} = '{user}';")
        return self.control.fetchall()

    def admin_list(self):
        self.admin_list = self.login_data_user("true","admin")  
        return [i[0] for i in self.admin_list]

    def add_user(self,lis=[]):
        if not lis:
            return
        self.control.executemany("insert into login (username,passwprd) values(?,?,?,)",lis)
        
class System_controler(Database):
    def run(self,data='',ret = 0):
        self.control.execute(data)
        if ret != 0:
            return self.control.fetchall()
        
    def table_reader_all(self,table):
        self.control.execute(f"select * from {table} ;")
        return self.control.fetchall()
    
    def table_reader_specific(self,table,data,by):
        self.control.execute(f"select * from {table} where {by} = '{data}';")
        return self.control.fetchall()
    
    def table_reader_col(self,table,data,by,row):#error can orrcur in rows
        self.control.execute(f"select ({row}) from {table} where {by} = '{data}'; ")
    
    def read_answer_collected(self,data,by = 'exam_id'):
        self.control.execute(f"select * from answer_collected where {by} = {data};")
        return self.control.fetchall()
    
    def read_answer_key(self,data,by="q_paper_id"):
        self.control.execute(f"select * from answer_key where {by} = {data};")
        return self.control.fetchall()
    
    def add_result(self,lis=[]):
        if not lis:
            return
        self.control.executemany("""insert into results 
                                 (username, registration_no, student_id, exam_id, overall_result, evaluated_paper) 
                                 ;values(?,?,?,?,?,?,);""",lis)
    
class Reader(Database):
    def personal_data_all(self):
        self.control.execute("select * from personal;")
        return self.control.fetchall()
    
    def personal_data(self,user,by="username"):
        self.control.execute(f"""select * from personal where {by} = '{user}';""")
        return self.control.fetchall()
    
    def qustion_paper_all(self):
        self.control.execute("select * from qustion_paper;")
        return self.control.fetchall()
    
    def qustion_paper(self,course,by="q_paper_id"):
        self.control.execute(f"select * from qustion_paper where {by} = {course};")
        return self.control.fetchall()
    
    def exam_schedule_all(self):
        self.control.execute("select * from exam_schedule;")
        return self.control.fetchall()
    
    def exam_schedule(self,id,by = "exam_id"):
        self.control.execute(f"select * from exam_schedule {by} = '{id}' ;")
    
    def results_all(self):
        self.control.execute("select * from results;")
        return self.control.fetchall()
    
    def results(self,user,by = "username"):
        self.control.execute(f"""
                             select * from results where {by} = '{user}';
                             """)
        return self.control.fetchall()
    
class Writer(Database):
    def add_personal(self,lis=[],into=''):
        if not lis:
            return
        if into == '':
            into = "username, name, student_id, registration_no, dob, course"
        self.control.executemany(f"insert into personal ({into}) values(?,?,?,?,?,?,);",lis)
        
    def shedule_exam(self,lis=[],into = "exam_id, exam_date, start_time, end_time, duration"):
        if not lis:
            return
        self.control.executemany(f"insert into exam_schedule ({into}) values(?,?,?,?,?,);",lis)

    def add_qustion_paper(self,lis=[],into = "exam_id, q_paper_id, course, Qustion_paper"):
        if not lis:
            return
        self.control.executemany(f"insert into qustion_paper ({into}) values (?,?,?,?,);",lis)
             
class Answer_collection(Database):
    def Collect_Answer(self,lis=[]):
        if not lis:
            return
        self.control.executemany("""insert into answer_collected (exam_id,q_paper_id,student_id,registration_no,answer_produced)
                                 values(?,?,?,?,?,);""",lis)
        
class Answer_key(Database):
    def add_answer_key(self,lis=[]):
        if not lis:
            return
        self.control.executemany("insert into answer_key (examid, q_paper_id, answer) values(?,?,?,);",lis)

class Administrator(Reader,Writer,Login,System_controler,Answer_collection,Answer_key,):
    def ret_admin(self):
        self.admin_list = self.login_data_user("true","admin")

# with app.app_context():
#     au = Login(get_db())
#     print(au.admin_list())

@app.route("/",methods = ["GET","POST"])
def test_page():
    if request.method == "POST":
        user = request.form['uname']
        psw = request.form['psw']
        with app.app_context():
            auth = Login(get_db())
            print(auth.login_data_user(user,what = 'password'))
            print(psw)
            if psw == auth.login_data_user(user,what = 'password')[0][0]:
                if user in auth.admin_list():
                    return "hello admin"
                return redirect(url_for("student",userid = user))
    return render_template("login.html")

@app.route("/dashboard/<userid>")
def student(userid):
    with app.app_context():
        read = Reader(get_db())
        userdata = read.personal_data(userid)
        userdata=userdata[0]
        exams = read.exam_schedule_all()
        return render_template('student.html', exam = exams,userid = userdata[1],std_id =userdata[2],reg_no = userdata[3],dob = userdata[4],course = userdata[5])
    
if __name__ == '__main__':
    app.run(debug=True,port=80)