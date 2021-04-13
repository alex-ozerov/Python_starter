while True:
    input_data = input("Введите число: ")
    if input_data.isdigit() and int(input_data) >= 10 and int(input_data) <= 50:
        break
    else:
        print("Попробуйте еще")