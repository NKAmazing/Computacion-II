from subprocess import Popen, PIPE
import argparse as arg
import time
import os

now = time.strftime("%c")


def main():
    parser = arg.ArgumentParser(description="Linea de comandos")
    parser.add_argument("-c", type=str, help="Elegir comando")
    parser.add_argument("-f", type=str, help="Escribir nombre de archivo de salida")
    parser.add_argument("-l", type=str, help="Escribir nombre de archivo log")
    args = parser.parse_args()
    exist(args)
    comando(args)


def exist(args):
    if os.path.exists(args.f):
        archivo_f = open(f"/home/nk-nicolas/Documentos/Computacion-II/Ejercicios/{args.f}.txt", "r")
    else:
        archivo_f = open(f"/home/nk-nicolas/Documentos/Computacion-II/Ejercicios/{args.f}.txt", "w")
    if os.path.exists(args.l):
        archivo_l = open(f"/home/nk-nicolas/Documentos/Computacion-II/Ejercicios/{args.l}.txt", "r")
    else:
        archivo_l = open(f"/home/nk-nicolas/Documentos/Computacion-II/Ejercicios/{args.l}.txt", "w")


def comando(args):
        p = Popen(["{}".format(args.c)], stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        if p.returncode == 0:
            msg_1 = (now + f": Comando {args.c} ejecutado correctamente")
            with open(f"/home/nk-nicolas/Documentos/Computacion-II/Ejercicios/{args.f}.txt", "w") as fd:
                fd.write(str(out))
            with open(f"/home/nk-nicolas/Documentos/Computacion-II/Ejercicios/{args.l}.txt", "w") as ld:
                ld.write(str(msg_1))

        else:
            with open(f"/home/nk-nicolas/Documentos/Computacion-II/Ejercicios/{args.l}.txt", "w") as ld:
                ld.write(str(err))


if __name__ == '__main__':
    main()
