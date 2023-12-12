a = input()
b = a[0]
c = a[1::]
a_upper = b.upper()
a_lower = c.lower()
print(a_upper+a_lower)
#--------------------
a = input()
b = a.count("-",0)
print(b)
#--------------------
a = input()
b = a.find("ra",0)
print(b)
#--------------------
s = input ()
s2= s.replace ("--", '-')
s3 = s2.replace ("--", '-')
print (s3)
#--------------------
a, b, c = input().split()
a1 = a.rjust(3, "0")
b1 = b.rjust(3, "0")
c1 = c.rjust(3, "0")
print(a1)
print(b1)
print(c1)
#--------------------
a = input().split()
print(len(a))
#--------------------
a = input()
b = a.replace(" ",";")
print(b)
#--------------------
