import socket
import multiprocessing as mp
import argparse as arg
import const as cs
import signal

def main():
    parser = arg.ArgumentParser(description="Server Socket Stream")
    parser.add_argument("-ho", type=str, help="Host of connection")
    parser.add_argument("-p", type=int, help="Port of connection")
    args = parser.parse_args()
    if args.ho and args.p:
        execute(args)
    else:
        print(cs.ARGS_ERR)

def execute(args):
    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    host = (args.ho)
    port = (args.p)

    # bind to the port
    serversocket.bind((host, port))

    serversocket.listen(5)

    while True:
        clientsocket, addr = serversocket.accept()
        client = mp.Process(target=client_function, args=(clientsocket, addr))
        client.start()


def client_function(clientsocket, addr):
    while True:
        # establish a connection
        data = clientsocket.recv(1024)
        if data.decode()[:3] == cs.ARG_2_STR:
            print(cs.EXIT_PROCESS)
            exit(0)
        print("Address: %s " % str(addr))
        print(f"{cs.RCV_MSG} "+data.decode(cs.CHAR_CODE))
        msg = data.decode().upper()
        clientsocket.send(msg.encode(cs.CHAR_CODE))

if __name__ == '__main__':
    main()