


def multia(num):
    def multib(num2):
        return num * num2
    return multib


recebteste = multia(3)

print (recebteste(5))