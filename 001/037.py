v = 0
c = 0
for d in range (1,20,1):
    print (d)
    if d % 2 == 0:
        v = v + d
        c = c + 1
print ('resultado da soma {}'.format(v))
print ('Foi feito {} vezes'.format(c))
