# Att göra:
import pdb

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

def human():
    x = 1
    counter = 0
    x = int(input('skriv in ett nummer'))
    while len(lista[x]) != 0:
        print('vänligen skriv in ett nytt nummer')
        x = int(input('skriv in ett nummer'))
    lista[x].append(intj)
    tuple(lista[x])
    print(type(lista[x]))
    print(lista)
    counter += 1
def bot():
    rand = (random.randrange(1, 9))
    while len(lista[rand]) != 0:
        rand = (random.randrange(1, 9))
    lista[rand].append(intp)
    print(lista)
for i in range(0,3):
    print(lista[i])
human()
bot()
human()
bot()
human()
bot()
'''x = int(input('skriv in ett nummer'))
lista[x].append("intj")
print(lista)
x = int(input('skriv in ett nummer'))
lista[x].append("intj")
print(lista)'''

if lista[0] == [intj] and lista[1] == [intj] and lista[2] == [intj]:
    print('vinnare')
elif lista[0] == [intp] and lista[1] == [intp] and lista[2] == [intp]:
    print('vinnare')
