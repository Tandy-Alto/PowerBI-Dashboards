CREATE DATABASE ba_april;
USE ba_april;
CREATE TABLE employee(emp_id INT,f_name TEXT,l_name TEXT,salary INT,location TEXT, manager_id INT);
SELECT * FROM employee;
INSERT INTO employee VALUES(1,'Raj','Kapoor',40000,'Delhi',11),(2,'Ram','Ahluwalia',45000,'Mirzapur',12),(3,'Yash','Johar',50000,'Lucknow',13);
INSERT INTO employee(f_name,l_name)VALUES('Rajesh','Khanna');
SELECT * FROM employee;
SELECT * FROM employee WHERE salary>35000;
SELECT * FROM employee WHERE f_name='Raj' AND location='Delhi';
INSERT INTO employee VALUES(5,'Taj','Suroor',45000,'Delhi',15);
SELECT * FROM employee WHERE f_name='Raj' OR location='Delhi';
SELECT * FROM employee WHERE f_name<>'Raj'; SELECT * FROM employee WHERE NOT f_name='Raj';
SELECT location FROM employee;
SELECT DISTINCT location FROM employee;
SELECT DISTINCT f_name,l_name FROM employee WHERE f_name='Raj';
SELECT * FROM employee where emp_id IS NOT NULL;
SELECT * FROM employee where emp_id IS NULL;
CREATE TABLE info (emp_id VARCHAR(20), department TEXT, domain TEXT);
INSERT INTO info VALUES('1','Media','Acting'),('2','Accounts','Finance'),('3','Sponsership', 'Customer Relationship Management(CRM)'),('','Advertisement','Dancing'),('5','Brand Awareness','Literature');
CREATE TABLE info_class (emp_id INT, department TEXT, domain TEXT);
* INSERT INTO info_class VALUES(1,'Media','Acting'),(2,'Accounts','Finance'),(3,'Sponsership', 'Customer Relationship Management(CRM)'),(NULL,'Advertisement','Dancing'),(5,'Brand Awareness','Literature');
SELECT a.f_name,a.l_name,a.salary,a.location,b.department,b.domain FROM employee a INNER JOIN info_class b ON a.emp_id=b.emp_id;
SELECT a.f_name,a.l_name,a.salary,a.location,b.department,b.domain FROM employee a LEFT JOIN info_class b ON a.emp_id=b.emp_id;
DELETE FROM info_class;
INSERT INTO info_class VALUES(1,'Media','Acting'),(2,'Accounts','Finance'),(3,'Sponsership', 'Customer Relationship Management(CRM)'),(4,'Media','Actress'),(NULL,'Advertisement','Dancing'),(5,'Brand Awareness','Literature');
SELECT a.f_name,a.l_name,a.salary,a.location,b.department,b.domain FROM employee a RIGHT JOIN info_class b ON a.emp_id=b.emp_id;
SELECT a.f_name,a.l_name,a.salary,a.location,b.department,b.domain FROM employee a CROSS JOIN info_class b ORDER BY f_name,department;

SELECT COUNT(*) FROM employee;
SELECT COUNT(salary) AS cnt FROM employee;

SELECT SUM(salary) FROM employee;    SELECT SUM(salary) AS sum FROM employee;
SELECT MAX(salary) AS max FROM employee;
SELECT MIN(salary) AS min FROM employee;
SELECT ROUND(AVG(salary)) AS avg FROM employee;  SELECT SUM(salary)/COUNT(salary) AS avg FROM employee;

?? SELECT location,AVG(salary) FROM employee WHERE location IS NOT NULL GROUP BY location;
SELECT location,AVG(salary) FROM employee WHERE location IS NOT NULL GROUP BY location HAVING AVG(salary)>=45000;

CREATE TABLE employee_1 AS SELECT*FROM employee WHERE emp_id IS NOT NULL;
SELECT * FROM employee_1;

CREATE TABLE employee_empty AS SELECT* FROM employee WHERE 1=2;		SELECT* FROM employee_empty;


UPDATE employee_1 SET manager_id=25 WHERE emp_id=5;
UPDATE employee_1 SET manager_id=20;

DELETE FROM employee_1 WHERE f_name='Raj';
DELETE FROM employee_1; SELECT*FROM employee_1;

DELIMITER $ 
CREATE PROCEDURE sample_proc()
BEGIN 
SELECT location,AVG(salary) 
FROM employee 
WHERE location IS NOT NULL 
GROUP BY location; 
END $ 
DELIMITER ;

CALL sample_proc();

DELIMITER $
CREATE PROCEDURE sample_proc_param(val TEXT)
BEGIN
SELECT location, AVG(salary)
FROM employee
WHERE location IS NOT NULL AND location=val
GROUP BY location;
END $
DELIMITER ;

CALL sample_proc_param('Delhi');

SELECT ROUND(AVG(salary)) FROM employee; SELECT* FROM employee WHERE salary>48000;   SELECT*FROM employee WHERE salary>(SELECT ROUND(AVG(salary)) FROM employee);   

CREATE DATABASE A; CREATE TABLE B(emp_id INT); DROP DATABASE A; USE A; DROP TABLE B; DROP PROCEDURE sample_proc;

ALTER TABLE employee MODIFY COLUMN emp_id TEXT;
ALTER TABLE employee ADD COLUMN domain TEXT;
ALTER TABLE employee RENAME COLUMN domain TO department;