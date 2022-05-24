import argparse
import multiprocessing as mp
import os
import const as cs
import math
import time
import numpy as np

def main():
    # le paso argumentos al codigo
    parser = argparse.ArgumentParser(description=cs.POOL_ARG_DESCR)
    parser.add_argument("-p", type=int, help=cs.PROC_ARG_HELP)
    parser.add_argument("-f", type=str, help=cs.PATH_ARG_HELP)
    parser.add_argument("-c", type=str, help=cs.OP_ARG_HELP)
    args = parser.parse_args()
    # utilizo un if para ejecutarlo y llamar a sus funciones
    if args.p and args.f and args.c:
        matrix_function()
        file_operator(args)
    else:
        print(cs.ARGS_ERR)
        print(cs.HELP_MSG)

def matrix_function():
    list_mx = [[1, 2, 3], [4, 5, 6]]
    global array_mx
    array_mx = np.array(list_mx)

def file_operator(args):
    # revisa si no existe, en cuyo caso lo crea
    if not os.path.exists(args.f):
        with open(f"{args.f}", "w") as fd:
            fd.write(str(array_mx))
            fd.flush()
    # abro el archivo
    fd = open(f"{args.f}", "r")
    # llamo a la funcion que ejecutara mp
    execute_mp(args, fd)

def square_function(x):
    # calcula la potencia al cuadrado
    print(f"{cs.PS_PID_MSG} {os.getpid()} {cs.SQP_MSG} ")
    print(f"{cs.JUMP_LINE} {array_mx}")
    return (pow(x, 2))

def root_function(x):
    # calcula la raiz cuadrada
    print(f"{cs.PS_PID_MSG} {os.getpid()} {cs.SQRT_MSG} ")
    print(f"{cs.JUMP_LINE} {array_mx}")
    return (math.sqrt(x))

def log_function(x):
    # calcula el logaritmo
    print(f"{cs.PS_PID_MSG} {os.getpid()} {cs.LOG_MSG} ")
    print(f"{cs.JUMP_LINE} {array_mx}")
    return (math.log(x, 10))

def execute_mp(args, fd):
    # array_int = array_mx.astype(int)
    # leo el archivo
    content = fd.read()
    # ejecuto pool
    pool = mp.Pool(processes=(args.p))
    print(cs.JUMP_LINE)
    # ejecuto la operacion
    print(cs.OP_TITLE, args.c)
    print(cs.JUMP_LINE)
    if args.c == 'pot':
        result = pool.map(square_function, [array_mx])
    elif args.c == 'raiz':
        result = pool.map(root_function, [array_mx])
    elif args.c == 'log':
        result = pool.map(log_function, [array_mx])
    else:
        print(cs.UNK_OP)
        time.sleep(0.5)
        return
    time.sleep(0.5)
    print(cs.JUMP_LINE)
    # printeo resultado de la operacion
    print(cs.RESULT_MSG)
    print(cs.JUMP_LINE, result, cs.JUMP_LINE)
    time.sleep(0.5)
    # cierro el archivo
    fd.close()
    print(cs.END_MSG)
    
if __name__ == '__main__':
    main()

