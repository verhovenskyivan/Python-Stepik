print("Тема занятия \"спецсимволы\"")
#--------------------------------------
a1 = input().replace(" ", "\\")
print(a1)
#--------------------------------------
a=input()
a=a.replace(' ','\'',1)
print(a.replace(' ','\"'))
#--------------------------------------
path = r"C:\WINDOWS\System32\drivers\etc\hosts"
print(path)
#--------------------------------------
a = input()
b = f"\"{a}\""
print(b)
