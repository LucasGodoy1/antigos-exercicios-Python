def multi (*args):
    total = 1
    for num in args:
        total *= num
    return total


x = multi(5, 7, 9, 10)
print (x)