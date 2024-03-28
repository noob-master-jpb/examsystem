CREATE TABLE IF NOT EXISTS "login" (
  username TEXT NOT NULL PRIMARY KEY,
  password TEXT NOT NULL
);

CREATE TABLE exam_schedule(
  exam_id int NOT NULL PRIMARY KEY,
  exam_date date DEFAULT NULL,
  start_time time DEFAULT NULL,
  end_time time DEFAULT NULL,
  duration time DEFAULT NULL, 
  exam_name char(50),
  exam_status char(10) DEFAULT upcoming
);


CREATE TABLE IF NOT EXISTS "students"(
  username TEXT UNIQUE,
  name TEXT,
  student_id INT NOT NULL UNIQUE,
  registration_no TEXT NOT NULL UNIQUE,
  dob Date,
  course TEXT,
  CONSTRAINT std_uname 
  FOREIGN KEY(username) loginREFERENCES (username)
  ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "teachers"(
    username TEXT NOT NULL,
    Name varchar(30),
    teacher_id int NOT NULL PRIMARY KEY,
    dob date,

    CONSTRAINT teacher_uname 
    FOREIGN KEY(username) REFERENCES login(username) 
    ON UPDATE CASCADE
);

CREATE TABLE qustion_paper (
  exam_id int DEFAULT NULL UNIQUE,
  q_paper_id int NOT NULL PRIMARY KEY ,
  "course" char(20) DEFAULT NULL,
  teacher_id int NOT NULL UNIQUE,
  qustion_paper longblob,

  CONSTRAINT q_paper_exam_id 
  FOREIGN KEY (exam_id) REFERENCES exam_schedule (exam_id) 
  ON UPDATE CASCADE,

  CONSTRAINT q_paper_t_id
  FOREIGN KEY (teacher id) REFERENCES teachers(techer_id)
  ON UPDATE CASCADE
);

CREATE TABLE answer_key (
  q_paper_id int NOT NULL UNIQUE,
  answer longblob,

  CONSTRAINT a_key_q_paper_id 
  FOREIGN KEY (q_paper_id) REFERENCES qustion_paper(q_paper_id)
  ON UPDATE CASCADE
);

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

CREATE TABLE IF NOT EXISTS "answer_collected"(
  ans_id int,
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

CREATE TABLE IF NOT EXISTS "results" (
  student_id int DEFAULT NULL,
  exam_id int DEFAULT NULL,
  result_id int NOT NULL UNIQUE,
  overall_result int DEFAULT NULL,
  evaluated_paper longblob, 

  CONSTRAINT results_st_id
  FOREIGN KEY(student_id) references students(student_id) 
  on update cascade,

  CONSTRAINT results_exam_id
  FOREIGN KEY(exam_id) references exam_schedule(exam_id) 
  on update cascade
  );

