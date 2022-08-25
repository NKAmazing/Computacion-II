import click
import const as cs
import subprocess
import socketserver
import signal, os

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()

        print("{} wrote:".format(self.client_address[0]))
        # print(self.data.decode)
        print(self.data.decode(cs.CHAR_CODE))

        p = subprocess.Popen([self.data], stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
        universal_newlines=True)
        out, err = p.communicate()
        ndata = str(out)
        out_data = (ndata).encode('ascii')
        # send back the output of the command
        self.request.sendall(out_data)

class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

@click.command()
# @click.option('--command', prompt='Enter command',
#             help=(cs.CMD_INFO_HELP))
@click.option('--concurrency', prompt='Type of Concurrency', 
            help=(cs.TYPE_CONC_HELP))

def execute(concurrency):
    
    HOST, PORT = "localhost", 9999
    socketserver.TCPServer.allow_reuse_address = True

    click.echo(concurrency)

    if concurrency == 't':
        # Create the server, binding to localhost on port 9999
        with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C

            server.serve_forever()
    elif concurrency == 'p':
        # Create the server, binding to localhost on port 9999
        with ForkedTCPServer((HOST, PORT), MyTCPHandler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C

            server.serve_forever()
    else:
        print(cs.ARGS_ERR_2)

if __name__ == '__main__':
    execute()