time = int(input("from 3 to 7:"))
mode = input("from mode(driver, pedestrian):")
while True:
    if mode == "driver" or mode == "pedestrian":
        break
    else:
        mode = input("from mode(driver, pedestrian):")
while True:
    if 2 < time < 8:
        break
    else:
        time = int(input("from 3 to 7:"))
def traffic_light(wait):
    print(wait)
    if mode == "pedestrian":
        if wait:
            print("You need to wait!")
            return "red"
        else:
            print("Now you can go!")
            return "green"
    elif mode == "driver":
        if wait >= 2:
            print("You need to wait!")
            return "red"
        elif wait == 1:
            print("Get ready!")
            return "yelow"
        else:
            print("Now you can go!")
            return "green"

light = "red"
while light == "red" or light == "yelow":
    time -= 1
    light = traffic_light(time)