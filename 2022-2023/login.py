import hashlib
from master import *

def signup():
    username = input('\nÍrja be a felhasználónevét: ')
    password = input('Írjon be egy jelszót: ')
    ConfirmPassword = input('Erősítse meg jelszavát: ')
    if ConfirmPassword == password:
        enc = ConfirmPassword.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open('bejelentkezesi_adatok.txt', 'w') as f:
            f.write(username + '\n')
            f.write(hash1)
        f.close()
        print('Sikeres regisztráció!\n')
        input('')
        os.system('cls')
    else:
        print('A két jelszó nem egyezik meg.\n')
        input()

def login():
    username = input('\nFelhasználónév: ')
    password = input('Jelszó: ')
    authorization = password.encode()
    AuthorizationHash = hashlib.md5(authorization).hexdigest()
    with open('bejelentkezesi_adatok.txt', 'r') as f:
        StoredUsername, StoredPassword = f.read().split('\n')
    f.close()
    if username == StoredUsername and AuthorizationHash == StoredPassword:
        print('Sikeres bejelentkezés!')
        Master()
    else:
        print('Sikertelen bejelentkezés!\n')
        input()
         
while True:
    print("\n********** Bejelentkezés **********")
    print('1..Új fiók létrehozása')
    print('2..Bejelentkezés')
    print('3..Kilépés a programból\n')
    choice = input('Választás: ')
    try:
        choice = int(choice)
    except ValueError:
        os. system("python login.py")
        print('192.176.45.34')
    choice = int(choice)
    if choice == 1:
        signup()
    elif choice == 2:
        login()
    elif choice == 3:
        break
