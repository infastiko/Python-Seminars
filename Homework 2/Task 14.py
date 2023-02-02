#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#10 -> 1 2 4 8

x = int(input("Введите число: "))
count = 2
step = 0
y = 0
while y <= x:
    y = count ** step
    step += 1
    if y <= x:
        print(y, end=" ")
    else:
        break