# Ветвление логики работы светофора:
def traffic_light(behavior, wait):
    if behavior == 'driver':
        return driver(wait)
    else:
        return pedestrian(wait)


# Автомобильный режим работы светофора:
def driver(wait):
    if wait > 1:
        print('You need to wait!')
        return 'red'
    elif wait == 1:
        print('Get ready!')
        return 'yellow'
    else:
        print('Now you can ride!')
        return 'green'


# Пешеходный режим работы светофора:
def pedestrian(wait):
    if wait:
        print('You need to wait!')
        return 'red'
    else:
        print('Now you can go!')
        return 'green'


# Функция проверки ввода таймера светофора
def input_time():
    user_time = int(input('From 3 to 7: '))
    while True:
        if 2 < user_time < 8:
            return user_time
        else:
            user_time = int(input('From 3 to 7: '))


# Функция проверки ввода режима светофора
def input_mode():
    user_mode = input('Enter the mode ("pedestrian" or "driver"): ')
    while True:
        if user_mode == 'driver' or user_mode == 'pedestrian':
            return user_mode
        else:
            user_mode = input('Enter the mode ("pedestrian" or "driver"): ')


# Главная функция, запускающая остальные по порядку:
def main():
    # Проверки ввода пользователя:
    time = input_time()
    mode = input_mode()

    # Запуск функций, содержащих логику работы светофора:
    light = 'red'
    while light == 'red' or light == 'yellow':
        time -= 1
        light = traffic_light(mode, time)


# Запуск программы, выполнение программного кода начинается здесь:
if __name__ == '__main__':
    main()
