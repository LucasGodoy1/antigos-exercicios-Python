n1 = int(input('Digite um valor para converter'))
print ('''Escolha uma opção apra converter
 [ 1 ] Converter Para BINARIO
 [ 2 ] Converter Para OCTAL
 [ 3 ] Converter para HEXDECIMAL''')
op = int(input('Sua opção'))
if op == 1:
    print ('Seu numero {} convertido para BIANRIO É {}'.format(n1, bin(n1)))
elif op == 2:
    print ('Seu numero {} convertido para OCTAL É {}'.format(n1,oct(n1)))
elif op == 3:
    print ('Seu numero {} convertido para HEXDECIMAL É {}'.format(n1, hex(n1)))
else: print ('OPÇÃO INVALIDA!')