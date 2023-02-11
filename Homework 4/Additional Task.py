x = [5, 1, 1, 1, 2, 3, 3, 6, 3, 3, 2, 2, 1, 6]
count = 1
total = 0
for i in range(len(x) - 1):
    if x.count(i) > 2:
        total += x.count(i)
        count = i
        for i in range(len(x) - 1):
            while x.count(count) > 0:
                x.remove(count)
print(x)
print(total)     