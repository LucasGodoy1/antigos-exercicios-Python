def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Sua idade é {idade} anos Voce não vota!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Sua idade é {idade} Voto Opcional!'
    else:
        return f'Sua idade é {idade} Voto Obrigatorio!'
    

n1 = int(input("Em que ano voce nasceu ?"))

print (voto(n1))
