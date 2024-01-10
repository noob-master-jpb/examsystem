from sqlite3 import connect

con = connect("abc.db")
control = con.cursor()

control.execute("""
CREATE TABLE results (
  username char(15) DEFAULT NULL,
  registration_no char(50) DEFAULT NULL,
  student_id int DEFAULT NULL,
  exam_id int DEFAULT NULL,
  overall_result int DEFAULT NULL,
  evaluated_paper longblob,
  CONSTRAINT results_fk FOREIGN KEY(username) references login(username) on update cascade,
  CONSTRAINT results_fk FOREIGN KEY(registration_no) references personal(registration_no) on update cascade,
  CONSTRAINT results_fk FOREIGN KEY(student_id) references personal(student_id) on update cascade,
  CONSTRAINT results_fk FOREIGN KEY(exam_id) references exam_schedule(exam_id) on update cascade
  );
""")
