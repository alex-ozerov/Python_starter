a = int(input("Введите 1 число:"))
b = int(input("Введите 2 число:"))
sum = 0
if a < b:
    for i in range(a, b + 1):
        sum += i
    print(sum)
else:
    print("Не корректный ввод!")