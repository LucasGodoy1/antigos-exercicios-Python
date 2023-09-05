import random
print ('-' * 35)
print ('Vamos embalharar"')
print ('Descubra quem fara as coisas primeiro!')
print ('-' * 35)
n1 = str(input ('Nome: '))
n2 = str (input ('Nome:'))
n3 = str(input ('Nome: '))
n4 = str (input ("nome:" ))
li = [n1, n2, n3, n4]
random.shuffle(li)
print (li)
