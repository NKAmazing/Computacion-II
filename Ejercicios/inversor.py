import os, argparse, time


def main():
    # creo el texto que le voy a cargar al archivo
    text = """Hola Mundo \nque tal \neste es un archivo \nde ejemplo.\n"""
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
    
    # establezco dos listas, una de lectura y otra de escritura
    list_read = []
    list_write = []

    # utlizo un for para operar pipe y fork segun la cantidad de lineas de mi archivo
    for i in range(len(lines)):
        # uso el pipe
        r, w = os.pipe()
        # cada r se agrega a la lista
        list_read.append(r)
        # cada w se agrega a la lista
        list_write.append(w)
        # utilizo fork
        ret = os.fork()

        # aparece el hijo
        if ret == 0:
            # el hijo llama a la funcion read_line que leera una linea del archivo
            read_line(list_read[i])
            os._exit(0)
    
    # aparece el padre y escribe el archivo en un pipe
    time.sleep(1)
    for i in range(len(lines)):
        line = lines[i]
        # lee la lista donde esta almacenado cada w, en posicion de i, y luego a cada linea la invierte
        os.write(list_write[i], bytes(line[::-1].encode()))
        time.sleep(1)

    for i in range(len(lines)):
        os.wait()

def read_line(r):
    time.sleep(1)
    # el hijo lee la linea que mando el padre
    read = os.read(r, 100)
    print(read.decode())
    
    
if __name__ == '__main__':
    main()