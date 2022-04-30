import os, argparse, time
import mmap, signal, sys


def main():
    parser = argparse.ArgumentParser(description="Memory Maping.\n Escriba path de archivo y el programa se ejecutara.")
    parser.add_argument("-f", type=str, help="Introduce path de archivo")
    args = parser.parse_args()
    # utilizo un if para ejecutarlo y llamar a sus funciones
    if args.f:
        execute(args)
    else:
        print("Faltan argumentos que pasarle a la terminal.")
        print("Para mas detalles, utilice -h o --help para recibir mas ayuda.")

def handler_parent(s, f):
    read = memory.readline()
    print("Padre leyendo: ", read.decode())

def execute(args):
    # utilizo mmap para crear la memoria compartida
    memory = mmap.mmap(-1, 100)
    # utilizo fork
    ret = os.fork()

    if ret == 0:
        n = input("Cuantas lineas quiere escribir? ")
        for i in range(n):
            sys.stdout.write("Escriba algo: ")
            sys.stdout.flush()
            line = sys.stdin.readline()
            memory.write(bytes(line))
            os.kill(os.getppid(), signal.SIGUSR1)

    signal.signal(signal.SIGUSR1, handler_parent)
    signal.pause()

    os.wait()
