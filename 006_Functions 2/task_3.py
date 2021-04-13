def step(n):
    if n == 1 or n == 0:
        return 1
    else:
        return step(n - 1) + step(n - 2)
n = int(input("Введите номер ступеньки:"))
print(step(n))