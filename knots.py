# Att göras:
import pdb
x = 1
# Följ listan i mattehäftet.
import random
lista0 = [[],[],[],
         [],[],[],
         [],[],[],]
lista = [[],[],[],
         [],[],[],
         [],[],[],]
#print(lista)
#pdb.set_trace()
intj = int(input('skriv in 1("x") eller 0("o")'))
intp = ''
if intj == 1:
    intj = 'x'
    intp = 'o'
elif intj == 0:
    intj = 'o'
    intp = 'x'
print(intj)
print(lista)

x = int(input('skriv in ett nummer'))
lista[x].append(intj)
tuple(lista[x])
print(type(lista[x]))
print(lista)
rand = (random.randrange(1,9))
while len(lista[rand])!=0:
    rand = (random.randrange(1, 9))
lista[rand].append(intp)
print(lista)
'''x = int(input('skriv in ett nummer'))
lista[x].append("intj")
print(lista)
x = int(input('skriv in ett nummer'))
lista[x].append("intj")
print(lista)'''

if lista[0] == ['x'] and lista[1] == ['x'] and lista[2] == ['x']:
    print('vinnare')
