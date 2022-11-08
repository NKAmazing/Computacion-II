import pickle
import click
import const as cs
import subprocess
import socketserver
import socket
import threading

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            # self.request is the TCP socket connected to the client
            self.data = self.request.recv(1024).strip()
            print("{} wrote:".format(self.client_address[0]))
            print(self.data.decode(cs.CHAR_CODE))
            # Decoding data and converting to string
            data_cmd = (self.data).decode()
            # Execute cmd with subprocess popen
            p = subprocess.Popen(data_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
            universal_newlines=True, shell=True)
            out, err = p.communicate()
            if err == '':
                out_data = (out).encode(cs.CHAR_CODE)
                check_msg = (cs.SV_CHECK).encode(cs.CHAR_CODE)
                # send back the output of the command
                list_data = [check_msg, out_data]
                serialization = pickle.dumps(list_data)
                self.request.sendall(serialization)
            elif out == '':
                err_data = (err).encode(cs.CHAR_CODE)
                check_msg = (cs.SV_ERR_CHECK).encode(cs.CHAR_CODE)
                # send back the output of the command
                list_data = [check_msg, err_data] 
                serialization = pickle.dumps(list_data)
                self.request.sendall(serialization)

class ForkedTCPServer6(socketserver.ForkingMixIn, socketserver.TCPServer):
    address_family = socket.AF_INET6
    pass

class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThreadedTCPServer6(socketserver.ThreadingMixIn, socketserver.TCPServer):
    address_family = socket.AF_INET6
    pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def services(d, concurrency):
    if concurrency == 't':
        print(cs.JUMP_LINE, cs.LAUNCH_SVT, cs.JUMP_LINE)
        if d[0] == socket.AF_INET:
            print("Launching with IPv4")
            # Create the server, binding to localhost on a specific
            with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
                # Activate the server; this will keep running until you
                # interrupt the program with Ctrl-C

                server.serve_forever()
        elif d[0] == socket.AF_INET6:
            print("Launching with IPv6")
            # Create the server, binding to localhost on a specific
            with ThreadedTCPServer6((HOST, PORT), MyTCPHandler) as server:
                # Activate the server; this will keep running until you
                # interrupt the program with Ctrl-C

                server.serve_forever()

    elif concurrency == 'p':
        print(cs.JUMP_LINE, cs.LAUNCH_SVP, cs.JUMP_LINE)
        if d[0] == socket.AF_INET:
            print("Launching with IPv4")
            # Create the server, binding to localhost on a specific port
            with ForkedTCPServer((HOST, PORT), MyTCPHandler) as server:
                # Activate the server; this will keep running until you
                # interrupt the program with Ctrl-C

                server.serve_forever()
        elif d[0] == socket.AF_INET6:
            print("Launching with IPv6")
            # Create the server, binding to localhost on a specific
            with ForkedTCPServer6((HOST, PORT), MyTCPHandler) as server:
                # Activate the server; this will keep running until you
                # interrupt the program with Ctrl-C

                server.serve_forever()
    else:
        print(cs.ARGS_ERR_2)

@click.command()
@click.option('-p', '--port', prompt='Enter port', type=int, help=(cs.PORT_INFO_HELP))
@click.option('-c', '--concurrency', prompt='Type of Concurrency', help=(cs.TYPE_CONC_HELP))

def execute(port, concurrency):
    global HOST, PORT
    HOST, PORT = cs.HOST_ARG, port
    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on a specific port
    directions = socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM)

    th_list = []
    print(directions)
    for d in directions:
        print(d[0])
        th_list.append(threading.Thread(target=services, args=(d, concurrency)))

    for th in th_list:
        th.start()
    

if __name__ == '__main__':
    execute()