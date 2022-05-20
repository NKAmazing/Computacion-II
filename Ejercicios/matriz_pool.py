import argparse
import multiprocessing as mp
import os
import const as cs
import math
import time

def main():
    # le paso argumentos al codigo
    parser = argparse.ArgumentParser(description=cs.POOL_ARG_DESCR)
    parser.add_argument("-p", type=int, help=cs.PROC_ARG_HELP)
    parser.add_argument("-f", type=str, help=cs.PATH_ARG_HELP)
    parser.add_argument("-c", type=str, help=cs.OP_ARG_HELP)
    args = parser.parse_args()
    # utilizo un if para ejecutarlo y llamar a sus funciones
    if args.p and args.f and args.c:
        file_operator(args)
    else:
        print(cs.ARGS_ERR)
        print(cs.HELP_MSG)


def file_operator(args):
    # revisa si no existe, en cuyo caso lo crea
    if not os.path.exists(args.f):
        with open(f"{args.f}", "w") as fd:
            fd.write(cs.MATRIX)
            fd.flush()
    # abro el archivo
    fd = open(f"{args.f}", "r")
    # llamo a la funcion que ejecutara mp
    execute_mp(args, fd)

def square_function(x):
    # calcula la potencia al cuadrado
    print(f"{cs.PS_PID_MSG} {os.getpid()} {cs.SQP_MSG} 2")
    return (pow(x, 2))

def root_function(x):
    # calcula la raiz cuadrada
    print(f"{cs.PS_PID_MSG} {os.getpid()} {cs.SQP_MSG} 16")
    return (math.sqrt(x))

def log_function(x):
    # calcula el logaritmo
    print(f"{cs.PS_PID_MSG} {os.getpid()} {cs.LOG_MSG} 2")
    return (math.log(x, 10))

def execute_mp(args, fd):
    # leo el archivo
    lines = fd.readlines()
    # ejecuto pool
    pool = mp.Pool(processes=(args.p))
    print(cs.JUMP_LINE)
    # ejecuto la operacion
    print(cs.OP_TITLE, args.c)
    print(cs.JUMP_LINE)
    if args.c == 'pot':
        result = pool.map(square_function, [2])
    elif args.c == 'raiz':
        result = pool.map(root_function, [16])
    elif args.c == 'log':
        result = pool.map(log_function, [2])
    else:
        print(cs.UNK_OP)
        time.sleep(0.5)
        return
    time.sleep(0.5)
    print(cs.JUMP_LINE)
    # printeo resultado de la operacion
    print(cs.RESULT_MSG, result)
    time.sleep(0.5)
    # cierro el archivo
    fd.close()
    
if __name__ == '__main__':
    main()

