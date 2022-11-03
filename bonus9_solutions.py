#Aggregating
#Merging
#Dates

#############################################
# Question 1:
# Consider the following dataframe
import pandas as pd
df1 = pd.DataFrame({'ID': [1,1,2,2,3,3],
                  'A': [1,2,3,4,4,4],
                  'B': [1,2,3,4,4,4]})
df1
#Group df1 by ID, compute the sum by group, and rename the columns to A_sum, B_sum
# Answer:
df_agg = df1.groupby('ID',as_index=False).sum()
df_agg.rename(columns={'A':'A_sum','B':'B_sum'}, inplace=True)
df_agg

#############################################
#Question 2:
# Consider the following dataframe
import pandas as pd
df1 = pd.DataFrame({'ID': [1,1,2,2,3,3],
                  'A': [1,2,3,4,4,4],
                  'B': [1,2,3,4,4,4]})
df1
#Group df1 by ID, compute the min, mean and max by group, and make sure the columns are single level
#Answer:

df1_agg = df1.groupby('ID', as_index=False).agg(['min','mean','max'])
df1_agg
df1_agg.columns = ['_'.join(x) for x in df1_agg.columns.ravel()]
df1_agg['ID'] = df1_agg.index #if we want ID as a column
df1_agg


#############################################
#Question 3:
import pandas as pd
df1 = pd.DataFrame({'ID': [1,3],
                  'A': [1,2],
                  'B': [1,4]})
df2 = pd.DataFrame({'ID': [1,2,3],
                  'A': [1,2,3],
                  'B': [1,4,4]})
#do a full outer merge on ID
# Answer:

#full outer join
pd.merge(left=df1,
         right=df2,
         how='outer',
         on='ID')


#############################################
#Question 4:
import pandas as pd
df1 = pd.DataFrame({'ID': [1,3],
                  'A': [1,2],
                  'B': [1,4]})
df2 = pd.DataFrame({'ID': [1,2,3],
                  'A': [1,2,3],
                  'B': [1,4,4]})
#do a left outer merge on ID
# Answer:

#full outer join
pd.merge(left=df1,
         right=df2,
         how='left',
         on='ID')


#############################################
#Question 5:
#STEP 1: Take this dataset, and read it in using pandas
'http://ballings.co/hidden/aCRM/data/chapter2/subscriptions.txt'
#STEP 2: Then compute the time elapsed between a customer's
#minimum StartDate and maximum StartDate (not EndDate). 
#Call this variable the "LOR" (length of relationship). 
#Since we need one row per customerid, we need to aggregate.
#STEP 3: Finally use seaborn to display the linear relationship between LOR and the customer's sum of TotalPrice.
#Answer:

#STEP 1:
#read in data as date
subscriptions = pd.read_table('http://ballings.co/hidden/aCRM/data/chapter2/subscriptions.txt', parse_dates = ['StartDate'] , delimiter = ';')
subscriptions.info()

#STEP 2:

#subset to keep only useful variables (this step is not necessary)
subscriptions = subscriptions[['CustomerID','StartDate','TotalPrice']]
subscriptions.shape

#aggregate
subs_agg = subscriptions.groupby('CustomerID').agg(
    min_StartDate = ('StartDate', min), 
    max_StartDate = ('StartDate', max), 
    sum_TotaPrice = ('TotalPrice', sum))
 
subs_agg.shape

#compute LOR
subs_agg['LOR'] = (subs_agg.max_StartDate - subs_agg.min_StartDate).dt.days

subs_agg.columns

#STEP 3:

#distribution of LOR (not necessary)
subs_agg.LOR.value_counts()

#plot and lm
import seaborn as sns 
sns.lmplot(x='LOR',
           y='sum_TotaPrice',
           data=subs_agg, 
           fit_reg=True)
plt.show()


#Note: why do we not use the max enddate instead of max startdate 
# in LOR? In this particular dataset, subscriptions are only added 
# on the day they are starting and the end date is an estimation 
# (e.g, if there is a weather event so that the newspaper company 
# cannot deliver, the end date is shifted). This means 
# that -- at the time when we are computing LOR -- the end date 
# may be in the future, and it is therefore not logical to use 
# the end date when computing how long a relationship has lasted.