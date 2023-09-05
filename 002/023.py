def fact (n):
    f = 1
    for c in range (1, n+1):
        f = f * c
    return f


n1 = int(input('Digite um numero para o fatorial'))

fat = fact(n1)
print (f'o fatorial de {n1} é {fat}')