r = 0
c = 0
for t in range (1,501,2):
    if t % 3 ==0: # A conta só acontece se for multiplo de 3
        c = c + 1 # Quantas vezes foi feito o loop dentro do IF:
        r = r + t
print ('A soma de todos os {} valroes impares é {}'.format(c, r))
print ('FIM')