lst = list(map(int, input().split()))
if lst[0] != lst[-1]:
    lst.append(True)
    print(*lst)
else:
    lst.append(False)
    print(*lst)
#-----------------------------------
cities = ["Москва", "Казань", "Ярославль"]
cities.insert(1,"Ульяновск")
print(*cities)
#-----------------------------------
lst = list(input())
lst.remove("+")
lst.remove("7")
lst.insert(0,"8")
lst.remove("-")
lst.remove("-")
print("".join(lst))
#-----------------------------------
a, b, c = input().split()
print(c,a[0]+'.'+b[0]+'.')
#------------------------------------
a= list(map(int,input().split())) 
b = a.pop(a.index(min(a))) 
c = a.pop(a.index(min(a)))
d = a.pop(a.index(min(a)))
e = [b, c, d]
e. sort()
print(*e)
#------------------------------------
lst = list(map(int, input().split()))
del_lst_end = lst.pop()
a = (del_lst_end / 2) == 0
lst.append(a)
print(*lst)
#------------------------------------
a = input().split()
print(a.count('2'))
#------------------------------------
l= list(input().split())
l.sort()
l.pop(0)
print(*l)
