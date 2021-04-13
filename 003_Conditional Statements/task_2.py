import math
x = float(input("Введите значение:"))
if -math.pi < x < math.pi:
    y = 3 * math.cos(3 * x)
elif x < -math.pi or x > math.pi:
    y = x
print(y)
