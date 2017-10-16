#!/usr/bin/python3
# -*- coding: utf-8 -*-
#sorce page: http://deutschina.hatenablog.com/entry/2016/02/22/013000

import socket
from datetime import datetime

server_address = ('localhost', 6789)
max_size = 1024

print("Starting the server at", datetime.now())
print("Waiting for a client to call.")
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)

data, client = server.recvfrom(max_size)

exec(data)

#print("At", datetime.now(), client, "said", data)
server.sendto(b'Are you talking to me?', client)
server.close()