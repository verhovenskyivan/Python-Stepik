a = input()
print((a[0])+(a[-1]))
#------------------------
a = input()
print(a[0:4])
#------------------------
a = input()
print(a[-3]+a[-2]+a[-1])
#------------------------
a = input()
print(a[1::2])
#------------------------
a = input()
b = input()
print((a[0::2])+ " " + (b[1::2]))
#------------------------
a = input()
print(a[4::-1])
#------------------------
a, b = input().split()
a2 = len(a)
print(b[0:a2])
#------------------------
a, b = input().split()
b1 = len(b)
a1= a[0:b1]
a2= a1[1::2]
b2=b[1::2]
print(a2==b2)
