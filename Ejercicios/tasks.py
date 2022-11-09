from celery import Celery
import os
import const as cs
import math

app = Celery('tasks', broker='redis://localhost', backend='redis://localhost:6379')

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

if __name__ == '__main__':
    app.start()
