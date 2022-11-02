from data import Data
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
    f = open('ecdl.csv', 'w', encoding='UTF-8')
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
    