import click
import const as cs
import numpy as np
import multiprocessing as mp
import time
from tasks import *

@click.command()
@click.option('-p', '--path', prompt='Enter path', type=str, help=(cs.PATH_ARG_HELP))
@click.option('-c', '--calculate', prompt='Enter calculation operation', help=(cs.OP_ARG_HELP))
def main(path, calculate):
    execute(path, calculate)

def matrix_function(result):
    array_mx = np.array(result)
    return array_mx

def execute(path, calculate):
    # manejo de archivos
    fd = file_operator(path)
    execute_mp(calculate, fd)

def file_operator(path):
    # revisa si no existe, en cuyo caso lo crea
    with open(f"{path}", "w") as fd:
        fd.write(cs.MATRIX)
        fd.flush()
    # abro el archivo
    fd = open(f"{path}", "r")
    # llamo a la funcion que ejecutara mp
    return fd

def execute_mp(calculate, fd):
    result = []
    matrix = []
    # leo el archivo
    lines = fd.readlines()
    for line in lines:
        split = line.split(", ")
        split = list(map(int, split))
        matrix.append(split)

    print(matrix)
    
    # ejecuto pool
    pool = mp.Pool(processes=(4))
    print(cs.JUMP_LINE)
    # ejecuto la operacion
    print(cs.OP_TITLE, calculate)
    print(cs.JUMP_LINE)
    for m in matrix:
        if calculate == 'pot': 
            opt = pool.map(square_function, m)
            result.append(opt)
        elif calculate == 'raiz':
            opt = pool.map(root_function, m)
            result.append(opt)
        elif calculate == 'log':
            opt = pool.map(log_function, m)
            result.append(opt)
        else:
            print(cs.UNK_OP)
            time.sleep(0.5)
            return
    time.sleep(0.5)
    print(cs.JUMP_LINE)
    # printeo resultado de la operacion
    print(cs.RESULT_MSG)
    result_mx = matrix_function(result)
    print(cs.JUMP_LINE, result_mx, cs.JUMP_LINE)
    time.sleep(0.5)
    # cierro el archivo
    fd.close()
    print(cs.END_MSG)

if __name__ == '__main__':
    main()