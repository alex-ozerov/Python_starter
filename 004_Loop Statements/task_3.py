y = int(input("Введите длину катита:"))
for i in range(1, y):
    print('*' * i)


y = int(input("Введите длину катита:"))
for i in range(1, y):
    print(' ' * i, '*' * (y - i))


y = int(input("Введите длину катита:"))
for i in range(1, y):
    print(' ' * (y - i), '*' * i)


y = int(input("Введите длину катита:"))
for i in range(1, y):
    print('*' * (y - i))


y = int(input("Введите длину гипотенузы:"))
for i in range(1, y):
    print(' ' * (y - i), '*' * i, '*' * i)

