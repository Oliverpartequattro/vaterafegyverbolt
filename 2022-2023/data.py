class Data:
    def __init__(self, row: str):
        data = row.split(';')
        self.Name = data[0]
        self.Condition = data[1]
        self.Guarantee = data[2]
        self.CurrentPrice = data[3]
        self.FixPrice = data[4]
        self.Link = data[5]
