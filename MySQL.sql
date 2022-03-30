create database project_dbms;
use  project_dbms;
CREATE TABLE User_account(name VARCHAR(50), 
    account_number BIGINT PRIMARY KEY,
    gender VARCHAR(2),
    aadhar_id BIGINT,
    DOB DATE,
    address VARCHAR(20),
    account_type VARCHAR(10),
    contact BIGINT
  );

create table login(
u_name VARCHAR(50) NOT NULL,
password VARCHAR(50) NOT NULL,
PRIMARY KEY ( u_name )
);

INSERT INTO user_account VALUES('Vishal Singh' ,
       1002 ,
       'M' ,
       100200300,
       '2000-02-22',
       'Samba', 
       'savings',85858585);


show tables;

select * from user_account;

select * from login;