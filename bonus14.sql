--operators
--missing values

----------------------------------------------------
--Question 1
--Use the modulo operator to compute the remainder of 444 divided by 7
--Answer:



----------------------------------------------------
--Question 2:
--Compute the absolute value of -9 using an operator
--Answer:



----------------------------------------------------
--Question 3
--Consider the following data:
drop table if exists a;
create table a (cola int, colb int);
insert into a values (1,null),(2,3),(5,null);
select * from a;
--Return all the records that have a null in colb
--Answer:



----------------------------------------------------
--Question 4
--Consider the following tables:
drop table if exists a;
create table a (cola int, colb int);
insert into a values (1,null),(2,3),(5,null);
select * from a;

drop table if exists b;
create table b (cola int, colb int);
insert into b values (1,null),(1,1),(5,null);
select * from b;

--Select all the records where the values of cola in a are present in 
--the values of cola in b.
--Answer:




