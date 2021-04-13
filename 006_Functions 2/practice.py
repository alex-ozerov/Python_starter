def number(c):
    global a
    if c == a:
        return a
    else:
        return c + number(c - 1)

a = int(input("Введите 1 число:"))
b = int(input("Введите 2 число:"))
print(number(b))
