--Postgres: basics

---------------------------------
--Exercise 1:
--Create an empty table called mytable, with 2 columns,
--called var1 and var2. Both are integers.
--Answer:

create table mytable (
    var1 integer,
    var2 integer);

---------------------------------
--Exercise 2:
--Insert three records:
--record 1: 11,24
--record 2: 5,88
--record 3: 3,2
--Answer:

  
INSERT INTO mytable (var1, var2)
VALUES 
    (11,24),
    (5,88),
    (3,2);
    
---------------------------------
--Exercise 3:
--Display the contents of mytable
--Answer:
select * from mytable;


---------------------------------
--Exercise 4:
--Remove all records from mytable:
--Answer:
truncate mytable;
-- or
delete from mytable;


---------------------------------
--Exercise 5:
--Remove mytable and verify if it still exists.
--Answer:
drop table mytable;
select * from mytable;














