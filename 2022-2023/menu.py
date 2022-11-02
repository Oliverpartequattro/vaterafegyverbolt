from data import Weapons
from functions import Name, Condition, Guarantee, CurrentPrice, FixPrice, Link, Print
def Menu():
    print('1.Fegyverek neve')
    print('2.Fegyverek állapottya')
    print('3.Fegyverek garacijája')
    print('4.Fegyverek jelenlegi ára')
    print('5.Fegyverek fi ára')
    print('6.Fegyverek linkje')
    choice = int(input("Kérjük válasszá: "))
    if choice == 1:
        for i in range(len(Weapons)):
            print(f'{i}.{Name(Weapons[i])}')
    elif choice == 2:
        for i in range(len(Weapons)):
            print(f'{i}.{Condition(Weapons[i])}')
    elif choice == 3:
        for i in range(len(Weapons)):
            print(f'{i}.{Guarantee(Weapons[i])}')
    elif choice == 4:
        for i in range(len(Weapons)):
            print(f'{i}.{CurrentPrice(Weapons[i])}')
    elif choice == 5:
        for i in range(len(Weapons)):
            print(f'{i}.{FixPrice(Weapons[i])}')
    elif choice == 6:
        for i in range(len(Weapons)):
            print(f'{i}.{Link(Weapons[i])}')
    choice2 = int(input("Kérjük válasszá: "))
    print(f'{Print(Weapons[choice2])}\n')

Menu()