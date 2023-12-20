a, b, c = map(int, input().split())
if b >= a and a<=c:
    print(a)
elif a >= b and b <=c:
    print(b)
else:
    print(c)
#-------------------------------------
a = float(input())
if a <= 60:
    a = 1
elif 64 >= a > 60:
    a = 2
elif 64 < a <= 69:
    a = 3
else:
    a = 4
print(a)
#-------------------------------------
a = int(input())
if a == 1:
    print("понедельник")
elif a == 2:
    print("вторник")
elif a == 3:
    print("среда")
elif a == 4:
    print("четверг")
elif a == 5:
    print("пятница")
elif a == 6:
    print("суббота")
else:
    print("воскресенье")
#---------------------------------------
a = int(input())
if a == 1:
    print(31)
elif a == 2:
    print(28)
elif a == 3:
    print(31)
elif a == 4:
    print(30)
elif a == 5:
    print(31)
elif a == 6:
    print(30)
elif a == 7:
    print(31)
elif a == 8:
    print(31)
elif a == 9:
    print(30)
elif a == 10:
    print(31)
elif a == 11:
    print(30)
else:
    print(31)
#---------------------------------------
k = int(input())
a = k % 7
if a == 1:
    print("понедельник")
if a == 2:
    print("вторник")
if a == 3:
    print("среда")
if a == 4:
    print("четверг")
if a == 5:
    print("пятница")
if a == 6:
    print("суббота")
if a == 7:
    print("воскресение")
#-------------------------------------------
a = int(input())
m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''
b = m.split('\n')
if a:
    print(b[a-1])
