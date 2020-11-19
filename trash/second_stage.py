from string import ascii_lowercase, digits
import socket
from sys import argv
import itertools

password_letters = ascii_lowercase + digits
password_length = len(password_letters)
hostname, port = argv[1:]
address = (hostname, int(port))
with socket.socket() as my_socket:
    my_socket.connect(address)
    for i in range(1, password_length):
        for password in itertools.product(password_letters, repeat=i):
            password = ''.join(password)
            print(password)
            my_socket.send(password.encode())
            server_response = my_socket.recv(1024)
            print(f'server response: {server_response.decode()}')
            if server_response == b'Connection success!':
                print(password)
                exit()
