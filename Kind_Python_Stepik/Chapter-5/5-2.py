p = 1
x = 1
while x != 0:
    x = int(input())
    if x > 0:
        p *= x
    else:
        continue
print(p)
#-------------------
lst = list(map(str, input().split()))
i = 0
ans = 'ДА'
while i < len(lst):
    if len(lst[i]) < 6:
        ans = 'HEТ'
        break
    else:
        i += 1
print(ans)
#-------------------
name = input().lower().split()
a = 0
while a < len(name):
    if name[a][0] == name[a][-1]:
        print("ДА")
        break
    a += 1
else:
    print("НЕТ")
#--------------------
n = int(input())
x = []
i = 1
while i <= n:
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        x.append(i)
    if n >= 100:
        print("слишком большое значение n")
        break
else:
    print(*x)
#-------------------
a = int(input())
b = 1
while b ** 2 <= a:
        b+=1
print(b)
#------------------
a = int(input())
i = 1
b = 10
while b < a:
    i += 1
    b += b / 100 * 10 
print(i)
#-----------------
