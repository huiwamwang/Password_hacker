#!/usr/bin/env python3

import socket
import sys
import json

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


login = sys.argv[1]
password = sys.argv[2]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024).decode()
        data_dict = json.loads(data)
        print(f'Connected by {addr}, received data: {data_dict}')
        if not data:
            break
        elif login != data_dict['login']:
            send_dict = json.dumps({'result': 'Wrong login!'})
            conn.send(send_dict.encode())
        elif login == data_dict['login']:
            conn.sendall((json.dumps({'result': 'Wrong password!'})).encode())
            i = 0
            while i <= len(password):
                if password[i] == data_dict['password']:
                    conn.sendall((json.dumps({'result': 'Exception happened during login'})).encode())
                    i += 1
            if password == data_dict['password']:
                conn.sendall(b'Connection success!') 
                break
        
