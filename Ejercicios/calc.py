import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', type=str, help='Elige una operacion (+, -, *, /)')
    parser.add_argument('-n', type=int, default=1, help= "Elige un numero del 1 al 9")
    parser.add_argument('-m', type=int, default=1, help= "Elige un numero del 1 al 9")
    args = parser.parse_args()
    sys.stdout.write(str(calculate(args)))


def calculate(args):

    if args.o == "*":
        total = args.n * args.m
    elif args.o == "+":
        total = args.n + args.m
    elif args.o == "-":
        total = args.n - args.m
    elif args.o == "/":
        total = args.n/args.m
    else:
        print("Error con los argumentos. Vuelva a intentarlo.")

    print(args.n, args.o, args.m, "=", total)


if __name__=='__main__':
    main()
