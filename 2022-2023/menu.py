import os
from data import Data
from functions import Weapons, Print, SearchByName
def Menu():
    os.system('cls')
    print('1.Fegyverek neve')
    print('2.Fegyverek állapottya')
    print('3.Fegyverek garacijája')
    print('4.Fegyverek jelenlegi ára')
    print('5.Fegyverek fi ára')
    print('6.Fegyverek linkje')
    Choice = int(input("Kérjük válasszá: "))
    Count = 0
    if Choice == 1:
        for row in Weapons:
            Count += 1
            print(f'{Count}.{row.Name}')
    elif Choice == 2:
        for row in Weapons:
            Count += 1
            print(f'{Count}.{row.Condition}')
    elif Choice == 3:
        for row in Weapons:
            Count += 1
            print(f'{Count}.{row.Guarantee}')
    elif Choice == 4:
        for row in Weapons:
            Count += 1
            print(f'{Count}.{row.CurrentPrice}')
    elif Choice == 5:
        for row in Weapons:
            Count += 1
            print(f'{Count}.{row.FixPrice}')
    elif Choice == 6:
        for row in Weapons:
            Count += 1
            print(f'{Count}.{row.Link}')
    Choice2 = int(input("Kérjük válasszá: "))
    print(f'{Print(Weapons[Choice2])}\n')