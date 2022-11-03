import asyncio
import time
import click
import subprocess
import const as cs
import pickle
import os

async def handle_function(reader, writer):
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
async def main(port):
    server = await asyncio.start_server(
        handle_function, '127.0.0.1', port)

    addr = server.sockets[0].getsockname()
    #print(f'Serving on {addr} {asyncio.current_task()}')

    async with server:
        print(f"Tareas:\n{asyncio.all_tasks()}")
        await server.serve_forever()

asyncio.run(main())
