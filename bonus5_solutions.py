#Bonus Assignment
#reading in data


######################################################################
######################################################################
#Important remark:

# A,B,C and D are column names. 

######################################################################

#DATA:
# http://ballings.co/data/data1.csv
# http://ballings.co/data/data2.csv
# http://ballings.co/data/data3.txt
# http://ballings.co/data/data4.data
# http://ballings.co/data/data5.datafile
# http://ballings.co/data/data6.dat
# http://ballings.co/data/data7.txt
# http://ballings.co/data/data8.txt
   
import pandas as pd    
?pd.read_table

######################################################################
#Exercise 1:
#Use pd.read_table() to read in data1.csv. 

pd.read_table("http://ballings.co/data/data1.csv", sep=",")

   
######################################################################
# Exercise 2:    
#Use pd.read_table() to read in data2.csv. Do not read in the comments, denoted by a *.

pd.read_table("http://ballings.co/data/data2.csv",delimiter=',',comment='*')

######################################################################
# Exercise 3:
# Use read_table() to read in data3.txt.
# Answer:
pd.read_table("http://ballings.co/data/data3.txt",delimiter=';',header=None)
#this works because the default quotechar is " and not '


######################################################################
# Exercise 4:
# Use read_table() to read in data4.data.
# Answer:

pd.read_table("http://ballings.co/data/data4.data", delimiter=';', header=None)


######################################################################

# Exercise 5:
# Use read_table to read in data5.datafile. 
# Answer:
pd.read_table("http://ballings.co/data/data5.datafile", delimiter=';', header=None)

######################################################################
# Exercise 6:
# Use read_table() to read in data6.dat. Only read in 
# row 3 to 5. Print the result to the screen.
# Answer:
#row 0 is the header, so we need:
# 3,a
# 4,e,b,c
# 5
pd.read_table("http://ballings.co/data/data6.dat", delimiter=',', nrows=3, skiprows = [1,2])

#Note: if you do not have these exact same row numbers that is still counted as correct.

######################################################################
# Exercise 7:
# Use read_table() to read in data7.txt. 
# Make sure you also read in the lines without data. 
# There should be 6 lines of data.
# Answer:

pd.read_table("http://ballings.co/data/data7.txt", delimiter=',',skip_blank_lines=False)

######################################################################
# Exercise 8:
# Use read_table() to read in data8.txt. Assign
# the following variable names: A,B,C,D 
# Answer:

pd.read_table("http://ballings.co/data/data8.txt",delimiter=",",names=['A','B','C','D'])
