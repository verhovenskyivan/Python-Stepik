for x in range(0, 11):
    print(x, end = ' ')
#-----------------------
i = 10
for i in range(10, -1, -1):
    print(i, end =' ')
#-----------------------
i = -10
for i in range(-10, -1, 2):
    print(i, end =' ')
#-----------------------
i = 1
for i in range(1, 20, 3):
    print(i, end = " ")
#-----------------------
lst = list(map(int, input().split()))
sum = 0
for i in  lst:
    if i % 2 != 0:
        sum += i
print(sum)
#-----------------------
lst = input().split()
for i in lst:
    print(len(i), end = ' ')
#-----------------------
a = int(input())
for i in range(1,(1+a),1):
    if a % int(i) == 0:
        print(i)
#-----------------------
a = int(input())
for i in range(2, m):
    if a % i == 0:
        print('НЕТ')
        break
else:
        print('ДА')
