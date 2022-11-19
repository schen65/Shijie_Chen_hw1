--Postgres: object types, stacking, and iteration.

---------------------------------
--Exercise 1:
--Create an anonymous block with two variables
--called var1 and var2. Both are of type text.
--Set var1 to 'Hello' and var2 to 'world'.
--Print to the screen the sentence:
--'var1 var2 how are you doing' where var1 and var2 
--should be replaced by the values that you assigned to them.
--Answer:


---------------------------------
--Exercise 2:
--Create a table with one column, called a, of type numeric array.
--Insert a record with 5 values.
--Answer:


---------------------------------
--Exercise 3:
--Create a composite type with at least three different types.
--Use it to create a new table and insert a record.
--Answer:



---------------------------------
--Exercise 4:
--step 1: Create a materialized view of the table you created in exercise 3 that selects
--all records.
--Step 2: Add an additional record to the table created in exercise 3
--Step 3: select all records from that materialized view
--Step 4: refresh the materialized view
--Step 5: select all records from that materialized view

--Answer:


---------------------------------------------
--Exercise 5. 
--Consider the following three tables.

drop table if exists a;
drop table if exists b;
drop table if exists c;

create table a (
    x int,
    y int
);

create table b (
    x int,
    y int
);

create table c (
    x int,
    y int
);


insert into a values (1,1), (2,2);
insert into b values (2,2), (3,3);
insert into c values (3,3), (4,4);

-- Now consider the following three queries:

--query 1
select * from a;

--query 2
select * from b;

--query 3
select * from c;

--Append the result of query2 to query1 (do not remove duplicates) and then remove all records 
--that are in the combined result that are not in the result of query3 (do not remove duplicates).

--Answer:



---------------------------------------------
--Exercise 6. 
--Consider the following tables.

drop table if exists a;

create table a (
    a int array
);


insert into a values (array[1,2,3,4]),(array[5,6,7,8,9,10,11,12,13,14]);

select * from a;


--Using a nested looping construct, print to the screen, one by one, the values of the first record, and the second record.

--Answer:

