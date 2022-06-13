import tkinter as tk
import pdb
# pdb.set_trace()
total = 0
x = 1
raknesatt = 1
cont = 1
while cont != 0:
    intp = int(input('skriv in ett nummer.'))
    raknesatt = int(input('0:Avsluta,1:+,2:-,3:*,4:/'))
    if raknesatt == 0:
        print(intp)
    elif raknesatt == 1:
        intj = int(input('skriv in ett till nummer.'))
        print(intj+intp)
    elif raknesatt == 2:
        intj = int(input('skriv in ett till nummer.'))
        print(intp-intj)
    elif raknesatt == 3:
        intj = int(input('skriv in ett till nummer.'))
        print(intp * intj)
    elif raknesatt == 4:
        intj = int(input('skriv in ett till nummer.'))
        print(intp / intj)
    cont = int(input('0:Avsluta,1:Fortsätta?'))
    
