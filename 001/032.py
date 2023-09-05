prec = float(input('Qual o preço das compras? '))
print ('''Como deseja pagar?
[1] à vista
[2] cartão de debito
[3] 2x no cartão
[4] 3x no cartão ou mais
[0] cancelar compra''')
op = int(input('Sua opção'))
if op == 1:
    print ('preço a pagar é R${}'.format(prec - prec * 10 / 100))
elif op == 2:
    print ('preço a pagar é R${}'.format(prec - prec * 5 / 100))
elif op == 3:
        print ('preço a pagar é R${}'.format(prec))
elif op == 4:
    par = int(input('Quantas parcelas?'))
    print ('preço a pagar é R${}'.format(prec + prec * 20 / 100))
elif op == 0:
    print ('compra cancelada com sucesso! ')