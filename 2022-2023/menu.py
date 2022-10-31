from data import Weapons
from functions import sdnuoboswdnbjownib, neobjepjibnokg, ewhugewhuibsdhv, énsfbofdnjbs, knsdjovbsdhbvds, wbzuvbqhbvdhi, ebuvhwbdivsudsbu
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
            print(f'{i}.{sdnuoboswdnbjownib(Weapons[i])}')
    elif sdhgkjsdbsjk == 2:
        for i in range(len(Weapons)):
            print(f'{i}.{neobjepjibnokg(Weapons[i])}')
    elif sdhgkjsdbsjk == 3:
        for i in range(len(Weapons)):
            print(f'{i}.{ewhugewhuibsdhv(Weapons[i])}')
    elif sdhgkjsdbsjk == 4:
        for i in range(len(Weapons)):
            print(f'{i}.{énsfbofdnjbs(Weapons[i])}')
    elif sdhgkjsdbsjk == 5:
        for i in range(len(Weapons)):
            print(f'{i}.{knsdjovbsdhbvds(Weapons[i])}')
    elif sdhgkjsdbsjk == 6:
        for i in range(len(Weapons)):
            print(f'{i}.{wbzuvbqhbvdhi(Weapons[i])}')
    zwidbvdsbvdbv = int(input("Kérjük válasszá: "))
    print(f'{ebuvhwbdivsudsbu(Weapons[zwidbvdsbvdbv])}\n')

Menu()