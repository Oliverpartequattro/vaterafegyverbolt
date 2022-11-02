from menu import Menu
from data import Data
from functions import Weapons, ReadFile, Print, SearchByName
ReadFile()
Choice = Menu()
while Choice != 0:
    if Choice == '1':
        SearchByName()
    if Choice == '2':
        pass
    if Choice == '3':
        pass
    if Choice == '4':
        pass
    Choice = Menu()