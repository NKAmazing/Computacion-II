import threading
import queue
import sys
import const as cs
import codecs
import time

def main():
    q = queue.Queue()
    s = threading.BoundedSemaphore(1)
    q2 = queue.Queue()
    threads = []
    threads.append(threading.Thread(target=thread_function, args=(s, q, q2), daemon=True))
    threads.append(threading.Thread(target=thread_2_function, args=(s, q, q2), daemon=True))
    for thread in threads:  # Starting all the threads
        thread.start()
    for thread in threads:  # Waits for threads to complete before moving on with the main script.
        thread.join()
    q.join()
    q2.join()
    print(cs.END_MSG)

def thread_function(s, q, q2):
    s.acquire()
    print(cs.INPUT_MSG)
    print(cs.JUMP_LINE)
    for line in sys.stdin:
        if line[:5] == cs.ARG_STR:
            break
        print(f"{cs.Q_ADDING_MSG} {line}")
        q2.put(line.strip("\n"))
        time.sleep(1)
    s.release()
    time.sleep(1)
    s.acquire()
    while True:
        print(cs.READ_MSG)
        time.sleep(0.5)
        print(cs.JUMP_LINE)
        item = q.get()
        print(f"{cs.THREAD_MSG_3} '{item}'")
        q.task_done()
        print(cs.JUMP_LINE)
        time.sleep(1)
        if q.empty():
            break
    s.release()
            
def thread_2_function(s, q, q2):
    s.acquire()
    print(cs.JUMP_LINE)
    while True:
        print(cs.READ_MSG)
        time.sleep(0.5)
        print(cs.JUMP_LINE)
        item = q2.get()
        print(f"{cs.PUT_Q_MSG} {item}")
        item = codecs.encode(item, cs.ARG_ROT_13)
        q.put(item)
        q2.task_done()
        print(cs.JUMP_LINE)
        time.sleep(1)
        if q2.empty():
            break
    s.release()
    

if __name__ == '__main__':
    main()
