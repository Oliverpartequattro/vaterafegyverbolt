import os
from data import Data
from functions import *

def menu():
    os.system('cls')
    print('1..Új eredmény rögzítése')
    print('2..Eredmény módosítása')
    print('3..Eredmény törlése')
    print('4..Eredmény keresése (név alapján)')
    print('')
    print('0..Kilépés a programból')

    choice = input('\nVálasztás (0..4): ')
    while len(choice) != 1 or choice < '0' or choice > '4':
        choice = input('\nVálasztás (0..4): ')

    os.system('cls')
    return int(choice)

    