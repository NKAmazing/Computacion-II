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
    print("Parent process: We're done here")
    
def child_funtion(msg, q, fd):
    # re abro fd en este proceso
    sys.stdin = os.fdopen(fd)
    print("To stop writing, type 'stop'.")
    print("Child 1 writing on Pipe...\n")
    

    for line in sys.stdin:
        msg_list.append(line.strip("\n"))
        if line[:4] == "stop":
            print("Stoping stdin...\n")
            break  
        print("writing: ", line)

    for data in range(len(msg_list)):
        msg.send(msg_list[data])
    msg.close()
    time.sleep(1)
    print("Child 1 reading from queue: ")
    for i in range(len(msg_list) - 1):
        print("-", q.get())

def child2_funtion(a, q):
    cond = True
    while cond == True:
        word = str(a.recv())
        if word == 'stop':
            break
        else:
            print("Reading from pipe: ")
            print("-", word)
            rot13(word, q)
    a.close()

def rot13(word, q):
    print("Sending message to queue...\n")
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    trans = chars[26:] + chars[:26]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    q.put(''.join( rot_char(c) for c in word))

if __name__ == '__main__':
    main()
