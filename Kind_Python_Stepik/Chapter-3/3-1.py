a = str(input())
b = str(input())
print(f'{a} {b}')
#------------------
a, b = map(str, input().split())
print((a+' ')*2 + (b+' ')*3)
#------------------
a, b = map(int, input().split())
print(f'Переменная a = {a}, переменная b = {b}')
#-------------------
a = input()
print("Строка: " + a + ". "+"Длина: "+str(len(a)))
#-------------------
a,b = map(str, input().split()) 
c = (a in b)
d = (b == a) 
f = (a > b)
e = (a < b)
print(c, d, f, e)
#------------------
a, b = map(str, input().split())
print(f"Коды: {a} = {str(ord(a))}, {b} = {str(ord(b))}")
