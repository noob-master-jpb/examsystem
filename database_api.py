from distutils.util import execute
from sqlite3 import connect

con = connect("database.db")
control = con.cursor()

class Database:
    def __init__(self,database) -> None:
            self.database = database
            self.connection = connect(database)
            self.control = self.connection.cursor()

class Login(Database):
    def login_data_all(self):
        self.control.execute("""
                             select * from login;
                             """)
        return self.control.fetchall()
    
    def login_data_user(self,user):
        self.control.execute(f"select* from login where username = '{user}';")
        return self.control.fetchall()
    
class System_controler(Database):
    def table_reader_all(self,table):
        self.control.execute(f"select * from {table} ")
        return self.control.fetchall()
    
    def table_reader_specific(self,table,data,by):
        self.control.execute(f"select * from {table} where {by} = '{data}';")
        return self.control.fetchall()
    
    def table_reader_col(self,table,data,by,row):#error can orrcur in rows
        self.control.execute(f"select ({row}) from {table} where {by} = '{data}'; ")
        
class Reader(Database):
    def personal_data_all(self):
        self.control.execute("select * from personal;")
        return self.control.fetchall()
    
    def personal_data(self,user,by="username"):
        self.control.execute(f"""select * from personal where {by} = '{user}';""")
        return self.control.fetchall()
    
    def qustion_paper_all(self):
        self.control.execute("select * from qustion_paper")
        return self.control.fetchall()
    
    def qustion_paper(self,course,by="q_paper_id"):
        self.control.execute(f"select * from qustion_paper where {by} = {course}")
        return self.control.fetchall()
    
    def exam_scheule_all(self):
        self.control.execute("select * from exam_schedule")
        return self.control.fetchall()
    
    def exam_schedule(self,id,by = "exam_id"):
        self.control.execute(f"select * from exam_schedule {by} = '{id}' ")
    
    def results_all(self):
        self.control.execute("select * from results;")
        return self.control.fetchall()
    
    def results(self,user,by = "username"):
        self.control.execute("""
                             select * from results where {by} = '{user}';
                             """)
        return self.control.fetchall()
    
class Writer(Database):
    def add_personal(self,lis=[],into=''):
        if not lis:
            return
        if into == '':
            into = "(username, name, student_id, registration_no, dob, course)"
        self.control.executemany(f"insert into table personal {into} value(?,?,?,?,?,?,)",lis)
        
    def shedule_exam(self,lis=[],into = "(exam_id, exam_date, start_time, end_time, duration)")

    
    
