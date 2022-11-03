#Bonus assignment, functions and methods

############1:
# 1. Create a function called foo with two parameters: a and b. 
# Function foo should define another 
# function called bar with the same parameters. 
# Function bar returns the result of multiplying a and b 
# and function foo adds the result of function bar to a.
# Have foo return a list containing the result of that addition as
# its first element and function bar as its second element.
# 2. Call foo with a=1 and b=2 and store it in an object called d.
# 3. Then use d to call function bar with a=1 and b=2.
# Answer:

#1. Create function:
def foo(a,b):
    def bar(a,b):
        return a*b
    return [a + bar(a,b),bar]


# 2. Call 'foo' with a=1 and b=2 and store it in an object called 'd'
d = foo(a=1,b=2)

# 3. Then use 'd' to call function 'bar' with a=1 and b=2.
d[1](1,2)


######################################################################
# Exercise 2:
# Create a function called foo with one parameter: x.
# foo should return 'hello' when x=1, 'world' when x=2, and '!' when x=3.
# foo should not print anything to the screen when we store the result
# of foo into an object like a = foo(3).

# Answer
def foo(x):
    if (x==1):
        return("hello")
    elif (x==2):
        return("world")
    elif (x==3):
        return("!")
 
a = foo(3)
a



######################################################################
# Exercise 3:
#Create a class called foo.
#Its arguments at initialization are a and b
#It should make available three attributes, a, b, MySum (the latter being a + b).
#It shoud also define a method, called mul, which 
# multiplies MySum by a number c, passed in to that method 
#when you call it.
# Answer:

class foo:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.MySum = a + b
    def mul(self,c):
        return self.MySum * c

res = foo(1,2)
res.a
res.b
res.MySum
res.mul(2)
