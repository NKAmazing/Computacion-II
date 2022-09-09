from main.functions import encrypt as enc
from main.functions import decrypt as dec
from main.constants import const as cs

def main():
    inp = input("Do you want to encrypt or decrypt your files? (E/D) : ")
    if inp == 'e':
        enc.execute()
    elif inp == 'd':
        dec.execute()


if __name__ == '__main__':
    main()