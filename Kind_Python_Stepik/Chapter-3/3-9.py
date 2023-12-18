lst = [5.4, 6.7, 10.4]
b = list(map(int, input().split()))
lst.append(b)
print(lst)
#-----------------------------------
a = list(input().split())
b = list(input().split())
c = list(input().split())
print([a, b, c])
#-----------------------------------
a = list(input().split())
b = list(input().split())
c = list(input().split())
print(a[-1], b[-1], c[-1])
#-----------------------------------
t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
     ["Я", "Python", "выучил", "с", "каналом"],
     ["Балакирев", "что", "раздавал?"]]
a = t[0:]
p=input()
print(p in t[0]+t[1]+t[2])
