import os
from data import Data
from functions import *

def menu():
    os.system('cls')
    print("\n********** Menü **********")
    print('1..Fegyver keresése (bármilyen adat alapján)')
    print('2..Új fegyver rögzítése')
    print('3..Fegyverre licitálás')
    print('4..Fegyver törlése')
    print('5..Fegyver adatainak módosítása')
    print('6...Kosár megtekintése')
    print('')
    print('0..Kijelentkezés')

    choice = input('\nVálasztás (0..6): ')
    while len(choice) != 1 or choice < '0' or choice > '6':
        choice = input('\nVálasztás (0..6): ')

    os.system('cls')
    return int(choice)

    