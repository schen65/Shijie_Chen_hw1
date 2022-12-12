--Memory monitoring and management
--Reading data
--Exploring data

----------------------------------------------------
--Question 1
--If we have a large a amount of data, why would we use PostgreSQL instead 
--of R or Python do process that data?
--Answer:

--R and Python load everything in memory. If the data is large we will get out-of-memory errors. 
--In Postgres we can limit RAM usage.


----------------------------------------------------
--Question 2
--What is dirty data in the context of Postgres memory management?
--Answer:

--It is data changed in memory that has not yet been written to a physical file


----------------------------------------------------
--Question 3
--Verify the setting of your work memory.
--Increase work memory by 2MB for the duration of this session
--Verify again
--Answer:

show work_mem;
set work_mem to '6MB';
show work_mem;




----------------------------------------------------------------------
--Question 4:
--Read in the purchases data set at
--http://ballings.co/hidden/aCRM/data/chapter3/purchases.csv
--(either download manually to disk and then read from disk,
--or download automatically with curl or wget).
--Store the data in a table called purchases.
--Verify whether the data was successfully stored by selecting from purchases by printing
--20 rows to the screen.
--Answer:

create table purchases (
    customerid int,
    purchasedate text,
    numberusers int,
    purchaseprice float
);

select * from purchases;

copy purchases 
from program 'curl "http://ballings.co/hidden/aCRM/data/chapter3/purchases.csv"'
with (header true, format csv, delimiter ',');

select * from purchases limit 20;


----------------------------------------------------------------------
--Question 5:
--Display the column names to the screen without records of data.
--Answer:

select column_name 
from information_schema.columns 
where table_name = 'purchases';

----------------------------------------------------------------------
--Question 6:
--Determine for each column the number of missing values
--Answer:

select count(*) - count(customerid) from purchases;
select count(*) - count(purchasedate) from purchases;
select count(*) - count(numberusers) from purchases;
select count(*) - count(purchaseprice) from purchases;

----------------------------------------------------------------------
--Question 7:
--Compute the proportion of times each unique value in the numberusers column occurs
--Hint 1: transform an integer value to a float value as follows: result::float
--Hint 2: you can use a select query in place of an attribute as long as 
--        the query produces a single data element
--Answer:

select numberusers, (count(*)::float / (select count(numberusers) from purchases))
from purchases 
group by numberusers;

----------------------------------------------------------------------
--Question 8:
--Verify with a regression that numberusers perfectly predicts purchaseprice
--Also show the intercept and slope
--Anwer:

select regr_intercept(purchaseprice,numberusers),
       regr_slope(purchaseprice,numberusers),
       regr_r2(purchaseprice,numberusers)
from purchases;


----------------------------------------------------------------------
--Question 9:
--Compute the minimum, first decile, median, nineth decile, and maximum of
--purchaseprice.
--Answer:

select 
min(purchaseprice),
percentile_cont(0.10) within group (order by purchaseprice) as decile_1,
percentile_cont(0.50) within group (order by purchaseprice) as median,
percentile_cont(0.90) within group (order by purchaseprice) as decile_9,
max(purchaseprice)
from purchases;

