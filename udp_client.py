#!/usr/bin/python3
# -*- coding: utf-8 -*-
#sorce page: http://deutschina.hatenablog.com/entry/2016/02/22/013000
""" This is UDP clietnt."""

def send_commmand(address, port, command):
    import socket
    server_address = (address, port)
    max_size = 1024

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client.sendto(command, server_address)
    data, server = client.recvfrom(max_size)
    print("At", server, "said", data)
    client.close()

command1 = b'''
print("LED ON")
print("LED OFF")
'''
send_commmand('localhost', 6789, command1)