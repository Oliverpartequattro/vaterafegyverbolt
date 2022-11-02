from data import Data
import os
Weapons = []
def ReadFile():
    f = open('Vatera_fegyverbolt.csv', 'r', encoding = 'UTF-8')
    f.readline()
    for row in f :
        r = Data(row.strip())
        Weapons.append(r)
    f.close
    return Weapons

def Print(row: str):
    print(f'{row.Name} {row.Condition} {row.Guarantee} {row.CurrentPrice} {row.FixPrice} {row.Link}')

def SearchByName():
    Name = input('Név(részlet): ')
    for r in Weapons:
        if Name.lower() in r.Name.lower():
            print(f'{r.Name} {r.Module}: {r.Percent}%')
    input('\n')
    
def ViewList():
    os.system('cls')
    print('1.Fegyverek neve')
    print('2.Fegyverek állapottya')
    print('3.Fegyverek garacijája')
    print('4.Fegyverek jelenlegi ára')
    print('5.Fegyverek fi ára')
    print('6.Fegyverek linkje')
    print('7.Fegyverre licitálás')
    Choice = int(input("Kérjük válasszá: "))
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

def deleteResult():
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
    