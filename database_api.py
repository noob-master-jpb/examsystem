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
    
    
class Reader(Database):
    def table_reader_all(self,table):
        self.control.execute(f"select * from {table} ")
        return self.control.fetchall()
    
    def table_reader_specific(self,table,data,by):
        self.control.execute(f"select * from {table} where {by} = '{data}';")
        return self.control.fetchall()
    
    def table_reader_col(self,table,data,by,row):#error can orrcur in rows
        self.control.execute(f"select ({row}) from {table} where {by} = '{data}'; ")
    
    def personal_data_all(self):
        self.control.execute("select * from personal;")
        return self.control.fetchall()
    
    def personal_data_user(self,user,by="username"):
        self.control.execute(f"""select * from personal where {by} = '{user}';""")
        return self.control.fetchall()
    
    def results_all(self):
        self.control.execute("""
                             select * from results;
                             """)
        return self.control.fetchall()
    
    def results_user(self,user,by = "username"):
        self.control.execute("""
                             select * from results where {by} = '{user}';
                             """)
        return self.control.fetchall()
    

    
