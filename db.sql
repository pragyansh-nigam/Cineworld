create database webpro;

create table webpro.signup(
		uid int AUTO_INCREMENT,
		name varchar(100) NOT NULL,
		mail varchar(100) NOT NULL,
		password varchar(20) NOT NULL,
		PRIMARY KEY (uid)
);