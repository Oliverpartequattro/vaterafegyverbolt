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
    print(f'{row.Name}{row.Condition}{row.Guarantee}{row.CurrentPrice}{row.FixPrice}{row.Link}')

def SearchByName():
    Name = input('Név(részlet): ')
    for r in Weapons:
        if Name.lower() in r.Name.lower():
            print(f'{r.Name} {r.Module}: {r.Percent}%')
    input('\n')

#Név;Állapot;Garancia;Jelenlegi ár:;Fix ár:;Link