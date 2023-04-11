# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 19:28:40 2023

@author: kurra
"""

import socket

# IP address and port of server
#SERVER_IP = '192.168.1.100'
#SERVER_PORT = 5000

server_address = ('localhost', 10000)

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the server's IP address and port
#sock.bind((SERVER_IP, SERVER_PORT))
sock.bind(server_address)
# listen for incoming connections
sock.listen(2)

# accept two connections from clients
conn1, addr1 = sock.accept()
conn2, addr2 = sock.accept()

while True:
    # receive a message from client 1
    data1 = conn1.recv(1024)
    if not data1:
        break
    print('Received from client 1:', data1.decode())

    # forward the message to client 2
    conn2.sendall(data1)

    # receive a message from client 2
    data2 = conn2.recv(1024)
    if not data2:
        break
    print('Received from client 2:', data2.decode())

    # forward the message to client 1
    conn1.sendall(data2)

# close the connections
conn1.close()
conn2.close()
