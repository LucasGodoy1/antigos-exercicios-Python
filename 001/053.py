continuar = 'S'
contador = soma = n2 = 0
while continuar != 'N':
    n2 = int(input('Digite um valor'))
    soma = soma + n2
    contador = contador + 1
    if contador ==1:
        maior = menor = n2
    else:
        if n2 > maior:
            maior = n2
        elif n2 < menor:
            menor = n2
    continuar = str(input('Deseja continuar ? [S/N]')).strip().upper()
media = soma / contador
print (contador)
print ('Voce digitou {} numeros e a média entre eles é {:.1f}'.format(contador, media))
print ('O menor numero digitado foi {} e o maior numero digitado foi {}'.format(menor, maior))
print ('Fim')
