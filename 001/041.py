n1 = int(input('Digite um numero'))
co = 0
for c in range(1, n1 +1):
    if n1 % c ==0:
        print ('\033[34m')
    else: print ('\032[33m')
