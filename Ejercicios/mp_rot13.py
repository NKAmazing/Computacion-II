import multiprocessing as mp
import sys
import time

def main():
    # creo lista de procesos
    p= []

    # creo el pipe
    a, b = mp.Pipe()
    
    # creo los dos procesos hijos
    child = mp.Process(target=child_funtion, args=(b, ))
    child_2 = mp.Process(target=child2_funtion, args=(a, ))

    # agrego los dos procesos hijos a la lista
    p.append(child)
    p.append(child_2)

    # inicio los procesos
    for i in range(2):
        p[i].start()
    
    # libero los procesos
    for i in range(2):
        p[i].join()

    # termina el padre
    time.sleep(0.5)
    print("Parent process: We're done here")
    
def child_funtion(conn):
    print("Child 1 writing on Pipe...")
    time.sleep(1)
    conn.send("hello world")
    conn.send("goodbye world")
    conn.close()

def child2_funtion(a):
    print("Child 2 reading: " + str(a.recv()))
    print("Child 2 reading: " + str(a.recv()))

if __name__ == '__main__':
    main()
