import os
from data import Data
from functions import *

def menu():
    os.system('cls')
    print('1..Fegyver keresése (bármilyen adat alapján)')
    print('2..Új fegyver rögzítése')
    print('3..Fegyverre licitálás')
    print('4..Fegyver törlése')
    print('')
    print('0..Kilépés a programból')

    choice = input('\nVálasztás (0..4): ')
    while len(choice) != 1 or choice < '0' or choice > '4':
        choice = input('\nVálasztás (0..4): ')

    os.system('cls')
    return int(choice)

    