import click
import const as cs
import subprocess
import socketserver
import signal, os

@click.command()
@click.option('--command', prompt='Enter command',
            help='The command to execute.')
# @click.option('--count', prompt='Count', type=int, help='Number of greetings.')

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()

        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())
        print("PID: %d" % os.getpid())
        signal.pause()

class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def execute(command):
    p = subprocess.Popen(command)
    click.echo(p)

if __name__ == '__main__':
    execute()