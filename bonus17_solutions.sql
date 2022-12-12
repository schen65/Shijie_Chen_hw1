--Some questions in this bonus assignment use the subscriptions table. If you do not have it anymore, please use the code in the section on reading in data to get it.

------------------------------------------------
--Question 1
--Create a function called c that returns the following information from the 
--information_schema.columns table: ordinal_position, column_name, data_type.
--The input argument is a table name.
--Test your function on the subscriptions table.
--Answer:

--We first need to verify the column types
SELECT
 column_name, data_type
FROM
 information_schema.columns
WHERE
 table_name = 'columns'
AND 
 column_name in ('ordinal_position', 'column_name', 'data_type');
 
--Next we can use these types in our create type statement:

drop type coltype cascade;

create type coltype as (ordinal_position integer, column_name name, data_type varchar);

drop function c;

create or replace function c (tab_name text) returns setof coltype as 
$$
SELECT
 ordinal_position, column_name, data_type 
FROM
 information_schema.columns
WHERE
 table_name = tab_name ;
$$
 language 'sql';

--Test function:

select * from c('subscriptions');



---------------------------------------------
--Question 2

--How long does it take to load the first row of the subscriptions table? 
--Write the query to obtain that information.
--Anwer:

explain analyze select * from subscriptions;

--the answer is the first number after 'actual time='



---------------------------------------------
--Question 3
--
--Step 1: Verify if table a is unlogged.
--Step 2: Make table a unlogged by altering it: https://www.postgresql.org/docs/current/sql-altertable.html
--Step 3: Verify if table a is now unlogged. 
--Step 4: Make table a logged
--Step 5: Verify is table a is now logged.
--Answer:

select relname from pg_class where relpersistence  = 'u';

alter table a set unlogged;

select relname from pg_class where relpersistence  = 'u';

alter table a set logged;

select relname from pg_class where relpersistence  = 'u';

---------------------------------------------
--CANCELED QUESTION
--Question 4 
--Step 1: Explain analyze the following query:

select subscriptionid from subscriptions where subscriptionid = '1013257';

--Step 2: What are the first two words of the query plan, and what is the execution time?
--Step 3: Create an index called subscriptions_subscriptionid on table subscriptions and column subscriptionid
--Step 4: Explain analyze the query again (no need to copy and paste the statement from step 1) and write down the first three words of the query plan and what the execution time is.
--Answer:



--Step 1:
explain analyze select subscriptionid from subscriptions where subscriptionid = '1013257';

--Step 2:
--Seq Scan (i.e., is scans all the instances)
--Execution time can be found on the last line of the query plan.
--Execution Time: 0.078 ms

--Step 3:
drop index if exists subscriptions_subscriptionid;
create index subscriptions_subscriptionid on subscriptions (subscriptionid);

--Step 4:
--Index Only Scan
--Execution Time: 0.054 ms

 