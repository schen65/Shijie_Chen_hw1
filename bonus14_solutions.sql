--operators
--missing values

----------------------------------------------------
--Question 1
--Use the modulo operator to compute the remainder of 444 divided by 7
--Answer:

select 444 % 7;

----------------------------------------------------
--Question 2:
--Compute the absolute value of -9 using an operator
--Answer:

select @ -9;

----------------------------------------------------
--Question 3
--Consider the following data:
drop table if exists a;
create table a (cola int, colb int);
insert into a values (1,null),(2,3),(5,null);
select * from a;
--Return all the records that have a null in colb
--Answer:

select * from a where colb is null;
--or
select * from a where colb is not distinct from null;

--This is incorrect:
select * from a where colb = null;

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

select * 
from a 
where cola in (select distinct cola from b);


