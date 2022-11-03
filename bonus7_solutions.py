# Missing values
# Operators

######################################################################
# Question 1:
import numpy as np

# Consider the following array. How many missings values does each 
# column have?
import numpy as np
a = np.array([[np.nan,2,4],[20,np.nan,5]])

# Answer:

#built-in function:
sum(np.isnan(a))

#or
#numpy version:
np.sum(np.isnan(a), axis = 0) #axis = 0 means sum up the rows

#or
for x in range(a.shape[1]):
    print(np.isnan(a)[:,x].sum())

#or
np.isnan(a)[:,0].sum()
np.isnan(a)[:,1].sum()
np.isnan(a)[:,2].sum()

######################################################################
# Exercise 2:
# Consider traindata and newdata:
import pandas as pd
train = pd.DataFrame([[np.nan,2,4],[20,np.nan,5],[40,np.nan,6]])
test = pd.DataFrame([[np.nan,2,4],[20,np.nan,np.nan]])

# Compute the column-wise mean on train and then impute test with those means. 
# Answer:


test.fillna(train.mean())


######################################################################
# Exercise 3:
# Consider traindata and newdata:
import pandas as pd
train = pd.DataFrame([[np.nan,2,4],[20,np.nan,5],[40,np.nan,6]])
test = pd.DataFrame([[np.nan,2,4],[20,np.nan,np.nan]])

# Compute the column-wise mean on train and then impute test 
# only for variable with index 1
# Answer:

test.fillna(train.mean().loc[[1]])



######################################################################
# Question 4:
# Consider the following array. Which values are not null
import numpy as np
import pandas as pd
a = pd.DataFrame([[np.nan,2,4],[20,np.nan,5],[40,np.nan,6]])

# Answer:

a.notnull()

######################################################################
# Exercise 5:
# Consider
a = 10
b = 3
# Compute the floor division, and modulus
# Answer:

a // b
a % b

######################################################################
# Exercise 6:
# Consider
a = 10
b = 3
# Multiply a with b and store in a. You cannot use a = a * b
#Answer:

a *= b
a

######################################################################
# Exercise 7:
# Consider
a = 1000
b = a

a == b
a is b


c = 1000
d = 1000
c is d

#Why does "c is d" return False, and "a is b" True?

#Answer:
#Because id of a and b is the same and the id of c and d is not.
#or
#Because c and d do not point to the same memory location.

id(a) == id(b)
id(c) == id(d)
