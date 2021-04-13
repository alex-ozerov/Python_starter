def action():
    if z == "+":
        print(addition(x, y))
    elif z == "-":
        print(subtraction(x, y))
    elif z == "*":
        print(multiplication(x, y))
    elif z == "/":
        print(division(x, y))
def addition(x, y):
    return x+y
def subtraction(x, y):
    return x-y
def multiplication(x, y):
    return x*y
def division(x, y):
        if y == 0:
            print("На наноль делить нельзя!")
        else:
            return x/y
while True:
    x = int(input("Введите первое число:\n"))
    y = int(input("Введите второе число:\n"))
    z = input("Введите действие(+, -, *, /, stop):")
    if z == "stop":
        break
    action()