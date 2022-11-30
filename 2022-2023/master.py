from menu import *
from data import *
from functions import *
def Master():
    ReadMainFile()
    ReadSideFile()

    choice = menu()
    while True:
        if choice == 0:
            os.system("python login.py")
            exit()
        if choice == 1:
            ViewList(True)
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
    