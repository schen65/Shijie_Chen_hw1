--conditional processing
--creating dummy variables
--aggregating

--------------------------------------------------
--Question 1.
--Consider the following data
drop table if exists a;
create table a (col1 int);
insert into a values (null),(1),(5),(3),(null),(2);
select * from a;
--If col1 is null, return a 0, otherwise return the value in col1.
--Write this the shortest possible way.
--Answer:
SELECT COALESCE(col1,0) FROM a;


--------------------------------------------------
--Question 2.
--Consider the following data
drop table if exists a;
create table a (id int, x text);
insert into a values (0,'a'),(1,'b'),(2,'a'),(0,'b'),(1,'b'),(2,'a');
select * from a;
--Write a sql query that counts the number of 'b' per id.
--Do not use a where-clause
--Order the results by id.
--Answer:
SELECT id,
COUNT(CASE WHEN x ='b' THEN 1 ELSE NULL END) as counts
FROM a
GROUP BY id;



--------------------------------------------------
--Question 3.
--Consider the following data
drop table if exists a;
create table a (col int);
insert into a values (0),(1),(2),(0),(1),(2);
select * from a;
--Write a pl/pgSQL anonymous block that loops through 
--the values of col in a and prints to the screen:
--'0' when the col is 0
--'1' when the col is 1
--'>1' for all other values
--Answer:
DO$$
DECLARE

BEGIN
END$$;




--------------------------------------------------
--Question 4:
--Part 1:
--Consider table a below:

drop table if exists a;
create table a (
    cat_variable1 text,
    cat_variable2 text);
insert into a (cat_variable1,cat_variable2)
values ('ab cd e','e'),
       ('b','d'),
       ('ab cd e','e'),
       ('c','d');    
select * from a;


--Automatically (using an anonymous block) create dummies for cat_variable1, 
--making sure that spaces in the variable names
--are automatically replaced by underscores. Look up and use the replace function in postgres.
--Answer:



--Part 2:

--Expand you solution to part 1 to also make dummies automatically for cat_variable2
--Answer:








