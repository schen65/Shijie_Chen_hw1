--Memory monitoring and management
--Reading data
--Exploring data

----------------------------------------------------
--Question 1
--If we have a large a amount of data, why would we use PostgreSQL instead 
--of R or Python to process that data?
--Answer:




----------------------------------------------------
--Question 2
--What is dirty data in the context of Postgres memory management?
--Answer:




----------------------------------------------------
--Question 3
--Verify the setting of your work memory.
--Increase work memory by 2MB for the duration of this session
--Verify again
--Answer:






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




----------------------------------------------------------------------
--Question 5:
--Display the column names to the screen without records of data.
--Answer:



----------------------------------------------------------------------
--Question 6:
--Determine for each column the number of missing values
--Answer:



----------------------------------------------------------------------
--Question 7:
--Compute the proportion of times each unique value in the numberusers column occurs
--Hint 1: transform an integer value to a float value as follows: result::float
--Hint 2: you can use a select query in place of an attribute as long as 
--        the query produces a single data element
--Answer:



----------------------------------------------------------------------
--Question 8:
--Verify with a regression that numberusers perfectly predicts purchaseprice
--Also show the intercept and slope
--Anwer:



----------------------------------------------------------------------
--Question 9:
--Compute the minimum, first decile, median, nineth decile, and maximum of
--purchaseprice.
--Answer:



