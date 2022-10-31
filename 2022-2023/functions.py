from data import Weapons
def Name(row: str):
    return row.split(';')[0]

def Condition(row: str):
    return row.split(';')[1]

def Guarantee(row: str):
    return row.split(';')[2]

def CurrentPrice(row: str):
    return row.split(';')[3]

def FixPrice(row: str):
    return row.split(';')[4]

def Link(row: str):
    return row.split(';')[5]