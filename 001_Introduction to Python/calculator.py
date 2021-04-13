while True:
    x = float(input("Введите первое число:\n"))
    y = float(input("Введите второе число:\n"))
    action = input("Действие:")
    if action == "+":
        print(x+y)
    elif action == "-":
        print(x-y)
    elif action == "*":
        print(x*y)
    elif action == "/":
        if y == 0:
            print("На наноль делить нельзя!")
        else:
            print(x/y)
    elif action == "**":
        print(x**y)
    elif action == "%":
        print(x%y)
    else :
        print("Значение не верно!")
