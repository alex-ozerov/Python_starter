def polindrome(abc):
    newabc = abc.replace(" ", "").replace(",", "")
    if str(newabc) == str(newabc)[::-1]:
        print(True)
    else:
        print(False)
abc = input("Введите фразу:")
polindrome(abc)