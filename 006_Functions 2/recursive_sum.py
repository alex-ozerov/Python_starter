def recur_sum(last):
    global start
    if last == start:
        return start
    else:
        return last + recur_sum(last - 1)


start = int(input("Enter a positive number"))
end = int(input("Enter a positive number"))
while True:
    if start < 1:
        start = int(input("Enter a positive number"))
    elif end < 1:
        end = int(input("Enter a positive number"))
    else:
        break

print("The sum is", recur_sum(end))
