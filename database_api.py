from sqlite3 import connect

con = connect("database.db")
control = con.cursor()
class administrator:
    def __init__(self,database) -> None:
            self.database = database
            self.connection = connect(database)
            self.control = self.connection.cursor()
            
    def login_data_all(self):
        self.control.execute("""
                             select * from login;
                             """)
        return self.control.fetchall()

    def login_data_user(self,user):
        self.control.execute(f"select* from login where username = '{user}';")
        return self.control.fetchall()
    
    def personal_data_all(self):
        self.control.execute("select * from personal data")
    
    def personal_data_user(self,user,by="username"):
        self.control.execute(f"""select * from personal where {by} = '{user}';""")
        return self.control.fetchall()
    
ad = administrator("database.db")


