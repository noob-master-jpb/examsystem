PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE login (
	id INTEGER NOT NULL, 
	username TEXT NOT NULL, 
	password TEXT NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
);
INSERT INTO login VALUES(1,'johnsmith','123');
INSERT INTO login VALUES(2,'sarahjones','123');
INSERT INTO login VALUES(3,'michaeldavis','123');
INSERT INTO login VALUES(4,'emilybrown','123');
INSERT INTO login VALUES(5,'davidthomas','123');
INSERT INTO login VALUES(6,'jenniferlee','123');
INSERT INTO login VALUES(7,'christopherwilson','123');
INSERT INTO login VALUES(8,'amandaroberts','123');
INSERT INTO login VALUES(9,'matthewjohnson','123');
INSERT INTO login VALUES(10,'laurawilliams','123');
INSERT INTO login VALUES(11,'math_teacher','123');
INSERT INTO login VALUES(12,'bio_teacher','123');
INSERT INTO login VALUES(13,'phys_teacher','123');
INSERT INTO login VALUES(14,'lit_teacher','123');
INSERT INTO login VALUES(15,'hist_teacher','123');
INSERT INTO login VALUES(16,'chem_teacher','123');
INSERT INTO login VALUES(17,'econ_teacher','123');
INSERT INTO login VALUES(18,'math_teacher2','123');
INSERT INTO login VALUES(19,'psych_teacher','123');
INSERT INTO login VALUES(20,'soc_teacher','123');
CREATE TABLE exam_schedule (
	id INTEGER NOT NULL, 
	exam_id INTEGER NOT NULL, 
	exam_date DATE NOT NULL, 
	start_time TIME, 
	end_time TIME, 
	duration TIME, 
	exam_name TEXT NOT NULL, 
	exam_status VARCHAR(20), 
	PRIMARY KEY (id), 
	UNIQUE (exam_id), 
	UNIQUE (exam_name)
);
INSERT INTO exam_schedule VALUES(1,101,'2024-05-15','09:00:00','11:00:00','02:00:00','Math Midterm','live');
INSERT INTO exam_schedule VALUES(2,102,'2024-06-20','10:00:00','12:00:00','02:00:00','Science Final','onwait');
INSERT INTO exam_schedule VALUES(3,103,'2024-07-10','09:30:00','11:30:00','02:00:00','English Final','Live');
INSERT INTO exam_schedule VALUES(4,104,'2024-08-05','10:00:00','12:00:00','02:00:00','Chemistry Midterm','Scheduled');
INSERT INTO exam_schedule VALUES(5,105,'2024-09-15','14:00:00','16:00:00','02:00:00','History Final','Scheduled');
CREATE TABLE accounts (
	id INTEGER NOT NULL, 
	username TEXT NOT NULL, 
	type VARCHAR(20) NOT NULL, 
	status VARCHAR(20) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	FOREIGN KEY(username) REFERENCES login (username) ON UPDATE CASCADE
);
INSERT INTO accounts VALUES(1,'johnsmith','student','active');
INSERT INTO accounts VALUES(2,'sarahjones','student','active');
INSERT INTO accounts VALUES(3,'michaeldavis','student','active');
INSERT INTO accounts VALUES(4,'emilybrown','student','active');
INSERT INTO accounts VALUES(5,'davidthomas','student','active');
INSERT INTO accounts VALUES(6,'jenniferlee','student','active');
INSERT INTO accounts VALUES(7,'christopherwilson','student','active');
INSERT INTO accounts VALUES(8,'amandaroberts','student','active');
INSERT INTO accounts VALUES(9,'matthewjohnson','student','active');
INSERT INTO accounts VALUES(10,'laurawilliams','student','active');
INSERT INTO accounts VALUES(11,'math_teacher','teacher','active');
INSERT INTO accounts VALUES(12,'bio_teacher','teacher','active');
INSERT INTO accounts VALUES(13,'phys_teacher','teacher','active');
INSERT INTO accounts VALUES(14,'lit_teacher','teacher','active');
INSERT INTO accounts VALUES(15,'hist_teacher','teacher','active');
INSERT INTO accounts VALUES(16,'chem_teacher','teacher','active');
INSERT INTO accounts VALUES(17,'econ_teacher','teacher','active');
INSERT INTO accounts VALUES(18,'math_teacher2','teacher','active');
INSERT INTO accounts VALUES(19,'psych_teacher','teacher','active');
INSERT INTO accounts VALUES(20,'soc_teacher','teacher','active');
CREATE TABLE student (
	id INTEGER NOT NULL, 
	username TEXT NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	student_id INTEGER NOT NULL, 
	reg_id TEXT NOT NULL, 
	dob DATE, 
	course VARCHAR(80), 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	FOREIGN KEY(username) REFERENCES login (username) ON UPDATE CASCADE, 
	UNIQUE (student_id), 
	UNIQUE (reg_id)
);
INSERT INTO student VALUES(1,'johnsmith','John Smith',1001,'REG001','1995-08-15','Computer Science');
INSERT INTO student VALUES(2,'sarahjones','Sarah Jones',1002,'REG002','1996-03-20','Biology');
INSERT INTO student VALUES(3,'michaeldavis','Michael Davis',1003,'REG003','1994-11-10','Physics');
INSERT INTO student VALUES(4,'emilybrown','Emily Brown',1004,'REG004','1997-07-25','Literature');
INSERT INTO student VALUES(5,'davidthomas','David Thomas',1005,'REG005','1993-09-05','History');
INSERT INTO student VALUES(6,'jenniferlee','Jennifer Lee',1006,'REG006','1998-02-12','Mathematics');
INSERT INTO student VALUES(7,'christopherwilson','Christopher Wilson',1007,'REG007','1992-05-30','Chemistry');
INSERT INTO student VALUES(8,'amandaroberts','Amanda Roberts',1008,'REG008','1999-06-18','Economics');
INSERT INTO student VALUES(9,'matthewjohnson','Matthew Johnson',1009,'REG009','1991-12-03','Psychology');
INSERT INTO student VALUES(10,'laurawilliams','Laura Williams',1010,'REG010','2000-04-28','Sociology');
CREATE TABLE teacher (
	id INTEGER NOT NULL, 
	username TEXT NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	teacher_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	FOREIGN KEY(username) REFERENCES login (username) ON UPDATE CASCADE, 
	UNIQUE (teacher_id)
);
INSERT INTO teacher VALUES(1,'math_teacher','Math Teacher',2001);
INSERT INTO teacher VALUES(2,'bio_teacher','Biology Teacher',2002);
INSERT INTO teacher VALUES(3,'phys_teacher','Physics Teacher',2003);
INSERT INTO teacher VALUES(4,'lit_teacher','Literature Teacher',2004);
INSERT INTO teacher VALUES(5,'hist_teacher','History Teacher',2005);
INSERT INTO teacher VALUES(6,'chem_teacher','Chemistry Teacher',2006);
INSERT INTO teacher VALUES(7,'econ_teacher','Economics Teacher',2007);
INSERT INTO teacher VALUES(8,'math_teacher2','Math Teacher 2',2008);
INSERT INTO teacher VALUES(9,'psych_teacher','Psychology Teacher',2009);
INSERT INTO teacher VALUES(10,'soc_teacher','Sociology Teacher',2010);
CREATE TABLE attendance (
	id INTEGER NOT NULL, 
	att_id INTEGER, 
	student_id INTEGER NOT NULL, 
	exam_id INTEGER NOT NULL, 
	status INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (att_id), 
	FOREIGN KEY(student_id) REFERENCES student (student_id) ON UPDATE CASCADE, 
	FOREIGN KEY(exam_id) REFERENCES exam_schedule (exam_id) ON UPDATE CASCADE
);
INSERT INTO attendance VALUES(1,1,1001,101,1);
INSERT INTO attendance VALUES(2,2,1002,101,1);
INSERT INTO attendance VALUES(3,3,1003,101,0);
INSERT INTO attendance VALUES(4,4,1004,101,1);
INSERT INTO attendance VALUES(5,5,1005,101,0);
INSERT INTO attendance VALUES(6,6,1006,101,1);
INSERT INTO attendance VALUES(7,7,1007,101,1);
INSERT INTO attendance VALUES(8,8,1008,101,0);
INSERT INTO attendance VALUES(9,9,1009,101,1);
INSERT INTO attendance VALUES(10,10,1010,101,1);
INSERT INTO attendance VALUES(11,11,1001,102,0);
INSERT INTO attendance VALUES(12,12,1002,102,1);
INSERT INTO attendance VALUES(13,13,1003,102,1);
INSERT INTO attendance VALUES(14,14,1004,102,1);
INSERT INTO attendance VALUES(15,15,1005,102,0);
INSERT INTO attendance VALUES(16,16,1006,102,1);
INSERT INTO attendance VALUES(17,17,1007,102,1);
INSERT INTO attendance VALUES(18,18,1008,102,1);
INSERT INTO attendance VALUES(19,19,1009,102,1);
INSERT INTO attendance VALUES(20,20,1010,102,1);
CREATE TABLE answers_collected (
	id INTEGER NOT NULL, 
	ans_id INTEGER, 
	exam_id INTEGER NOT NULL, 
	student_id INTEGER NOT NULL, 
	answer_produced BLOB, 
	PRIMARY KEY (id), 
	UNIQUE (ans_id), 
	FOREIGN KEY(exam_id) REFERENCES exam_schedule (exam_id) ON UPDATE CASCADE, 
	FOREIGN KEY(student_id) REFERENCES student (student_id) ON UPDATE CASCADE
);
INSERT INTO answers_collected VALUES(1,1,101,1001,'PDF content of John Smith answers for Math Midterm');
INSERT INTO answers_collected VALUES(2,2,101,1002,'PDF content of Sarah Jones answers for Math Midterm');
INSERT INTO answers_collected VALUES(4,4,101,1004,'PDF content of Emily Brown  answers for Math Midterm');
INSERT INTO answers_collected VALUES(6,6,101,1006,'PDF content of Jennifer Lee  answers for Math Midterm');
INSERT INTO answers_collected VALUES(7,7,101,1007,'PDF content of Christopher Wilson  answers for Math Midterm');
INSERT INTO answers_collected VALUES(9,9,101,1009,'PDF content of Matthew Johnson  answers for Math Midterm');
INSERT INTO answers_collected VALUES(10,10,101,1010,'PDF content of Laura Williams  answers for Math Midterm');
INSERT INTO answers_collected VALUES(12,12,102,1002,'PDF content of Sarah Jones  answers for Science Final');
INSERT INTO answers_collected VALUES(13,13,102,1003,'PDF content of Michael Davis  answers for Science Final');
INSERT INTO answers_collected VALUES(14,14,102,1004,'PDF content of Emily Brown  answers for Science Final');
INSERT INTO answers_collected VALUES(16,16,102,1006,'PDF content of Jennifer Lee  answers for Science Final');
INSERT INTO answers_collected VALUES(17,17,102,1007,'PDF content of Christopher Wilson  answers for Science Final');
INSERT INTO answers_collected VALUES(18,18,102,1008,'PDF content of Amanda Roberts  answers for Science Final');
INSERT INTO answers_collected VALUES(19,19,102,1009,'PDF content of Matthew Johnson  answers for Science Final');
INSERT INTO answers_collected VALUES(20,20,102,1010,'PDF content of Laura Williams  answers for Science Final');
CREATE TABLE results (
	id INTEGER NOT NULL, 
	result_id INTEGER, 
	student_id INTEGER NOT NULL, 
	exam_id INTEGER NOT NULL, 
	overall_result INTEGER, 
	evaluated_paper TEXT, 
	PRIMARY KEY (id), 
	UNIQUE (result_id), 
	FOREIGN KEY(student_id) REFERENCES student (student_id) ON UPDATE CASCADE, 
	FOREIGN KEY(exam_id) REFERENCES exam_schedule (exam_id) ON UPDATE CASCADE
);
INSERT INTO results VALUES(1,1,1001,101,85,'John Smith did well overall.');
INSERT INTO results VALUES(2,2,1002,101,70,'Sarah Jones needs improvement in certain areas.');
INSERT INTO results VALUES(4,4,1004,101,75,'Emily Brown needs to focus more on specific topics.');
INSERT INTO results VALUES(6,6,1006,101,90,'Jennifer Lee demonstrated a strong understanding.');
INSERT INTO results VALUES(7,7,1007,101,80,'Christopher Wilson showed solid performance.');
INSERT INTO results VALUES(9,9,1009,101,88,'Matthew Johnson showed great improvement.');
INSERT INTO results VALUES(10,10,1010,101,92,'Laura Williams excelled in all sections.');
INSERT INTO results VALUES(12,12,1002,102,70,'Sarah Jones needs improvement in certain areas.');
INSERT INTO results VALUES(13,13,1003,102,95,'Michael Davis performed exceptionally.');
INSERT INTO results VALUES(14,14,1004,102,75,'Emily Brown needs to focus more on specific topics.');
INSERT INTO results VALUES(16,16,1006,102,90,'Jennifer Lee demonstrated a strong understanding.');
INSERT INTO results VALUES(17,17,1007,102,80,'Christopher Wilson showed solid performance.');
INSERT INTO results VALUES(18,18,1008,102,65,'Amanda Roberts needs to review the material thoroughly.');
INSERT INTO results VALUES(19,19,1009,102,88,'Matthew Johnson showed great improvement.');
INSERT INTO results VALUES(20,20,1010,102,92,'Laura Williams excelled in all sections.');
CREATE TABLE answer_key (
	id INTEGER NOT NULL, 
	q_paper_id INTEGER, 
	answer BLOB, 
	PRIMARY KEY (id), 
	UNIQUE (q_paper_id), 
	FOREIGN KEY(q_paper_id) REFERENCES question_paper (q_paper_id) ON UPDATE CASCADE
);
INSERT INTO answer_key VALUES(1,1,'Answer key for Math Midterm');
INSERT INTO answer_key VALUES(2,2,'Answer key for Science Final');
INSERT INTO answer_key VALUES(3,3,'Answer key for English Final');
INSERT INTO answer_key VALUES(4,4,'Answer key for Chemistry Midterm');
INSERT INTO answer_key VALUES(5,5,'Answer key for History Final');
INSERT INTO answer_key VALUES(6,6,'Answer key for Physics Midterm');
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
INSERT INTO alembic_version VALUES('10bb02479d89');
CREATE TABLE IF NOT EXISTS "question_paper" (
	id INTEGER NOT NULL, 
	exam_id INTEGER NOT NULL, 
	q_paper_id INTEGER NOT NULL, 
	course VARCHAR(50), 
	teacher_id INTEGER, 
	question_paper BLOB NOT NULL, 
	PRIMARY KEY (id), 
	CONSTRAINT unique_exam_id_course UNIQUE (exam_id, course), 
	FOREIGN KEY(teacher_id) REFERENCES teacher (teacher_id) ON UPDATE CASCADE, 
	UNIQUE (q_paper_id), 
	FOREIGN KEY(exam_id) REFERENCES exam_schedule (exam_id) ON UPDATE CASCADE
);
INSERT INTO question_paper VALUES(1,101,1,'Math',2001,'PDF content of Math question paper for Math Midterm');
INSERT INTO question_paper VALUES(2,102,2,'Science',2002,'PDF content of Science question paper for Science Final');
INSERT INTO question_paper VALUES(3,103,3,'English',2004,'PDF content of English question paper for English Final');
INSERT INTO question_paper VALUES(4,104,4,'Chemistry',2006,'PDF content of Chemistry question paper for Chemistry Midterm');
INSERT INTO question_paper VALUES(5,105,5,'History',2005,'PDF content of History question paper for History Final');
INSERT INTO question_paper VALUES(6,102,6,'Physics',2003,'PDF content of Physics question paper for Physics Midterm');
COMMIT;
