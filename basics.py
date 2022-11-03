from array import array
from tkinter.tix import Tree
from typing import type_check_only
import numpy as np
# boolean
a = True
type(a)
a = np.bool_(True)
type(a)
help(np)
a[0]

b = np.int8(1)
type(b)
b[0]

c= np.int16(1)
type(c)
c[0]

d = np.int32(1)
type(d)
d[0]

e = np.int64(1)
type(e)
e[0]

f = 1
type(f)
f[0]



g = np.uint8(1)
type(g)
g[0]

h = np.uint16(1)
type(h)
h[0]


k = np.float16(1.1)
type(k)
k[0]


p = 'word'
type(p)
p[0]



q = [1, 'word', 1.1 , np.array([[3,4],[4,5],[6,3]])]
type(q)
q[0]


q[0] = 99999999999
q
q2 = q
q = 'shit'
q2

x = tuple((1, 'word', 1.1 , np.array([[3,4],[4,5],[6,3]])))
type(x)
x[0]
(1,1)

x[0] =9999999



s = {'name': 'john', 'age': 25, 'info':np.array([[1,2],[4,5],[5,6]])}
type(s)
s = dict(s)
s[0]
s['name']


{'a':1, 'a':2, 'b':2}


s['name']  = 'dope'
s

s.pop('name')
s['lastname'] = 'dope'
s


s2 = s
s.pop('age')
s



s2



t = {'name', 'age', 'info', 1.2, 1}
type(t)

t['name']
t[0]


t.discard('name')
t.add('fisher')
t2 = t 
t.add('123')

t2

u= frozenset(t)

type(u)

u.discard('info')


v= np.array([[1,2],[1,2,3,4], {'a'}])
type(v)
v[0]

import pandas as pd
w = pd.DataFrame([[1,2,3], [4,5,6]])
w[0]

w.iloc 