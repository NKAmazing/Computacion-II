import argparse
from ast import arg
from asyncore import read
import sys
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, help="Ingresa el nombre de un archivo existente.")
    parser.add_argument('-o', type=str, help="Ingrese el nombre del archivo donde se copiara el contenido.")
    args = parser.parse_args()
    sys.stdout.write(str(copy(args)))


def copy(args):
    args1 = args.i

    if os.path.exists(args1) == True:
        exist = open(args.i, "r")
        content = exist.read()
        print(content)

        with open(args.i, "r") as read_file:
            with open(args.o, "w") as write_file:
                for line in read_file:
                    write_file.write(line)
                    return "Se ha copiado el archivo exitosamente."
    else:
        print("El archivo no existe.")
if __name__=='__main__':
    main()

