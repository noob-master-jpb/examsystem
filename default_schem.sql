DROP TABLE IF EXISTS login;

CREATE TABLE login (
  username char(15) NOT NULL PRIMARY KEY,
  password varchar(5000) NOT NULL,
  admin bool Not NULL
);

DROP TABLE IF EXISTS personal;

CREATE TABLE personal (
  username char(15) NOT NULL,
  name char(20) NOT NULL,
  student_id int NOT NULL PRIMARY KEY,
  registration_no varchar(50) NOT NULL UNIQUE,
  dob date NOT NULL,
  course char(20) NOT NULL,
  CONSTRAINT personal_fk FOREIGN KEY (username) REFERENCES login (username) ON UPDATE CASCADE
);

DROP TABLE IF EXISTS exam_schedule;
CREATE TABLE exam_schedule (
  exam_id int NOT NULL PRIMARY KEY ,
  exam_date date DEFAULT NULL,
  start_time time DEFAULT NULL,
  end_time time DEFAULT NULL,
  duration time DEFAULT NULL
);

DROP TABLE IF EXISTS qustion_paper;
CREATE TABLE qustion_paper (
  exam_id int DEFAULT NULL,
  q_paper_id int NOT NULL PRIMARY KEY ,
  q_paper_course char(20) DEFAULT NULL,
  qustion_paper longblob,
  CONSTRAINT qustion_paper_fk_ FOREIGN KEY (exam_id) REFERENCES exam_schedule (exam_id) ON UPDATE CASCADE
);

DROP TABLE IF EXISTS answer_collected;
CREATE TABLE answer_collected (
  exam_id int DEFAULT NULL,
  q_paper_id int DEFAULT NULL,
  student_id int DEFAULT NULL,
  registration_no char(50) DEFAULT NULL,
  answer_produced longblob,
  CONSTRAINT answer_collected_fk FOREIGN KEY (q_paper_id) REFERENCES qustion_paper (q_paper_id) ON UPDATE CASCADE,
  CONSTRAINT answer_collected_fk FOREIGN KEY (student_id) REFERENCES personal (student_id) ON UPDATE CASCADE,
  CONSTRAINT answer_collected_fk FOREIGN KEY (registration_no) REFERENCES personal (registration_no) ON UPDATE CASCADE,
  CONSTRAINT answer_collected_fk FOREIGN KEY (exam_id) REFERENCES exam_schedule (exam_id) ON UPDATE CASCADE
);

DROP TABLE IF EXISTS answer_key;
CREATE TABLE answer_key (
  exam_id int DEFAULT NULL,
  q_paper_id int DEFAULT NULL,
  answer longblob,
  CONSTRAINT answer_key_fk FOREIGN KEY (exam_id) REFERENCES exam_schedule (exam_id) ON UPDATE CASCADE,
  CONSTRAINT answer_key_fk FOREIGN KEY (q_paper_id) REFERENCES qustion_paper (q_paper_id) ON UPDATE CASCADE
);

DROP TABLE IF EXISTS results;

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