# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

x = int(input("Введите начальное число прогрессии: "))
y = int(input("Введите шаг: "))
z = int(input("Введите количество элементов прогрессии: "))
list1 = list()

for i in range(z):
    list1.append(x)
    x += y

print(list1)