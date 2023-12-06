# return positive number 
d = int(input())
print(abs(d))
#------------------------------------Minimun
d1, d2, d3, d4, d5 = map(int, input().split())
print(min(d1,d2,d3,d4,d5))
#-------------------------------------- Maximun
d1, d2, d3, d4, d5 = map(int, input().split())
print(max(d1,d2,d3,d4,d5))
#-------------------------------------- Гипотенуза
import math
a, b = map(int, input().split())
c = round(math.hypot(a,b),2)
print(c)
#-------------------------------------- Факториал
import math
n, k = map(int, input().split())
print(int(math.factorial(n) / (math.factorial(k) * (math.factorial(n-k)))))
#---------------------------------------------- Округление до ближайшего целого
from math import ceil as ce
n, m = map(int, input().split())

bus = 20
c = int(m+n)
print(ce(c/bus))
#-------------------------------------------- Округление
x = int(input())
y = x * 0.9
print(int(500/y))
