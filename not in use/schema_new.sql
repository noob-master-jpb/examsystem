PRAGMA foreign_keys=OFF;

BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "login" (
  username TEXT NOT NULL PRIMARY KEY,
  password TEXT NOT NULL
);
INSERT INTO login VALUES('john_doe','123');
INSERT INTO login VALUES('emma_davis','123');
INSERT INTO login VALUES('charlie_miller','123');
INSERT INTO login VALUES('alice_smith','123');
INSERT INTO login VALUES('bob_jones','123');
INSERT INTO login VALUES('jane_smith','123');
INSERT INTO login VALUES('rahul_gupta','123');
INSERT INTO login VALUES('priya_sharma','123');
INSERT INTO login VALUES('amit_patel','123');

CREATE TABLE exam_schedule (
  exam_id int NOT NULL PRIMARY KEY,
  exam_date date DEFAULT NULL,
  start_time time DEFAULT NULL,
  end_time time DEFAULT NULL,
  duration time DEFAULT NULL, 
  exam_name char(50),
  "exam_status" char(10));

INSERT INTO exam_schedule VALUES(1,'2024-01-15','09:00:00','12:00:00','03:00:00','sem1','finished');
INSERT INTO exam_schedule VALUES(4,'2024-03-10','09:00:00','12:00:00','03:00:00','sem2','pending');
INSERT INTO exam_schedule VALUES(5,'2024-03-25','13:30:00','16:30:00','03:00:00','sem3','pending');
INSERT INTO exam_schedule VALUES(2,'2024-02-01','10:30:00','13:30:00','03:00:00','sem4','finished');
INSERT INTO exam_schedule VALUES(3,'2024-02-15','14:00:00','17:00:00','03:00:00','sem5','pending');

CREATE TABLE IF NOT EXISTS "students"(
  username TEXT UNIQUE,
  name TEXT,
  student_id INT NOT NULL UNIQUE,
  registration_no TEXT NOT NULL UNIQUE,
  dob NUM,
  course TEXT,
  CONSTRAINT std_uname 
  FOREIGN KEY(username) REFERENCES login(username)
  ON UPDATE CASCADE
);

INSERT INTO students VALUES('emma_davis','Emma Davis',1004,'REG101','1993-08-15','Physics');
INSERT INTO students VALUES('charlie_miller','Charlie Miller',1005,'REG202','1994-04-25','Chemistry');
INSERT INTO students VALUES('jane_smith','Jane Smith',1002,'REG002','2000-02-02','Engineering');
INSERT INTO students VALUES('rahul_gupta','Rahul Gupta',1003,'REG003','2001-05-15','Computer Science');
INSERT INTO students VALUES('priya_sharma','Priya Sharma',1006,'REG009','2000-08-20','Electrical Engineering');
INSERT INTO students VALUES('amit_patel','Amit Patel',1007,'REG008','1999-12-10','Civil Engineering');

CREATE TABLE IF NOT EXISTS "teachers"(
    username TEXT NOT NULL,
    Name varchar(30),
    teacher_id int NOT NULL PRIMARY KEY,
    dob date,

    CONSTRAINT teacher_uname 
    FOREIGN KEY(username) REFERENCES login(username) 
    ON UPDATE CASCADE
);

INSERT INTO teachers VALUES('john_doe','John Doe',1001,'1990-01-15');
INSERT INTO teachers VALUES('alice_smith','Alice Smith',1004,'1982-09-10');
INSERT INTO teachers VALUES('bob_jones','Bob Jones',1005,'1978-03-25');

CREATE TABLE qustion_paper (
  exam_id int DEFAULT NULL UNIQUE,
  q_paper_id int NOT NULL PRIMARY KEY ,
  "course" char(20) DEFAULT NULL,
  qustion_paper longblob,

  CONSTRAINT q_paper_exam_id 
  FOREIGN KEY (exam_id) REFERENCES exam_schedule (exam_id) 
  ON UPDATE CASCADE
);

INSERT INTO qustion_paper VALUES(1,101,'Computer Science','Sample Question Paper Data');
INSERT INTO qustion_paper VALUES(4,104,'Physics','Physics Questions Data');
INSERT INTO qustion_paper VALUES(5,105,'Chemistry','Chemistry Questions Data');
INSERT INTO qustion_paper VALUES(2,102,'Biology','Biology Questions Data');
INSERT INTO qustion_paper VALUES(3,103,'Mathematics','Math Questions Data');

CREATE TABLE answer_key (
  q_paper_id int NOT NULL UNIQUE,
  answer longblob,

  CONSTRAINT a_key_q_paper_id 
  FOREIGN KEY (q_paper_id) REFERENCES qustion_paper(q_paper_id)
  ON UPDATE CASCADE
);

INSERT INTO answer_key VALUES(104,'Correct Physics Answers Data');
INSERT INTO answer_key VALUES(105,'Correct Chemistry Answers Data');
INSERT INTO answer_key VALUES(101,'sample');
INSERT INTO answer_key VALUES(102,'sample');
INSERT INTO answer_key VALUES(103,'sample');

CREATE TABLE IF NOT EXISTS "attendance"(
  id int NOT NULL PRIMARY KEY,
  student_id int NOT NULL,
  exam_id int NOT NULL,
  status int NOT NULL,

  CONSTRAINT attendance_st_id
  FOREIGN KEY(student_id) references students(student_id) 
  on update cascade,

  CONSTRAINT attendance_exam_id 
  FOREIGN KEY(exam_id) references exam_schedule(exam_id) 
  on update cascade
);

INSERT INTO attendance VALUES(2,1004,2,1);
INSERT INTO attendance VALUES(3,1005,3,0);
INSERT INTO attendance VALUES(6,1002,1,1);
INSERT INTO attendance VALUES(4,1003,1,1);
INSERT INTO attendance VALUES(5,1006,2,1);
INSERT INTO attendance VALUES(7,1007,2,0);

CREATE TABLE IF NOT EXISTS "answer_collected"(
  exam_id INT,
  student_id INT,
  answer_produced longblob,

  CONSTRAINT ans_collect_exam_id 
  FOREIGN KEY(exam_id) REFERENCES exam_schedule(exam_id)
  ON UPDATE CASCADE,

  CONSTRAINT ans_collect_std_id 
  FOREIGN KEY(student_id) REFERENCES students(student_id)
  ON UPDATE CASCADE
);

INSERT INTO answer_collected VALUES(4,1004,'Physics Answers Data');
INSERT INTO answer_collected VALUES(5,1005,'Chemistry Answers Data');
INSERT INTO answer_collected VALUES(1,1002,'Sample answer produced ');
INSERT INTO answer_collected VALUES(1,1003,'Sample answer produced ');
INSERT INTO answer_collected VALUES(2,1006,'Sample answer produced ');
INSERT INTO answer_collected VALUES(2,1007,'Sample answer produced ');

CREATE TABLE IF NOT EXISTS "results" (
  student_id int DEFAULT NULL,
  exam_id int DEFAULT NULL,
  overall_result int DEFAULT NULL,
  evaluated_paper longblob, 

  CONSTRAINT results_st_id
  FOREIGN KEY(student_id) references students(student_id) 
  on update cascade,

  CONSTRAINT results_exam_id
  FOREIGN KEY(exam_id) references exam_schedule(exam_id) 
  on update cascade
  );

INSERT INTO results VALUES(1004,4,88,'Physics Exam Evaluated Data');
INSERT INTO results VALUES(1005,5,95,'Chemistry Exam Evaluated Data');
INSERT INTO results VALUES(1002,1,85,'Sample evaluated paper for student 1002');
INSERT INTO results VALUES(1003,1,78,'Sample evaluated paper for student 1003');
INSERT INTO results VALUES(1006,2,92,'Sample evaluated paper for student 1006');
INSERT INTO results VALUES(1007,2,70,'Sample evaluated paper for student 1007');

COMMIT;
