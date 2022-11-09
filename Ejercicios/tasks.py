from celery import Celery
import os
import const as cs
import math

app = Celery('tasks', broker='redis://127.0.0.1', backend='redis://127.0.0.1')

@app.task
def square_function(x):
    l = []
    # calcula la potencia al cuadrado
    print(f"{cs.PS_PID_MSG} {os.getpid()} {cs.SQP_MSG} ")
    print(f"{cs.JUMP_LINE} {x}")
    for i in x:
        data = (pow(i, 2))
        l.append(data)
    return l

@app.task
def root_function(x):
    l = []
    # calcula la raiz cuadrada
    print(f"{cs.PS_PID_MSG} {os.getpid()} {cs.SQRT_MSG} ")
    print(f"{cs.JUMP_LINE} {x}")
    for i in x:
        data = (math.sqrt(i))
        l.append(data)
    return l 

@app.task
def log_function(x):
    l = []
    # calcula el logaritmo
    print(f"{cs.PS_PID_MSG} {os.getpid()} {cs.LOG_MSG} ")
    print(f"{cs.JUMP_LINE} {x}")
    for i in x:
        data = (math.log(i, 10))
        l.append(data)
    return l

if __name__ == '__main__':
    app.start()
