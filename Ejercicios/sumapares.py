import os, time, subprocess, argparse


def main():
    suma = 0
    parser = argparse.ArgumentParser(description="Linea de comandos")
    parser = argparse.ArgumentParser(add_help=False)
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("-n", type=int, help="Elegir numero")
    group.add_argument("-he", action='store_true', help="Activa ayuda de uso")
    group.add_argument("-v", action='store_true', help="Activa modo verbose")
    args = parser.parse_args()
    if args.he:
        help_usage(args)
    else:
        print("Ejecutado sin ayuda.\n")
    if args.n:
        execute(args, suma)
        

def execute(args, suma):
    # ejecuto fork en un for, en rango de la cantidad indicada en -n 
    for i in range(args.n):
        retorno = os.fork()
        pid = os.getpid()
        ppid = os.getppid()
        # uso un if para verificar si es el proceso hijo o el padre
        # aparece el hijo
        if retorno == 0:
            # chequea si se ejecuto con modo verbose
            if args.v:
                mode_verbose(pid, ppid, suma)
                os._exit(0)
            # si no se ejecuto el -v ejecuta la suma de modo normal
            else:
                suma_pares(pid,ppid, suma)
                os._exit(0)
    # aparece el padre
    for i in range(args.n):
        os.wait()
    print('El proceso de suma ha terminado')
            
            
    
  

def suma_pares(pid, ppid, suma):
    for g in range(0, pid + 1):
        if g % 2 == 0:
            suma += g
    print(f'{pid} - {ppid}:', suma)      
        

def help_usage(args):
    print('\nAYUDA:\n \nDebera pasarle un argumento de numero al programa para que se ejecute: \n'
          '\nEjemplo: \n./sumapares.py -n 10\n \nDonde 10 es el numero indicado de procesos hijos '
          'que van a crearse. \nEl sistema mostrara los 10 procesos hijos con sus respectivas '
          'sumas de pares.\n')


def mode_verbose(pid, ppid, suma):
    print('Starting process', pid)
    time.sleep(1)
    suma_pares(pid, ppid, suma)
    time.sleep(1)
    print('Ending process', pid)


if __name__ == "__main__":
    main()
