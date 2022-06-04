import threading
import queue
import sys
import const as cs
import codecs
import time

def main():
    q = queue.Queue()
    s = threading.BoundedSemaphore(1)
    threads = []
    threads.append(threading.Thread(target=thread_function, args=(s, q), daemon=True))
    threads.append(threading.Thread(target=thread_2_function, args=(s, q), daemon=True))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    q.join()
    print(cs.END_MSG)

def thread_function(s, q):
    s.acquire()
    global items
    items = []
    for line in sys.stdin:
        if line[:5] == 'break':
            break
        print(f"{cs.L_ADDING_MSG} {line}")
        items.append(line)
        time.sleep(1)
    s.release()
    time.sleep(1)
    while True:
        print(cs.READ_MSG)
        item = q.get()
        print(f"{cs.THREAD_MSG} {item}")
        print(f"{cs.THREAD_MSG_2} {item}")
        q.task_done()
        if q.empty():
            break
            
def thread_2_function(s, q):
    s.acquire()
    for item in items:
        print(f"{cs.PUT_Q_MSG} {item}")
        item = codecs.encode(item, 'rot13')
        q.put(item)
        time.sleep(1)
    s.release()

if __name__ == '__main__':
    main()
