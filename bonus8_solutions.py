# Topic:
# Dummy variables
# Conditional processing
# timing code


######################################################################
# Exercise 1:
# Automatically create dummy variables of all the variables in data. 
# Store the result in a data frame called df.
# Make sure to represent the data efficiently by dropping one category per variable. 
import pandas as pd
data = pd.DataFrame({'V1': ["yes","no","maybe","yes","no"],
                     'V2': ["now","today","today","tomorrow","tomorrow"]})
data
# Answer:

df = pd.get_dummies(data, drop_first=True)
df

######################################################################
# Exercise 2:
# Manually create dummy variables of V1 using np.where. 
# Store the result in a data frame called df. Name the columns V1_yes, V1_no, V1_maybe.
data = pd.DataFrame({'V1': ["yes","no","maybe","yes","no"]})
data

# Answer
import numpy as np
df = data
df['V1_yes'] = np.where(data.V1=="yes",1,0)
df['V1_no'] = np.where(data.V1=="no",1,0)
df['V1_maybe'] = np.where(data.V1=="maybe",1,0)
df

######################################################################
# Exercise 3:
# Figure out what is wrong here and correct the code.
x = 3

if (x==1):
  print("x is 1")
else if (x==2):
  print("x is 2")
else if (x==3):
  print("x is 3")



# Answer:
#else if is what is wrong. It should be elif

if (x==1):
  print("x is 1")
elif (x==2):
  print("x is 2")
elif (x==3):
  print("x is 3")

######################################################################
# Exercise 4:
# Figure out what is wrong here and correct the code.
x = np.arange(5)
x

if (x < 3): 
    x 
else:
    0

# Answer:
#Don't use if() for vectors. Use np.where() instead.
np.where(x < 3,x,0)


######################################################################
# Exercise 5:
# How many seconds does it take to execute the following line of code 100 million times
a += 1
# Answer:

timeit.timeit(stmt = 'a += 1', setup = 'a = 0', number = 100000000)
#note that the final result would be 1 (not 100 million), 
#because it reinitializes every time. The purpose of this exercise
#it to understand the setup parameter.


#############################
#Exercise 6:

# Consider this list: [1,2,3,4,5]
# Write a for loop to print all values to the 
# screen, one by one, except value 3.

# Answer:
for i in [1,2,3,4,5]:
    if i == 3: continue
    print(i)
    
#############################    
#Exercise 7:

# Consider this list: [1,2,3,4,5]
# Write a list comprehension to print all values to 
# the screen except value 3.
# Answer:

[i for i in [1,2,3,4,5] if i != 3]

#############################
#Exercise 8:

# Consider this iterable: [1,2,3,4,5]
# Make an iterator and use the next function 
# to produce the values one by one.
# Answer:

m = iter([1,2,3,4,5])
next(m)
next(m)
next(m)
next(m)
next(m)