import os, argparse, time, string


def main():
    global PID_lista, dicc_proc, lista
    PID_lista = []
    dicc_proc = {}
    lista = list(string.ascii_uppercase)
    parser = argparse.ArgumentParser(description="Linea de comandos")
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("-n", type=int, help="Elegir numero")
    parser.add_argument("-r", type=int, help="Elige veces que se repite la letra")
    parser.add_argument("-f", type=str, help="Introduzca nombre de archivo")
    group.add_argument("-v", action='store_true', help="Activa modo verbose")
    args = parser.parse_args()
    if args.n and args.r and args.f:
        create_file(args)
        execute_fork(args)
    else:
        print("Faltan argumentos que pasarle a la terminal.")
        print("Para mas detalles, utilice -h o --help para recibir mas ayuda.")


def execute_fork(args):
    # ejecuto fork en un for, en rango de la cantidad indicada en -n 
    for i in range(args.n):
        retorno = os.fork()
        # uso un if para verificar si es el proceso hijo o el padre
        # aparece el hijo
        if retorno == 0:
            pid = os.getpid()
            PID_lista.append(pid)
            # with open(f"/home/nk-nicolas/Documentos/Apuntes/Personal-Projects/Ejemplos/Python/{args.f}.txt", "a") as fd:
            #     fd.write(str(pid) + ",")
            # chequea si se ejecuto con modo verbose
            if args.v:
                mode_verbose(os.getpid())
                # convert(args)
                execute(args)
                os._exit(0)
            # si no se ejecuto el -v ejecuta el almacenamiento de letra
            else:
                # convert(args)
                execute(args)
                os._exit(0)
    # aparece el padre
    time.sleep(1)

    # with open(f"/home/nk-nicolas/Documentos/Apuntes/Personal-Projects/Ejemplos/Python/{args.f}.txt", "r") as fd:
    #     lines = fd.read().split(",")

    #     for line in lines:
    #         print(line)
    #         PID_lista.append(line)
        
    #     PID_lista.remove("")
    #     print(PID_lista)

    for i in range(args.n):
        os.wait()
    time.sleep(1)
    print('El proceso de suma ha terminado')
    print(dicc_proc)

def execute(args):
    # creo una lista con el patron de abecedario
    i = 0
    # uso un for para recorrer la lista de PIDs y agrego al diccionario de procesos las letras
    for g in range(len(PID_lista)):
        dicc_proc[PID_lista[g]] = lista[i]
        i += 1
    if args.r >= 1:
        for g in range(args.r):
            store_letter(args)
        # print("El proceso ha terminado de cargar los datos")
    # elif args.r == 1:
    #         store_letter(dicc_proc)
    #         # print("El proceso ha terminado de cargar los datos")
    else:
        print("Error en el argumento -r")

def create_file(args):
    if os.path.exists(args.f):
        fd = open(f"/home/nk-nicolas/Documentos/Computacion-II/Ejercicios/{args.f}.txt", "r")
    else:
        fd = open(f"/home/nk-nicolas/Documentos/Computacion-II/Ejercicios/{args.f}.txt", "w+")
    fd.close

# def convert(args):
#     with open(f"/home/nk-nicolas/Documentos/Apuntes/Personal-Projects/Ejemplos/Python/{args.f}.txt", "r") as fd:
#         lines = fd.read().split(",")

#         for line in lines:
#             # print(line)
#             PID_lista.append(line)
        
#         PID_lista.remove("")
#         print(PID_lista)
        

def store_letter(args):
    for i in dicc_proc.values():
        with open(f"/home/nk-nicolas/Documentos/Computacion-II/Ejercicios/{args.f}.txt", "a") as fd:
            fd.write(str(i))
            fd.flush()
            time.sleep(1)
    
    # i = 0
    # for g in range(PID_lista):
    #     dicc_proc[PID_lista[g]] = lista_abc[i]
    #     print(f'{dicc_proc.values(g)}')
    #     i += 1

def mode_verbose(pid, dicc_proc):
    print(f"Proceso {pid} escribiendo letra '{dicc_proc(pid)}'")
    time.sleep(1)

    

if __name__ == '__main__':
    main()
