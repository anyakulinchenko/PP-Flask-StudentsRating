use mydb;

CREATE TABLE students (
  sid int NOT NULL AUTO_INCREMENT,
  first_name varchar(30) DEFAULT NULL,
  last_name varchar(40) DEFAULT NULL,
  total_rating int DEFAULT NULL,
  PRIMARY KEY (sid)
);

CREATE TABLE teachers (
  tid int NOT NULL AUTO_INCREMENT,
  username varchar(40) NOT NULL,
  password varchar(40) NOT NULL,
  first_name varchar(30) DEFAULT NULL,
  last_name varchar(40) DEFAULT NULL,
  PRIMARY KEY (tid)
);

CREATE TABLE ratings (
  rid int NOT NULL AUTO_INCREMENT,
  subject varchar(30) DEFAULT NULL,
  svalue int DEFAULT NULL,
  sid int DEFAULT NULL,
  PRIMARY KEY (rid),
  KEY sid (sid),
  FOREIGN KEY (sid) REFERENCES students (sid)
);




insert students( first_name, last_name) values ('Anna', 'Kulinchenko');
insert teachers( username, password, first_name,last_name) values ('tusername', 'tpassword', 'Nadiia', 'Zykova');
insert ratings( subject, svalue, sid) values ('math', 4, 1);

