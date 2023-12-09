10 > 5 # true
10 < 10 #false
10 <= 10 #true
#-------------------
a = float(input())
if int(a) % 3 == 0:
    print("True")
else:
    print("False")
#------------------
x = float(input())
print(round(x) > x)
#------------------
a, b = map(int, input().split())
if a % b == 0:
    print("True")
else:
    print("False")
#-----------------
a = float(input())
print((a >= 0 and a <= 2) or ( a >= 10 and a <= 20 ))
