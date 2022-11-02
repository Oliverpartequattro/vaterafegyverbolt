from data import Weapons
from functions import Name, Condition, Guarantee, CurrentPrice, FixPrice, Link, Print
def Menu():
    print('1.Fegyverek neve')
    print('2.Fegyverek állapottya')
    print('3.Fegyverek garacijája')
    print('4.Fegyverek jelenlegi ára')
    print('5.Fegyverek fi ára')
    print('6.Fegyverek linkje')
    sdhgkjsdbsjk = int(input("Kérjük válasszá: "))
    if sdhgkjsdbsjk == 1:
        for i in range(len(Weapons)):
            print(f'{i}.{Name(Weapons[i])}')
    elif sdhgkjsdbsjk == 2:
        for i in range(len(Weapons)):
            print(f'{i}.{Condition(Weapons[i])}')
    elif sdhgkjsdbsjk == 3:
        for i in range(len(Weapons)):
            print(f'{i}.{Guarantee(Weapons[i])}')
    elif sdhgkjsdbsjk == 4:
        for i in range(len(Weapons)):
            print(f'{i}.{CurrentPrice(Weapons[i])}')
    elif sdhgkjsdbsjk == 5:
        for i in range(len(Weapons)):
            print(f'{i}.{FixPrice(Weapons[i])}')
    elif sdhgkjsdbsjk == 6:
        for i in range(len(Weapons)):
            print(f'{i}.{Link(Weapons[i])}')
    zwidbvdsbvdbv = int(input("Kérjük válasszá: "))
    print(f'{Print(Weapons[zwidbvdsbvdbv])}\n')

Menu()