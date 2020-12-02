#!/usr/bin/env python3

import socket
import sys

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


password = sys.argv[1]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        print(f'Connected by {addr}, received data: {data.decode()}')
        if not data:
            break
        elif password == data.decode():
            conn.sendall(b'Connection success!')
            break
        conn.send(data)
