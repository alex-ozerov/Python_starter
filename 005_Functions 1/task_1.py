def hello(name="Alex"):
    username = str(input("What is your name?"))
    if username:
        print('Hello,', username, '!', sep=' ')
    else:
        print('Hello,', name, '!', sep=' ')
hello()
