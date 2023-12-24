n, m = map(int, input().split())
while n <= m:
    s = n**2
    print(s, end=' ')
    n += 1
#-------------------------------
x = float(input())
count = 2
while count <= 10:
    res = x * count
    count += 1
    print(round(res, 2), end=' ')
#------------------------------
n = int(input())
i = 1
sum = 0
while i <= n:
    sum += 1/i
    i += 1
print(round(sum, 3))
#------------------------------
a = int(input())
sum = a
while a !=0:
    a = int(input())
    sum += a
print(sum)
#------------------------------
n = input()
while "--" in n:
    n = n.replace("--", "-")
print(n)
#------------------------------
n = int(input())
s = 1
if n > 99:
    while n != 0:
        d = n % 10
        s *= d
        n = n // 10
    print(s)
#-----------------------------
n = int(input())
count = 1
a, b = 1, 1
while count <= n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
#------------------------------

n = int(input())
sum = 1000
y = 1
while y <= n:
    y+= 1
    sum += sum*0.05
print(round(sum, 2))
#------------------------------
n, m = map(int,input().split())
while n < m and n % 2 == 0:
    print(n+1, end=' ')
    n+=2
#------------------------------
