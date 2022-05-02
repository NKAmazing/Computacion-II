import os, argparse, time
import mmap, signal, sys


def main():
    parser = argparse.ArgumentParser(description="Memory Maping.\n Escriba path de archivo y el programa se ejecutara.")
    parser.add_argument("-f", type=str, help="Introduce path de archivo")
    global args
    args = parser.parse_args()
    # utilizo un if para ejecutarlo y llamar a sus funciones
    if args.f:
        execute(args)
    else:
        print("Faltan argumentos que pasarle a la terminal.")
        print("Para mas detalles, utilice -h o --help para recibir mas ayuda.")

def handler_parent(s, f):
    if s == signal.SIGUSR1:
        print("rebobinando...")
        memory.seek(0)
        print("leyendo desde la memoria - ", memory.tell())
        read = memory.read(filesize)
        print("Padre leyendo: ", read.decode())
        os.kill(list_pid[1], signal.SIGUSR1)
    elif s == signal.SIGUSR2:
        os.kill(list_pid[1], signal.SIGUSR2)
        os.wait()
        print("Padre saliendo")
        sys.exit(0)


def handler_child(s, f):
    if s == signal.SIGUSR1:
        print("Hijo 2 notificado...")
        # memory.seek(0)
        # read = memory.read(filesize).decode().upper()
        read = memory.readline().decode().upper()
        print(type(read))
        if not os.path.exists(args.f):
            fd = open(f"{args.f}", "w")
            fd.close
        with open(f"{args.f}", "a") as fd:
            fd.write(read.strip("\00"))
            fd.flush()
    elif s == signal.SIGUSR2:
        print("Hijo 2 saliendo")
        sys.exit(0)

def execute(args):
    global list_pid
    list_pid = []
    # utilizo mmap para crear la memoria compartida
    global memory, filesize
    filesize = 1024
    memory = mmap.mmap(-1, filesize)
    print("padre esperando...")

    for process in range(2):
        # utilizo fork
        global ret
        ret = os.fork()
        if ret == 0:
            list_pid.append(os.getpid())
            if process == 0:
                for line in sys.stdin:
                    if line[:3] == "bye":
                        os.kill(os.getppid(), signal.SIGUSR2)
                        print("Hijo 1 saliendo")
                        sys.exit(0)
                    print("Hijo 1 escribiendo en la memoria - ", memory.tell())
                    memory.write(bytes(line.encode()))
                    os.kill(os.getppid(), signal.SIGUSR1)
            else:
                
                signal.signal(signal.SIGUSR1, handler_child)
                signal.signal(signal.SIGUSR2, handler_child)
                while True:
                    signal.pause()
        else: 
            list_pid.append(ret)
            
        
    # padre
    print(list_pid)
    signal.signal(signal.SIGUSR1, handler_parent)
    signal.pause()

    signal.signal(signal.SIGUSR2, handler_parent)
    signal.pause()
    # print("Padre saliendo")


    os.wait()

if __name__ == '__main__':
    main()