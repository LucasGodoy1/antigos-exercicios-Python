def validação():
    while True:
        try:
            num = int(input('Digite um Numero'))
            print('\033[0;36mValdiado com sucesso!\033[m')
            break
        except:
            print ('\033[0;31mERRO! Digite um Numero!\033[0m')
    print (f'Voce Digitou {num}')

validação()