import socket
import sys
import const as cs
import click
import pickle

def socket_create():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print(cs.SV_ERR)
        sys.exit()
    return s
            

@click.command()
@click.option('-ho', '--host', prompt='Enter host', type=str, help=(cs.HOST_INFO_HELP))
@click.option('-p', '--port', prompt='Enter port', type=int, help=(cs.PORT_INFO_HELP))

def execute_client(host, port):
    s = socket_create()
    s.connect((host, port))

    while True:
        # To quit -->  press Ctrl + C
        msg = input(cs.CLIENT_MSG)
        if msg != '':
            # Set the whole string
            s.send(msg.encode(cs.CHAR_CODE))
            msg = s.recv(1024)
            msg_decode = pickle.loads(msg)
            for i in range(len(msg_decode)):
                print(msg_decode[i].decode(cs.CHAR_CODE))

if __name__ == '__main__':
    execute_client()