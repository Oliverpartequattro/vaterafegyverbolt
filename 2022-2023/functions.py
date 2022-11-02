from data import Data
import os
Weapons = []
def ReadFile():
    f = open('Vatera_fegyverbolt.csv', 'r', encoding = 'UTF-8')
    for row in f :
        r = Data(row.strip())
        Weapons.append(r)
    f.close
    return Weapons 

def Print(row: str):
    print(f'Név:{row.Name} Állapot:{row.Condition} Garancia:{row.Guarantee} Jelenlegi Ár:{row.CurrentPrice} Vételár:{row.FixPrice} Link:{row.Link}')

def ViewList():
    os.system('cls')
    print('1.Listázás név alapján')
    print('2.Listázás állapot alapján')
    print('3.Listázás garancia alapján')
    print('4.Listázás jelenlegi ár alapján')
    print('5.Listázás vételár alapján')
    print('6.Listázás link alapján')
    Choice = int(input("Kérjük válasszon szempontot: "))
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
    Choice2 = int(input("Részletesebb információért írja be a fegyver sorszámát: "))
    print(f'{Print(Weapons[Choice2])}\n')
    input('')

#Név;Állapot;Garancia;Jelenlegi ár:;Fix ár:;Link

def NewWeapon():
    name = input('Név: ')
    condition = input('Állapot: ')
    guarantee = input('Grancia: ')
    currentprice = input('Legnagyobb licit: ')
    fixprice = input('Vételár:')
    link = input('Link: ')

    row = f'{name};{condition};{guarantee};{currentprice};{fixprice};{link}\n'
    f = open('Vatera_fegyverbolt.csv', 'a', encoding='UTF-8')
    f.write(row)
    f.close()

    r = Data(row)
    Weapons.append(r)

def writeFile():
    f = open('Vatera_fegyverbolt.csv', 'w', encoding='UTF-8')
    for r in Weapons:
        row = f'{r.name};{r.condition};{r.guarantee};{r.currentprice};{r.fixprice};{r.link}\n'
        f.write(row)
    f.close()

def DeleteWeapon():
    name = input('Név: ')
    for r in Weapons:
        if r.name.lower() == name.lower():
            Weapons.remove(r)
            writeFile()
            return
    input('Ilyen fegyver nics')
    
def licit():
    name = input('Amire licitálni szeretnél: ')
    for r in Weapons:
        if r.name.lower() == name.lower():
            NewLicit =  input('Mennyivel licitálsz?')
            if NewLicit > r.currentprice:
                r.currentprice = NewLicit
            else:
                print('192.176.45,34')
            writeFile()
            return
    input('Ilyen nevű vizsgázó nem volt')
    