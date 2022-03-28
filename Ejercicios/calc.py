import getopt
import sys


def calculadora():
    args = (sys.argv[1:])
    opts = "o:n:m:"

    (opts, arg) = getopt.getopt(args, opts)

    operacion = None
    n = None
    m = None

    for op, ar in opts:
        if op in ['-o']:
            operacion = ar
        elif op in ['-n']:
            n = int(ar)
        elif op in ['-m']:
            m = int(ar)

    if operacion == '+':
        total = (n + m)
        print('El resultado es: ', total)
    elif operacion == '-':
        total = (n - m)
        print('El resultado es: ', total)
    elif operacion == 'x':
        total = (n * m)
        print('El resultado es: ', total)
    elif operacion == '/':
        total = (n / m)
        print('El resultado es: ', total)
    else:
        print("Operacion invalida")


calculadora()
