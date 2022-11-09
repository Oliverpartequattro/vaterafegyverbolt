from menu import *
from data import *
from functions import *
ReadFile()

choice = menu()
while choice != 0:
    if choice == 1:
        ViewList()
    if choice == 2:
        NewWeapon()
    if choice == 3:
        licit()
    if choice == 4:
        DeleteWeapon()
    if choice == 5:
        ModifyWeapon()
    if choice == 6:
        ViewShoppingCart()
    choice = menu()
    