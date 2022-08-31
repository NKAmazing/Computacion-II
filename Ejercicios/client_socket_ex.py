import socket
import sys
import const as cs
import click
import pickle

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print(cs.SV_ERR)
    sys.exit()

@click.command()
@click.option('-ho', '--host', prompt='Enter host', type=str, help=(cs.HOST_INFO_HELP))
@click.option('-p', '--port', prompt='Enter port', type=int, help=(cs.PORT_INFO_HELP))

def execute_client(host, port):
    s.connect((host, port))

    while True:
        # To quit -->  press Ctrl + C
        msg = input(cs.CLIENT_MSG)
        # Set the whole string
        s.send(msg.encode(cs.CHAR_CODE))
        msg = s.recv(1024)
        msg_decode = pickle.loads(msg)
        # print(cs.SV_MSG + cs.JUMP_LINE + msg.decode(cs.CHAR_CODE))
        # print(cs.SV_MSG + cs.JUMP_LINE + msg[0].decode(cs.CHAR_CODE))
        for i in range(len(msg_decode)):
            print(msg_decode[i].decode(cs.CHAR_CODE))


if __name__ == '__main__':
    execute_client()