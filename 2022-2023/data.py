Weapons = []
f = open('Vatera fegyverbolt.csv', 'r', encoding='UTF-8')
for row in f:
    Weapons.append(row)
f.close()

class Data:
    def __init__(self, row: str):
        data = row.split(';')
        self.Name = data[0]
        self.Module = data[1]
        self.Time = data[2]
        self.Percent = int(data[3])
