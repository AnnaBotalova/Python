from pyDatalog import pyDatalog
import random2

y=0
c=0
for x in range(999999):
     y=y+x
     c=c+1

print(y)

y=y/c
print(y)
c=0

v=list(range(100000))
for x in range(1000):
	s=random2.randrange(100)
	c=c*s
	v[x]=s

print()

le = len(v)
if le:
    v.sort()
    if (le % 2):
        m = (le - 1)//2
        M = v[m]
    else:
        m = le//2
        M = (v[m-1] + v[m]) / 2

print('Mediana: ', M)
