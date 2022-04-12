import os, argparse, time, string


def main():
    global lista
    # creo una lista con el patron de abecedario
    lista = list(string.ascii_uppercase)
    # le paso argumentos al codigo
    parser = argparse.ArgumentParser(description="Linea de comandos")
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("-n", type=int, help="Elegir numero")
    parser.add_argument("-r", type=int, help="Elige veces que se repite la letra")
    parser.add_argument("-f", type=str, help="Introduzca nombre de archivo")
    group.add_argument("-v", action='store_true', help="Activa modo verbose")
    args = parser.parse_args()
    # utilizo un if para ejecutarlo y llamar a sus funciones
    if args.n and args.r and args.f:
        create_file(args)
        execute_fork(args)
    else:
        print("Faltan argumentos que pasarle a la terminal.")
        print("Para mas detalles, utilice -h o --help para recibir mas ayuda.")

def create_file(args):
    if os.path.exists(args.f):
        fd = open(f"/home/nk-nicolas/Documentos/Computacion-II/Ejercicios/{args.f}.txt", "r")
    else:
        fd = open(f"/home/nk-nicolas/Documentos/Computacion-II/Ejercicios/{args.f}.txt", "w+")
    fd.close

def execute_fork(args):
    # ejecuto fork en un for, en rango de la cantidad indicada en -n 
    for i in range(args.n):
        retorno = os.fork()
        # uso un if para verificar si es el proceso hijo o el padre
        # aparece el hijo
        if retorno == 0:
            pid = os.getpid()
            global letra
            letra = lista[i]
            execute(args, pid)
            os._exit(0)
    # aparece el padre
    for i in range(args.n):
        os.wait()
    time.sleep(1)
    print("El proceso ha terminado de cargar los datos")

def execute(args, pid):
    # ejecuto un if para probar cuantas veces paso la misma letra
    if args.r >= 1:
        for g in range(args.r):
            # chequea si se ejecuto con modo verbose
            if args.v:
                mode_verbose(pid)
            # si no se ejecuto el -v ejecuta el almacenamiento de letra
            store_letter(args)
    else:
        print("Error en el argumento -r")

def mode_verbose(pid):
    print(f"Proceso {pid} escribiendo letra '{letra}'")

def store_letter(args):
    with open(f"/home/nk-nicolas/Documentos/Computacion-II/Ejercicios/{args.f}.txt", "a") as fd:
        fd.write(str(letra))
        fd.flush()
        time.sleep(1)

if __name__ == '__main__':
    main()
