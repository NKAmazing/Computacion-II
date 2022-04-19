import os, argparse, time


def main():
    # creo el texto que le voy a cargar al archivo
    text = """Hola Mundo \nque tal \neste es un archivo \nde ejemplo."""
    # le paso argumentos al codigo
    parser = argparse.ArgumentParser(description="Inversor de cadenas.\n Escriba path de archivo y el programa invertira las lineas de texto de ese archivo.")
    parser.add_argument("-f", type=str, help="Introduzca path de archivo")
    args = parser.parse_args()
    # utilizo un if para ejecutarlo y llamar a sus funciones
    if args.f:
        create_file(args, text)
    else:
        print("Faltan argumentos que pasarle a la terminal.")
        print("Para mas detalles, utilice -h o --help para recibir mas ayuda.")

def create_file(args, text):
    # revisa si no existe, en cuyo caso lo crea
    if not os.path.exists(args.f):
        with open(f"{args.f}", "w") as fd:
            fd.write(text)
    # abro el archivo
    fd = open(f"{args.f}", "r")
    # llamo a la funcion para usar fork y pipe
    execute_fork(fd)

def execute_fork(fd):
    # leo las lineas del texto
    lines = fd.readlines()
    # print(len(lines))

    list_read = []
    list_write = []

    # ejecuto un fork dentro de un for, en rango de la cantidad de lineas de mi fd
    for i in range(len(lines)):
        r, w = os.pipe()
        list_read.append(r)
        list_write.append(w)
        ret = os.fork()

        # aparece el hijo
        if ret == 0:
            read_write(list_read[i])
            # read = os.read(r, 100)
            # print("Hijos leyendo: \n", read.decode())
            os._exit(0)
    
    # aparece el padre
    time.sleep(1)
    for i in range(len(lines)):
        line = lines[i]
        os.write(list_write[i], bytes(line[::-1].encode()))
        time.sleep(1)
        # os.write(list_write[i], str.encode(line))

    for i in range(len(lines)):
        os.wait()

def read_write(r):
    time.sleep(1)
    read = os.read(r, 100)
    print(read.decode())
    
    
if __name__ == '__main__':
    main()