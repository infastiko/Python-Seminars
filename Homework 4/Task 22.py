# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random

x = int(input("Введите количество элементов 1-го списка: "))
y = int(input("Введите количество элементов 2-го списка: "))
list_1 = list()
list_2 = list()

for i in range(x):
    list_1.append(random.randrange(1, 20))
for i in range(y):
    list_2.append(random.randrange(1, 20))
    print(list_1, list_2)
    
print(sorted(set(list_1) & set(list_2)))