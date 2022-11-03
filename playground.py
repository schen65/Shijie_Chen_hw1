from array import array
from pickle import TRUE
from re import X


a = "words"
a[0]
a[1]
a[5]
a[-1]
a[len(a)-1]
a[ : ]
a[1:3]
a[1:]
a[:-1]
a[: 3]
a = 'verylongword'
a[::2]
a[3::-2]
a[::-3]
a[::-1]
a[::-2]
a[::-3]
a
a.pop(1)
a[::2]
a[::-2]
[a[x] for x in [0,4]]
[a[0], a[3]]
b = [1,2,3,4,5,6]
b[1:4]
b
b[-2:5]
b = [[1,2,3],
    [4,5,6],
    [7,3,9]]
b
b[0][0]
b[1] = 200
b[0:2]
b[0:2] = []
b
b[1:1] = [100, 200, 300]
b[:0] = [388]

b
b = [1,2,3,4,5,6]
b.append(5)
b.extend([4,5,6,6])
b. insert(1,20)
b
b.pop()
b.pop(-2)
b.remove(4)
del b[0:30]
c = (1,2,3,4,5,6,7)
type(c)
c[1:4]
d = {'name': 'CJ', 'age':21, 'info': 'richass'}
d['age']
d[21]
del d['age']
d['hobby'] = 'brew coffee'
d
d.values()
d.items()
d.get('hobby')
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(0,40).reshape(10,4),
                    columns=['A', 'B','C','D'])
df['A']
type(df[['A']])



import hello as hl
hl.world()
import os
os.getcwd()
import sys
sys.path.append('typeyourpath')
sys.path()
os.getcwd()
a = [1,2,3,4,5,None ,7]
[x is None for x in a]
import numpy as np
a = np.array([1,2,np.nan, 3])
sum(a)

np.isnan(a)
sum(np.isnan(a))

import numpy as np
import datetime
for dtype in ['object', 'float']:
    print('dtype', dtype)
    start = datetime.datetime.now()
    for i in range(10):
        a = np.arange(10000000, dtype=dtype).sum()
    print(datetime.datetime.now() - start)

a = np.array([1,2,np.nan, 3], dtype=np.int)
import pandas as pd
df = pd.DataFrame([[1, np.nan ,3 ], [4,5,6]])
df
np.isnan(df)
df.isna()
df.notna()
df.isnull()
df.fillna(df.mean())

df.dropna(how= 'all')
df.dropna(axis=1)
np.nan == np.nan
None == None
df[1] == np.nan
df[1].sum()

pd.DataFrame([np.nan]).sum()




X = 4
if(X <= 2):
    print("<=2")
elif(X==3):
    print("==3")
else:
    print("> 3")

import numpy as np
x = np.arange(10)
x

np.where(x == 3 , x , 1)



import datetime
import time

start = datetime.datetime.now()
time.sleep(3)
print(datetime.datetime.now() - start)

import timeit

timeit.timeit(stmt='time.sleep(3)',
            setup= 'import time' ,
            number = 4)


timeit.timeit(stmt='np.arange(1000000,dtype=float).sum()' ,
              setup= 'import numpy as np' , 
              number= 20)



for i in range(100):
    print(i)

i = 1
while i < 100 :
    i +=1
    print(i)

import numpy as np
i = 1
x = 1
for x in range(100):
    print(x)

x = 0
while x < 100:
    x += 1
    if x == 3: continue
    if x == 8: break
    print(x)


x = 0
while TRUE:
    x += 1
    print(x)
    if x == 100: break

for (a,b) in [(1,2),(3,4),(5,6)]:
    print(a,b)


s = 'hello'
s_iter = iter(s)
s_iter
next(s_iter)
list(range(10))


L = [1 , 2 , 3, 4]
for x in range(len(L)):
    L[x] += 20
print(L)

a = [1,2,3,4,5,6,7]
b = [8,9,0,1,2,3,4]
c = [5,6,7,8,9,0,1]
list(map(np.mean,zip(a,b,c)))


def foo(x):
    l = ['a','e','i','o','u']
    if (x in l):
        return True
    else:
        return False

list(filter(foo,['a','s','u','i']))
list(map(foo,['a','b','c','i']))




word = 'hello'
counter = 0
l = [None] * len(word)
for (counter, item) in enumerate(word):
    l[counter] = item
l



it = range(10)
list(it)
iter = iter(list(it))
next(iter)

l = [1,2,3]
l = [x +10 for x in l if x != 2]
l









def doo(a,b):
    def aar(a,b):
        return a*b
    y = aar(a,b) +b
    return y
x = doo(1,2)
x
