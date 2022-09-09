import pickle
import click
import const as cs
import subprocess
import concurrent.futures
import socket
import os

def service_client(s2, addr):
    print ("Worker ",os.getpid()," atendiendo a ",addr)
    while True:
        sent = s2.recv(1024).strip()
        print (sent.decode())
        data_cmd = sent.decode()
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
            s2.sendall(serialization)
        elif out == '':
            err_data = (err).encode(cs.CHAR_CODE)
            check_msg = (cs.SV_ERR_CHECK).encode(cs.CHAR_CODE)
            # send back the output of the command
            list_data = [check_msg, err_data] 
            serialization = pickle.dumps(list_data)
            s2.sendall(serialization)

@click.command()
@click.option('-p', '--port', prompt='Enter port', type=int, help=(cs.PORT_INFO_HELP))
@click.option('-c', '--concurrency', prompt='Type of Concurrency', help=(cs.TYPE_CONC_HELP))

def execute(port, concurrency):
    if concurrency == 'p':
        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
                s.bind(("127.0.0.1", port))
                s.listen(1)
                while True:
                    s2, addr = s.accept()
                    result = executor.submit(service_client, s2, addr)
    elif concurrency == 't':
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
                s.bind(("127.0.0.1", port))
                s.listen(1)
                while True:
                    s2, addr = s.accept()
                    result = executor.submit(service_client, s2, addr)
    else:
        print(cs.ARGS_ERR_2)


if __name__ == '__main__':
    execute()