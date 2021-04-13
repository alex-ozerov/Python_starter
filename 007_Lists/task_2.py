list = [1, 2]
n = int(input("Введите номер ступеньки:"))
for i in range(n - 2):
    list.append(list[i] + list[i+ 1])
print(list)