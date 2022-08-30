import socket
import sys
import const as cs

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print(cs.SV_ERR)
    sys.exit()

host = sys.argv[1]
port = int(sys.argv[2])

s.connect((host, port))

while True:
    # To quit -->  press Ctrl + C
    msg = input(cs.CLIENT_MSG)
    # Set the whole string
    s.send(msg.encode(cs.CHAR_CODE))
    msg = s.recv(1024)
    print(cs.SV_MSG + cs.JUMP_LINE + msg.decode(cs.CHAR_CODE))