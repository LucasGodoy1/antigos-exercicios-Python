# https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/funcoes-em-python/modulos/exercicio-100-funcoes-para-sortear-e-somar/
from random import randint

def sorteia (variavel):
    for c in range (5):
        variavel.append(randint(1, 10))


num = list()
sorteia(num) # LISTA VAZIA ESTÁ SENDO
#USADA NO DEF ELA SUBSTITUI A VARIAVEL NO DEF
print ('-'*30)
print (num)

def somapar(variavel):
    soma = 0
    for v in variavel: # usando a variavel num criada, como lista
        if v % 2 ==0:
            soma += v
    print (f'Somando os valores pares da {variavel} temos {soma}')

somapar(num) #LISTA VAZIA ESTÁ SENDO USADA NO DEF ELA SUBSTITUI A VARIAVEL NO DEF

