# Петя успевает по математике лучше всех в классе, поэтому учитель задал ему сложное домашнее задание, в котором нужно в заданном наборе целых чисел найти сумму всех положительных элементов,
# затем найти где в заданной последовательности находятся максимальный и минимальный элемент и вычислить произведение чисел, расположенных в этой последовательности между ними.
# Так же известно, что минимальный и максимальный элемент встречаются в заданном множестве чисел только один раз и не являются соседними.Поскольку задач такого рода учитель дал Пете около ста,
# то Петя как сильный программист смог написать программу, которая по заданному набору чисел самостоятельно находит решение.

# 1)	5
#     -7 5 -1 3 9	            17 -15
# 2)	8
#     3 14 -9 4 -5 1 -12 4	    26 180
# 3)	10
#     -5 1 2 3 4 5 6 7 8 -3	    36 5040

x = int(input("Введите размер списка: "))
list_1 = list()
for i in range(x):
    list_1.append(int(input(f"Введите {i+1}-й элемент списка: ")))
print(list_1)
sum = 0
mult = 1
max = list_1.index(max(list_1))
min = list_1.index(min(list_1))
for i in range(len(list_1)):
    if list_1[i] > 0:
        sum += list_1[i]
    if i > max and i < min:
        mult *= list_1[i]
    elif i < max and i > min:
        mult *= list_1[i]

print(sum, mult)