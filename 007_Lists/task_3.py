a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
list = []
for i in range(a, b+1):
    k = 0
    for j in range(1, i):
        if i % j == 0:
            k = k + 1
    if k == 1:
        list.append(i)
print(list)


def multiplylist(list):
    multiply = 1
    for x in list:
        multiply = multiply * x
    return multiply


action = input("Введите действие(*,+):")
if action == "+":
    print(sum(list))
elif action == "*":
    print(multiplylist(list))