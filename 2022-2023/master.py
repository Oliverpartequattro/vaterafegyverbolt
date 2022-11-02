from menu import *
from data import *
from functions import *
ReadFile()

choice = menu()
while choice != 0:
    if choice == 1:
        newResult()
    if choice == 2:
        modifyResult()
    if choice == 3:
        deleteResult()
    if choice == 4:
        searchByName()
    choice = menu()
    