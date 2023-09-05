sexo = str(input('Qual é seu sexo ? [M/F]')).strip().upper() [0]
while sexo not in 'MF':
    sexo = str(input('Qual é seu sexo ? [M/F]')).strip().upper()[0]
    print ('-'*40)
    print ('Sexo invalido!')
    print ('-'*40)
print ('Sexo registrado com sucesso ')