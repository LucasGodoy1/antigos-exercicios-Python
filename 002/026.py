


def impar(*args):
    par = []
    impar = []
    for item in args:
        if item %2 ==0:
            par.append(item)
        else:
            impar.append(item)
    if impar == []:
        impar = '[Nenhum]'
    elif par == []:
        par = '[Nenhum]'
    return f'Os numeros pares são {par} e Os impares são {impar}'
            
        



parouimpar = impar(1, 5, 6, 22, 6, 8, 9, 33, 29)
print (parouimpar)