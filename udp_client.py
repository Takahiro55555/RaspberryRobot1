#!/usr/bin/python3
# -*- coding: utf-8 -*-
#sorce page: http://deutschina.hatenablog.com/entry/2016/02/22/013000
""" This is UDP clietnt."""

import socket
from datetime import datetime

server_address = ('localhost',6789)
max_size = 1024

print("Starting the client at", datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'Hey!', server_address)
data, server = client.recvfrom(max_size)
print("At", datetime.now(), server, "said", data)
client.close()