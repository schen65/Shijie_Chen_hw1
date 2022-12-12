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

select coalesce(col1,0) from a;

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

select id, 
       sum(
           case when x = 'a' then 0
                when x = 'b' then 1
           end
          ) as nbr_b
from a
group by id
order by id;


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

do $$
declare
    v int;
begin
    for v in (select col from a order by col) loop
        if v = 0 then raise notice '0';
        elsif v = 1 then raise notice '1';
        else raise notice '>1';
        end if;
    end loop;    
end $$



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


DO $$
DECLARE 
    category text;
    category_sanitized text;
    query1 text;
    query2 text;    
    query3 text;        
BEGIN
    
    --make a copy of a, for two reasons:
        --have a backup in case something goes wrong
        --it is used in the for-clause and therefore in an active query when we alter it inside the for-loop
    drop table if exists dummies;
    create table dummies as select cat_variable1 from a;
    
    FOR category IN (select distinct cat_variable1 from a) LOOP
        
        category_sanitized = replace(category, ' ','_');
        
        query1 = 'alter table dummies add column cat_variable1_' || category_sanitized || ' int';
        execute query1;

        query2 = 'update dummies set cat_variable1_' || category_sanitized || ' = 0';
        execute query2;
        
        query3 = 'update dummies set cat_variable1_' || category_sanitized || ' = 1 
                  where replace(cat_variable1, '' '',''_'') = ''' || category_sanitized || '''';
        --the four quotes at the end of query 3:
            --first quote starts the string
             --second quote escapes the next one
             --third quote is the quote that gets added as follows: category'
            --fourth quote ends the string
        execute query3;
        
    END LOOP;
    
END $$;

select * from dummies;

--Part 2:

--Expand you solution to part 1 to also make dummies automatically for cat_variable2
--Answer:


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


DO $$
DECLARE 
    category record;
    category_sanitized text;
    query1 text;
    query2 text;    
    query3 text;        
BEGIN
    
    drop table if exists dummies;
    create table dummies as select * from a;
    
    
    FOR category IN (select distinct cat_variable1 as value, 'cat_variable1' as variable from a
                     union
                     select distinct cat_variable2, 'cat_variable2' from a) LOOP
    
    --RAISE NOTICE '% %', category.value, category.variable;
    
        category_sanitized = replace(category.value, ' ','_');

        query1 = 'alter table dummies add column ' || category.variable || '_' || category_sanitized || ' int';
        execute query1;

        query2 = 'update dummies set ' || category.variable || '_' || category_sanitized || ' = 0';
        execute query2;
        
        query3 = 'update dummies set ' || category.variable || '_'  || category_sanitized || ' = 1 
                  where replace(' || category.variable || ', '' '',''_'') = ''' || category_sanitized || '''';
        execute query3;

     
    END LOOP;
    
END $$;

select * from dummies;







