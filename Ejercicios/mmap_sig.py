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
        # usamos un seek para volver al principio y leemos
        print("rebobinando...")
        memory.seek(0)
        print("leyendo desde la memoria - ", memory.tell())
        read = memory.read(filesize)
        print("Padre leyendo: ", read.decode())
        os.kill(list_pid[1], signal.SIGUSR1)
    elif s == signal.SIGUSR2:
        # manda señal al hijo 2, espera, y luego sale
        os.kill(list_pid[1], signal.SIGUSR2)
        os.wait()
        print("Padre saliendo")
        sys.exit(0)


def handler_child(s, f):
    if s == signal.SIGUSR1:
        # recibe la señal, lee la memoria y guarda en el archivo
        print("Hijo 2 notificado...")
        read = memory.readline().decode().upper()
        # print(type(read))
        if not os.path.exists(args.f):
            fd = open(f"{args.f}", "w")
            fd.close
        with open(f"{args.f}", "a") as fd:
            fd.write(read.strip("\00"))
            fd.flush()
    elif s == signal.SIGUSR2:
        # recibe la otra señal y sale
        print("Hijo 2 saliendo")
        sys.exit(0)

def execute(args):
    global list_pid
    list_pid = []
    # utilizo mmap para crear la memoria compartida
    global memory, filesize
    filesize = 1024
    memory = mmap.mmap(-1, filesize)
    print("padre esperando...\n")
    # forkeo dos veces
    for process in range(2):
        # utilizo fork
        global ret
        ret = os.fork()
        # itero con un if, si es el hijo, agrego a la lista el pid
        if ret == 0:
            list_pid.append(os.getpid())
            # hijo 1
            if process == 0:
                # recorro con un for el sys.stdin para pasar datos por terminal
                for line in sys.stdin:
                    # si line es 'bye', manda una señal al padre y sale
                    if line[:3] == "bye":
                        time.sleep(1)
                        os.kill(os.getppid(), signal.SIGUSR2)
                        print("Hijo 1 saliendo")
                        sys.exit(0)
                    # el hijo escribe en la memoria y manda una señal al padre
                    print("Hijo 1 escribiendo en la memoria - ", memory.tell())
                    memory.write(bytes(line.encode()))
                    print("Hijo 1 terminado de escribir la linea - ", memory.tell())
                    os.kill(os.getppid(), signal.SIGUSR1)
            # hijo 2
            else:
                # recibe las señales del padre
                signal.signal(signal.SIGUSR1, handler_child)
                signal.signal(signal.SIGUSR2, handler_child)
                while True:
                    signal.pause()
        else: 
            list_pid.append(ret)
            
        
    # padre
    signal.signal(signal.SIGUSR2, handler_parent)
    signal.signal(signal.SIGUSR1, handler_parent)
    signal.pause()

    os.wait()

if __name__ == '__main__':
    main()