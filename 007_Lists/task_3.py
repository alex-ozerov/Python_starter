a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
list = []
k = 0
if a == 1:
    a1 = a + 1
else:
    a1 = a
for i in range(a1, b+1):
    for j in range(a1, i):
        if i % j == 0:
            k = k + 1
    if k == 0:
        list.append(i)
    else:
        k = 0
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