from celery import Celery
import os, time
import const as cs
import math
import numpy as np
import multiprocessing as mp

app = Celery('tasks', broker='redis://localhost', backend='redis://localhost:6379')

@app.task
def execute(path, calculate):
    # manejo de archivos
    file_operator(path, calculate)

@app.task
def matrix_function(result):
    array_mx = np.array(result)
    return array_mx

@app.task
def file_operator(path, calculate):
    # revisa si no existe, en cuyo caso lo crea
    with open(f"{path}", "w") as fd:
        fd.write(cs.MATRIX)
        fd.flush()
    # abro el archivo
    fd = open(f"{path}", "r")
    # llamo a la funcion que ejecutara mp
    execute_mp(calculate, fd)

@app.task
def square_function(x):
    # calcula la potencia al cuadrado
    print(f"{cs.PS_PID_MSG} {os.getpid()} {cs.SQP_MSG} ")
    print(f"{cs.JUMP_LINE} {x}")
    return (pow(x, 2))

@app.task
def root_function(x):
    # calcula la raiz cuadrada
    print(f"{cs.PS_PID_MSG} {os.getpid()} {cs.SQRT_MSG} ")
    print(f"{cs.JUMP_LINE} {x}")
    return (math.sqrt(x))

@app.task
def log_function(x):
    # calcula el logaritmo
    print(f"{cs.PS_PID_MSG} {os.getpid()} {cs.LOG_MSG} ")
    print(f"{cs.JUMP_LINE} {x}")
    return (math.log(x, 10))

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
