#!/usr/bin/python3
# -*- coding: utf-8 -*-
#sorce page: http://deutschina.hatenablog.com/entry/2016/02/22/013000

import socket
from datetime import datetime

# RasPi
import RPi.GPIO as GPIO
PIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN,GPIO.OUT)
GPIO.output(PIN,False)

server_address = ('localhost', 6789)
max_size = 1024
print("Starting the server at", datetime.now())
print("Waiting for a client to call.")
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)

while True:
    data, client = server.recvfrom(max_size)
    
    exec(data)

    #print("At", datetime.now(), client, "said", data)
    server.sendto(b'Are you talking to me?', client)
server.close()

# RasPi
GPIO.output(PIN,False)
GPIO.cleanup()