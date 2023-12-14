age = 22
name = "Иван"
msg = 'Меня зовут {0}, мне {1}'.format(name, age)
print(msg)
#------------------------------------------------
a = input()
b = input()
c = int(input())
msg = "Уважаемый {0} {1}! Поздравляем Вас с {2}-летием!".format(a,b,c)
print(msg)
#------------------------------------------------
a, b, c = map(int, input().split())
msg = "Габариты: {0} x {1} x {2}".format(a,b,c)
print(msg)
#------------------------------------------------
a, b, c = map(int, input().split())
print(f"Габариты: {a} x {b} x {c}")
#------------------------------------------------
a = input().split()
print(f"{min(a)} {max(a)}")
#------------------------------------------------
city = input()
street = input()
house = input()
home = input()
print(f"г. {city}, ул. {street}, д. {house}, кв. {home}")
#------------------------------------------------
a = float(input())
b = int(input())
c = int(b/a)
print(f"Вы можете получить {c}$ за {b} рублей по курсу {a}")
