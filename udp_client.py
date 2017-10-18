#!/usr/bin/python3
# -*- coding: utf-8 -*-
#sorce page: http://deutschina.hatenablog.com/entry/2016/02/22/013000
""" This is UDP clietnt."""
import getch

def send_commmand(address, port, command):
    import socket
    server_address = (address, port)
    max_size = 1024

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client.sendto(command, server_address)
    data, server = client.recvfrom(max_size)
    print("At", server, "said", data)
    client.close()

command0 = b'''
print("see you")
break;
'''

command1 = b'''
print("ON")
'''

command2 = b'''
print("OFF")
'''
while True:
    key = ord(getch.getch())
    print(str(key))
    if key == 119:
        #w
        send_commmand('localhost', 6789, command1)
        print("w")
        #continue

    elif key == 32:
        #space key
        send_commmand('localhost', 6789, command2)
        print("space")
        #continue

    elif key == 113:
        #q
        send_commmand('localhost', 6789, command0)
        print("q")
        break

    else:
        continue

