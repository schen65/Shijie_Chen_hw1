#Data exploration

import pandas as pd
import numpy as np

######################################################################
# Exercise 1:
# Confirm that a has 1000 values
a = np.arange(0,1000)
# Answer:
len(a)

######################################################################
# Before you start to work on subsequent questions:
# You will need this dataset for the exercises:

subs = pd.read_table('http://ballings.co/hidden/aCRM/data/chapter2/subscriptions.txt', delimiter=';')


######################################################################
# Exercise 2:
# Compute the minimum, maximum, quartiles, and mean of the TotalCredit
# variable.
# Answer:

subs['TotalCredit'].describe()


######################################################################
# Exercise 3:
# What is the mean of FormulaDiscount?
# Answer:

subs.FormulaDiscount.mean()


######################################################################
# Exercise 4:
# What is the variance of TotalPrice?
# Answer:

subs.FormulaDiscount.var()


######################################################################
# Exercise 5:
# What is the standard deviation of TotalPrice?
# Answer:

subs.TotalPrice.std()

######################################################################
# Exercise 6: 
# Make a scatter plot of TotalDiscount (x-axis) and NetNewspaperPrice 
# (y-axis). Add a regression line to the plot.
# Answer:

import matplotlib.pyplot as plt
import seaborn as sns
sns.lmplot('TotalDiscount','NetNewspaperPrice',subs)
plt.show()

######################################################################
# Exercise 7: 
# How many missing values are there in each of the columns in the subs data frame?
# Answer:

subs.isna().sum()


######################################################################
# Exercise 8: 
# What is the correlation between NbrStart and FormulaDiscount?
# Answer:

np.corrcoef(subs.NbrStart[~np.isnan(subs.FormulaDiscount)],
            subs.FormulaDiscount[~np.isnan(subs.FormulaDiscount)])
#or
subs.NbrStart.corr(subs.FormulaDiscount)