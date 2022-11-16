from data import Data
import os
import locale
ShoppingCart = []
Weapons = []
def ReadFile():
    f = open('Vatera_fegyverbolt.csv', 'r', encoding = 'UTF-8')
    for row in f :
        r = Data(row.strip())
        Weapons.append(r)
    f.close()
    return Weapons 

def Print(row: str):
    return (f'Név: {row.Name}\nÁllapot: {row.Condition}\nGarancia: {row.Guarantee}\nJelenlegi Ár: {row.CurrentPrice} Ft\nVételár: {row.FixPrice} Ft\nÁru helye: {row.Place}\nLink: {row.Link}\nMódosítható-e: {row.Modify}')

def ViewList():
    os.system('cls')
    print('1.Listázás név alapján')
    print('2.Listázás állapot alapján')
    print('3.Listázás garancia alapján')
    print('4.Listázás jelenlegi ár alapján')
    print('5.Listázás vételár alapján')
    print('6.Listázás az áru helye alapján')
    print('7.Listázás link alapján')
    print('8.Listázás módosíthatóság alapján')
    Choice = int(input("Kérjük válasszon szempontot: "))
    Count = 0
    if Choice == 1:
        for row in Weapons:
            Count += 1
            print(f'\n{Count}.{row.Name}\n')
    elif Choice == 2:
        for row in Weapons:
            Count += 1
            print(f'\n{Count}.{row.Condition}\n')
    elif Choice == 3:
        for row in Weapons:
            Count += 1
            print(f'\n{Count}.{row.Guarantee}\n')
    elif Choice == 4:
        for row in Weapons:
            Count += 1
            print(f'\n{Count}.{row.CurrentPrice}\n Ft')
    elif Choice == 5:
        for row in Weapons:
            Count += 1
            print(f'\n{Count}.{row.FixPrice}\n Ft')
    elif Choice == 6:
        for row in Weapons:
            Count += 1
            print(f'\n{Count}.{row.Place}\n')
    elif Choice == 7:
        for row in Weapons:
            Count += 1
            print(f'\n{Count}.{row.Link}\n')
    elif Choice == 8:
        for row in Weapons:
            Count += 1
            print(f'\n{Count}.{row.Modify}\n')
    else:
        print('192.176.45.34\n')
    Choice2 = int(input("Részletesebb információért írja be a fegyver sorszámát: "))
    print(f'\n{Print(Weapons[Choice2-1])}\n')
    Choice3 = int(input('1 - Kosárba helyezés\n'))
    if Choice3 == 1:
        ShoppingCart.append(Weapons[Choice2 - 1])
    else:
        input('Vissza a főmenübe...')
    

#Név;Állapot;Garancia;Jelenlegi ár:;Fix ár:;Link

def NewWeapon():
    name = input('Név: ')
    condition = input('Állapot: ')
    guarantee = input('Grancia: ')
    currentprice = input('Legnagyobb licit (Ft): ')
    fixprice = input('Vételár (Ft):')
    place = input('Áru helye: ')
    link = input('Link: ')
    modify = 'Igen'

    row = f'{name};{condition};{guarantee};{currentprice};{fixprice};{place};{link};{modify}\n'
    f = open('Vatera_fegyverbolt.csv', 'a', encoding='UTF-8')
    f.write(row)
    f.close()

    r = Data(row)
    Weapons.append(r)

def writeFile():
    f = open('Vatera_fegyverbolt.csv', 'w', encoding='UTF-8')
    for r in Weapons:
        row = f'{r.Name};{r.Condition};{r.Guarantee};{r.CurrentPrice};{r.FixPrice};{r.Place};{r.Link};{r.Modify}'
        f.write(f'{row}\n')
    f.close()

def DeleteWeapon():
    ViewList()
    name = input('Törölni kívánt fegyver neve: ')
    for r in Weapons:
        if r.Name.lower() == name.lower() and r.Modify.lower() == 'igen':
            Weapons.remove(r)
            writeFile()
            return
    input('Ilyen fegyver nincs')
    
def licit():
    ViewList()
    name = input('Amire licitálni szeretne: ')
    for r in Weapons:
        if r.Name.lower() == name.lower():
            NewLicit =  input('Mennyivel licitálsz?: ')
            if NewLicit > r.CurrentPrice:
                NewLicit = int(NewLicit)
                locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
                r.CurrentPrice = (f'{NewLicit:n} Ft')
            else:
                print('192.176.45.34')
            writeFile()
            return
    input('Ilyen nevű fegyver nincs')

def ModifyWeapon():
    ViewList()
    name = input('Változtatni kívánt fegyver neve: ')
    for r in Weapons:
        if r.Name.lower() == name.lower() and r.Modify.lower() == 'igen':
            r.Name = input('Új név: ')
            r.Condition = input('Új állapot: ')
            r.Guarantee = input ('Új garancia: ')
            r.CurrentPrice = input('Új licitár (Ft): ')
            r.FixPrice = input('Új vételár (Ft): ')
            r.Place = input('Új Áru helye: ')
            r.Link = input('Új link: ')
            r.Modify = 'igen'
            writeFile()
            return
    input('Ilyen nevű fegyver nincs')

def ViewShoppingCart():
    Count = 0
    Sum = 0
    for row in ShoppingCart:
        if row.FixPrice != "Csak Licit":
            int(row.FixPrice)
        else:
            row.FixPrice = 0
        Count += 1
        print(f'{Count}. Név: {row.Name}\nÁllapot: {row.Condition}\nGarancia: {row.Guarantee}\nJelenlegi Ár: {row.CurrentPrice} Ft\nVételár: {row.FixPrice} Ft\nÁru helye: {row.Place}\nLink: {row.Link}\nMódosítható-e: {row.Modify}\n')
        Sum += int(row.FixPrice)
        if row.FixPrice == 0:
            print('A kosárban lévő termék(ek) közül legalább az egyikre csak licitálni lehet.')
        else:
            print(f'Összérték: {Sum} Ft')
    input('')
    