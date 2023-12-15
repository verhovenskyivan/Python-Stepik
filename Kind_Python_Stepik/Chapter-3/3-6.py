a, b, c = map(int, input().split())
lst = [a, b , c]
print(lst)
#-----------------------------------
cities = input().split()
if "Москва" in cities:
    print("True")
else:
    print("False")
#-----------------------------------
cities = input().split()
print(cities[-1])
#-----------------------------------
marks = list(map(int, input().split()))
a = (round(sum(marks) / len(marks), 1))
print(a)
#-----------------------------------
book = [input(),input(),int(input()),float(input())]
book[1] = 'Пушкин'
del book[2]
book[2] = (book[2]*2)
print(book)
#-----------------------------------
a = list(map(int, input().split()))
print(max(a), min(a), sum(a))
#-----------------------------------
a = list(map(int, input().split()))
a_sort = sorted(a, reverse=True)
print(*a_sort)
#-----------------------------------
cities = ["Москва", "Тверь", "Вологда"]
lst1 = input().split() 
lst = cities + lst1 
print(*lst)
#-----------------------------------
cities = ["Москва", "Тверь", "Вологда"]
lst1 = input().split() 
lst = lst1  + cities
print(*lst)
