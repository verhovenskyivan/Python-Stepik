a = float(input())
b = float(input())
d = max(a, b)
print(d)
#-----------------#
a = int(input())
msg = "кратно 3" if a % 3 == 0 else "не кратно 3"
print(msg)
#-----------------#
a = input().lower()
msg = "палиндром" if  a == a[::-1] else "не палиндром"
print(msg)
#-----------------#
a = int(input())
msg = "True" if a == 1 else "False"
print(msg)
#-----------------#
a = int(input())
print(0 if a == 59 else a+1)
#-----------------#
