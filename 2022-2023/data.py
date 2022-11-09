class Data:
    def __init__(self, row: str):
        data = row.strip().split(';')
        self.Name = data[0]
        self.Condition = data[1]
        self.Guarantee = data[2]
        self.CurrentPrice = int(data[3])
        self.FixPrice = data[4]
        self.Place = data[5]
        self.Link = data[6]
        self.Modify = data[7]
