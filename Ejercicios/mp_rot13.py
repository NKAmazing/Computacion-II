import multiprocessing as mp
import sys
import time
import os

def main():
    # abro stdin en este proceso
    fd = sys.stdin.fileno()
    # creo lista de mensajes
    global msg_list
    msg_list = []
    # creo lista de procesos
    p = []
    # se crea el pipe
    a, b = mp.Pipe()
    # se crea la queue
    q = mp.Queue()
    # creo los dos procesos hijos
    child = mp.Process(target=child_funtion, args=(b, q, fd))
    child_2 = mp.Process(target=child2_funtion, args=(a, q))
    # agrego los dos procesos hijos a la lista
    p.append(child)
    p.append(child_2)
    
    # inicio los procesos
    for i in range(len(p)):
        p[i].start()
    
    # libero los procesos
    for i in range(len(p)):
        p[i].join()

    # termina el padre
    time.sleep(1)
    print("\n")
    print("Parent process: We're done here")
    
def child_funtion(msg, q, fd):
    # re abro fd en este proceso
    sys.stdin = os.fdopen(fd)
    print("To stop writing, type 'stop'.")
    print("Child 1 writing on Pipe...\n")
    
    # escribo por terminal
    for line in sys.stdin:
        # agrego cada linea a una lista
        msg_list.append(line.strip("\n"))
        if line[:4] == "stop":
            print("Stoping stdin...\n")
            break  
        print("writing: ", line)

    # envio cada dato de la lista por un extremo del pipe
    for data in range(len(msg_list)):
        msg.send(msg_list[data])
    # cierro el extremo del pipe despues de enviar los datos
    msg.close()
    time.sleep(1)
    print("Child 1 reading from queue: ")
    for i in range(len(msg_list) - 1):
        print("-", q.get())

def child2_funtion(a, q):
    cond = True
    while cond == True:
        # recibo los mensajes a traves el pipe
        word = str(a.recv())
        if word == 'stop':
            break
        else:
            # lee por el pipe
            print("Reading from pipe: ")
            print("-", word)
            # llamo a la funcion para encriptar a rot13
            rot13(word, q)
    # cierro el otro extremo del pipe
    a.close()

def rot13(word, q):
    print("Sending message to queue...\n")
    # defino chars
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    # rota los caracteres de chars
    trans = chars[26:] + chars[:26]
    # paso argumento c (letra) a traves de lambda y utilizo un find por cada letra de mi palabra
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    # utilizo un join para unir cada c como un solo string
    q.put(''.join( rot_char(c) for c in word))

if __name__ == '__main__':
    main()
