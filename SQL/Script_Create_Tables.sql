------------------------------------------
--DDL statement for table 'HR' database--
--------------------------------------------

CREATE TABLE EMPLOYEES (
                            EMP_ID CHAR(9) NOT NULL, 
                            F_NAME VARCHAR(15) NOT NULL,
                            L_NAME VARCHAR(15) NOT NULL,
                            SSN CHAR(9),
                            B_DATE DATE,
                            SEX CHAR,
                            ADDRESS VARCHAR(30),
                            JOB_ID CHAR(9),
                            SALARY DECIMAL(10,2),
                            MANAGER_ID CHAR(9),
                            DEP_ID CHAR(9) NOT NULL,
                            PRIMARY KEY (EMP_ID));
                            
  CREATE TABLE JOB_HISTORY (
                            EMPL_ID CHAR(9) NOT NULL, 
                            START_DATE DATE,
                            JOBS_ID CHAR(9) NOT NULL,
                            DEPT_ID CHAR(9),
                            PRIMARY KEY (EMPL_ID,JOBS_ID));
 
 CREATE TABLE JOBS (
                            JOB_IDENT CHAR(9) NOT NULL, 
                            JOB_TITLE VARCHAR(30) ,
                            MIN_SALARY DECIMAL(10,2),
                            MAX_SALARY DECIMAL(10,2),
                            PRIMARY KEY (JOB_IDENT));

CREATE TABLE DEPARTMENTS (
                            DEPT_ID_DEP CHAR(9) NOT NULL, 
                            DEP_NAME VARCHAR(15) ,
                            MANAGER_ID CHAR(9),
                            LOC_ID CHAR(9),
                            PRIMARY KEY (DEPT_ID_DEP));

CREATE TABLE LOCATIONS (
                            LOCT_ID CHAR(9) NOT NULL,
                            DEP_ID_LOC CHAR(9) NOT NULL,
                            PRIMARY KEY (LOCT_ID,DEP_ID_LOC));
                            
ALTER SESSION SET NLS_DATE_FORMAT = 'MM/DD/YYYY';
INSERT INTO EMPLOYEES(EMP_ID,F_NAME,L_NAME,SSN,B_DATE,SEX,ADDRESS,JOB_ID,SALARY,MANAGER_ID,DEP_ID) VALUES ('E1001','John','Thomas',123456,'01/09/1976','M','5631 Rice, OakPark,IL',100,100000,30001,2);
INSERT INTO EMPLOYEES(EMP_ID,F_NAME,L_NAME,SSN,B_DATE,SEX,ADDRESS,JOB_ID,SALARY,MANAGER_ID,DEP_ID) VALUES ('E1002','Alice','James',123457,'07/31/1972','F','980 Berry ln, Elgin,IL',200,80000,30002,5);
INSERT INTO EMPLOYEES(EMP_ID,F_NAME,L_NAME,SSN,B_DATE,SEX,ADDRESS,JOB_ID,SALARY,MANAGER_ID,DEP_ID) VALUES ('E1003','Steve','Wells',123458,'08/10/1980','M','291 Springs, Gary,IL',300,50000,30002,5);
INSERT INTO EMPLOYEES(EMP_ID,F_NAME,L_NAME,SSN,B_DATE,SEX,ADDRESS,JOB_ID,SALARY,MANAGER_ID,DEP_ID) VALUES ('E1004','Santosh','Kumar',123459,'07/20/1985','M','511 Aurora Av, Aurora,IL',400,60000,30004,5);
INSERT INTO EMPLOYEES(EMP_ID,F_NAME,L_NAME,SSN,B_DATE,SEX,ADDRESS,JOB_ID,SALARY,MANAGER_ID,DEP_ID) VALUES ('E1005','Ahmed','Hussain',123410,'01/04/1981','M','216 Oak Tree, Geneva,IL',500,70000,30001,2);
INSERT INTO EMPLOYEES(EMP_ID,F_NAME,L_NAME,SSN,B_DATE,SEX,ADDRESS,JOB_ID,SALARY,MANAGER_ID,DEP_ID) VALUES ('E1006','Nancy','Allen',123411,'02/06/1978','F','111 Green Pl, Elgin,IL',600,90000,30001,2);
INSERT INTO EMPLOYEES(EMP_ID,F_NAME,L_NAME,SSN,B_DATE,SEX,ADDRESS,JOB_ID,SALARY,MANAGER_ID,DEP_ID) VALUES ('E1007','Mary','Thomas',123412,'05/05/1975','F','100 Rose Pl, Gary,IL',650,65000,30003,7);
INSERT INTO EMPLOYEES(EMP_ID,F_NAME,L_NAME,SSN,B_DATE,SEX,ADDRESS,JOB_ID,SALARY,MANAGER_ID,DEP_ID) VALUES ('E1008','Bharath','Gupta',123413,'05/06/1985','M','145 Berry Ln, Naperville,IL',660,65000,30003,7);
INSERT INTO EMPLOYEES(EMP_ID,F_NAME,L_NAME,SSN,B_DATE,SEX,ADDRESS,JOB_ID,SALARY,MANAGER_ID,DEP_ID) VALUES ('E1009','Andrea','Jones',123414,'07/09/1990','F','120 Fall Creek, Gary,IL',234,70000,30003,7);

INSERT INTO DEPARTMENTS(DEPT_ID_DEP,DEP_NAME,MANAGER_ID,LOC_ID) VALUES (2,'Architect Group',30001,'L0001');
INSERT INTO DEPARTMENTS(DEPT_ID_DEP,DEP_NAME,MANAGER_ID,LOC_ID) VALUES (5,'Software Group',30002,'L0002');
INSERT INTO DEPARTMENTS(DEPT_ID_DEP,DEP_NAME,MANAGER_ID,LOC_ID) VALUES (7,'Design Team',30003,'L0003');
INSERT INTO DEPARTMENTS(DEPT_ID_DEP,DEP_NAME,MANAGER_ID,LOC_ID) VALUES (5,'Software Group',30004,'L0004');


-- INSERT INTO DEPARTMENTS(DEPT_ID_DEP,DEP_NAME,MANAGER_ID,LOC_ID) VALUES (2,'Architect Group',30001,'L0001');
-- INSERT INTO DEPARTMENTS(DEPT_ID_DEP,DEP_NAME,MANAGER_ID,LOC_ID) VALUES (5,'Software Group',30002,'L0002');
-- INSERT INTO DEPARTMENTS(DEPT_ID_DEP,DEP_NAME,MANAGER_ID,LOC_ID) VALUES (7,'Design Team',30003,'L0003');
-- INSERT INTO DEPARTMENTS(DEPT_ID_DEP,DEP_NAME,MANAGER_ID,LOC_ID) VALUES (5,'Software Group',30004,'L0004');
