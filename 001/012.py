n = str(input ('Digite seu nome completo: ')).strip()
print ('seu nome em caixa alta é: {}'.format(n.upper()))
print ('seu nome em caixa baixa é {}'.format(n.lower()))
print ('vamos contar os digitos em seu nome {}'.format(len(n)))
print ('vamso contar sem os espaços: {}'.format(len(n) - n.count('')))
