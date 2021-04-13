x = float(input("Введите число:"))
if -10 < x <10:
    y = x**2
elif x < -10:
    y = 2 * abs(x) - 1
elif x > 10:
    y = 2 * x
print(y)