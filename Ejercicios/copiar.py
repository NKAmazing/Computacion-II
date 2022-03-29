import argparse as arg
import sys
import os


def main():
    parser = arg.ArgumentParser(description="Programa para copiar archivos")
    parser.add_argument('-i', type=str, help="Ingresa el nombre de un archivo existente.")
    parser.add_argument('-o', type=str, help="Ingrese el nombre del nuevo archivo.")
    args = parser.parse_args()
    sys.stdout.write(str(copy(args)))


def copy(args):
    args_2 = args.i

    if os.path.exists(args_2):
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


main()
