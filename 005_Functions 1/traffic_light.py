# На основе примера создайте алгоритм светофора с двумя режимами:
# Светофор для перешехода и светофор для водителя.
# Попросите пользователя ввести необходимый режим.
# Если ввод некорректен (не "pedestrian" или "driver"), то запросите ввод еще раз.
# Создайте функцию, которая на основании параметра "mode"
# реализовывает алгоритм светофора для пешехода или для водителя.
# В случае автомобильного светофора программа при желтом свете светофора должна
# выдать сообщение "Get ready!".
time = int(input('From 3 to 7: '))
while True:
    if 2 < time < 8:
        break
    else:
        time = int(input('From 3 to 7: '))


def traffic_light(wait):
    # Логически верным будет создать вложенное условие.
    # Либо создайте две вспомогательные функции: для водителя и для пешехода.
    if wait:
        print('You need to wait!')
        return 'red'
    else:
        print('Now you can go!')
        return 'green'


light = 'red'
while light == 'red' or light == 'yellow':
    time -= 1
    light = traffic_light(time)
