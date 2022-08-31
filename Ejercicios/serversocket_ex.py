import pickle
import click
import const as cs
import subprocess
import socketserver
import time

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
                # ndata = str(out)
                out_data = (out).encode(cs.CHAR_CODE)
                check_msg = (cs.SV_CHECK).encode(cs.CHAR_CODE)
                # send back the output of the command
                list_data = [out_data, check_msg]
                serializacion = pickle.dumps(list_data)
                # self.request.sendall(out_data)
                # self.request.sendall(check_msg)
                self.request.sendall(serializacion)
            elif out == '':
                # error_cmd = str(err)
                err_data = (err).encode(cs.CHAR_CODE)
                check_msg = (cs.SV_ERR_CHECK).encode(cs.CHAR_CODE)
                # send back the output of the command
                self.request.sendall(err_data)
                self.request.sendall(check_msg)

class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

@click.command()
@click.option('-p', '--port', prompt='Enter port', type=int, help=(cs.PORT_INFO_HELP))
@click.option('-c', '--concurrency', prompt='Type of Concurrency', help=(cs.TYPE_CONC_HELP))

def execute(port, concurrency):
    
    HOST, PORT = cs.HOST_ARG, port
    socketserver.TCPServer.allow_reuse_address = True

    if concurrency == 't':
        print(cs.JUMP_LINE, cs.LAUNCH_SVT, cs.JUMP_LINE)
        # Create the server, binding to localhost on a specific
        with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C

            server.serve_forever()
    elif concurrency == 'p':
        print(cs.JUMP_LINE, cs.LAUNCH_SVP, cs.JUMP_LINE)
        # Create the server, binding to localhost on a specific port
        with ForkedTCPServer((HOST, PORT), MyTCPHandler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C

            server.serve_forever()
    else:
        print(cs.ARGS_ERR_2)

if __name__ == '__main__':
    execute()