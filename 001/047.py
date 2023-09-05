# https://www.youtube.com/watch?v=Kjpb_IAOKRQ
# REVISAR TUDO DEPOIS!
contador = 0
for lp in range (0,3):
    contador = contador + 1
    p1 = float(input('Qual é seu peso? {}°'.format(contador)))
    if contador ==1: # CLASSIFICANDO OS PRIMEIROS VALORES
        ma1 = p1
        me1 = p1
    else: # Dizendo  qual ele deve se tornar
        if p1 > ma1:
            ma1 = p1
        elif p1 < me1:
            me1 = p1

print ('o maior peso foi {}'.format(ma1))
print ('o menor peso foi {}'.format(me1))

