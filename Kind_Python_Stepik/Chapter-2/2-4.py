a = 7
b = -4
c = 3
print(a, b, c)
#----------
a = 7
b = -4
c = 3
print(a, b, c, sep='\n')
#---------------
s1 = "Hello"
s2 = "Balakirev"
print(s1, s2)
#---------------
s1, s2 = map(str.strip, input().split())
print("Word 1: " + s1, "| Word 2: " +s2)
#---------------
s1, s2 = map(int, input().split())
print(s1**s2)
#-------------
s1, s2 = map(float, input().split())
c = round(s1+s2, 2)
print(c)
#---------------
x, y = map(int, input().split())
print(x+y+x*2+y*4)
#---------------
x = float(input())
y = float(input())
print(2 *(x +y))
#----------
import math
print(round(math.pi,3))
#---------------------
a = float(input())
print(f"Вы ввели число {a}")
