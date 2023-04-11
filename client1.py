# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 19:29:07 2023

@author: kurra
"""
import socket

# IP address and port of server
SERVER_IP = '192.168.1.100'
SERVER_PORT = 5000

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

while True:
    # send a message to the server
    message = input('Enter message: ')
    sock.sendall(message.encode())

    # receive a message from the server
    data = sock.recv(1024)
    if not data:
        break
    print('Received:', data.decode())

# close the connection
sock.close()


