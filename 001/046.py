from datetime import date
atual = date.today().year
co = 1
co1 = 0
co2 = 0
for loop in range (0,7):
    n1 = int(input('Quando nasceu a {}° pessoa ?'.format(co)))
    idade = atual - n1
    co = co + 1
    if idade >=18:
        co1 = co1 + 1
    elif idade < 18:
        co2 = co2 + 1
print ('são {} pessoas adultas '.format(co1))
print ('são {} pessoas jovens'.format(co2))
