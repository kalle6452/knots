import random
import pdb
kort_1 = (random.randrange(1, 12))
kort_2 = (random.randrange(1, 12))
kort_3 = (random.randrange(1, 12))
kort_4 = (random.randrange(1, 12))
print(kort_1)
print(kort_2)
print(kort_3)
print(kort_4)
summa = kort_1 + kort_2
summa1 = kort_4 + kort_3
if summa > 21:
    print('förlust')
elif summa == 21:
    print('blackjack')
cont = input('vill du fortsätta?')
while cont == 'y':
    summa += (random.randrange(1, 12))
    print(summa)
    cont = input('vill du fortsätta?')
print(summa)
print(summa1)
#pdb.set_trace()
while summa1 < 17:
    summa1 += (random.randrange(1, 12))
print(summa1)
if summa > 21:
    print('tjock')
elif summa == 21:
    print('blackjack')
elif summa1 > 21:
    print('seger')
elif summa1 > summa:
    print('förlust')
elif summa > summa1:
    print('seger')
else:
    print('pengarna tillbaka')
