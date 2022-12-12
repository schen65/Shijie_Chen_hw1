--joining
--working with time

------------------------------------------------
--Question 1
--Write a query that substracts one year and three days 
--from today's date. The output columns should be called 'today' and 
--'one_year_and_three_days_ago'.
--Answer:

select current_date as today, 
       current_date - interval '1 year' - interval '3 days' as one_year_and_three_days_ago;



------------------------------------------------
--Question 2
--Consider the following three datasets:

drop table if exists a;
drop table if exists b;
drop table if exists c;
create table a (id int, col_a int);
create table b (id int, col_b int);
create table c (id int, col_c int);
insert into a values (1,100),(2,200),(3,300);
insert into b values (2,400),(3,500),(4,600);
insert into c values (1,700),(3,800),(4,900);

--In a single query:
--Inner join a and b and 
--then inner join the joined a_b table and c.
--The join key is id.
--Write two different queries that accomplish that task: one with a multi-join, and one with two single joins and a subquery.
--Answer:

select * 
from a
inner join b on a.id = b.id
inner join c on a.id = c.id;

select * 
from (select a.id, col_a, col_b 
      from a
      inner join b on a.id = b.id) as a_b
inner join c on a_b.id = c.id;     


------------------------------------------------
--Question 3
--Use two different ways to cast '20 Feb 2018' to a date.
-- Answer:

select '20 Feb 2018'::date;
select to_date('20 Feb 2018','DDMonYYYY');