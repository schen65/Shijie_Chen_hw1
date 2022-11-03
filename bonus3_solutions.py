# Bonus Assignment 3:

# Data Objects 

# Question 1. Explain (not code) why mutability is good.
# Answer:

# Without mutability one has to destroy the object and recreate it.
# This can be slow.

# Question 2. Explain (not code) why mutability is bad.
# Answer:

# If the object is immutable, integrity is guaranteed. There
# is no way the object can be changed, say, several thousand
# lines later.

# Question 3. Consider a and b. Run the following lines:
a = [1,2,3]
b = a
#Next, change a to [100,2,3] by recreating a, and then inspect the value of 
# a and b. Did b change to [100, 2, 3]?
# Answer:

a = [100, 2, 3]
a
b
# No. This is because upon recreating a, the memory location for a 
# changes, and it is not the same memory location to which b is pointing.


# Question 4. Consider a and b. Run the following lines:
a = [1,2,3]
b = a
# Next change a to [100, 2, 3] by subsetting a and assigning 100 to the subset. Then inspect a and b. Did b change to [100, 2, 3]?
# Answer:

a[0] = 100
a
b
#Yes. Object sharing only works for mutations.

# Question 5: Test a tuple for object sharing:
a = (1,2,3)
# Answer:
b = a
a[0] = 100
# Tuples do not support item assignment (which uses subsetting),
# and thus we cannot mutate the object. Therefore it cannot support
# object sharing.

