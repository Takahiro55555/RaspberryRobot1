#!/usr/bin/python3
# -*- coding: utf-8 -*-
#sorce page: http://deutschina.hatenablog.com/entry/2016/02/22/013000
#動作確認済み

import socket
from datetime import datetime

# RasPi
import RPi.GPIO as GPIO

PIN1 = 11
PIN2 = 12
PIN3 = 15
PIN4 = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN1,GPIO.OUT)
GPIO.setup(PIN2,GPIO.OUT)
GPIO.setup(PIN3,GPIO.OUT)
GPIO.setup(PIN4,GPIO.OUT)
GPIO.output(PIN1,False)
GPIO.output(PIN2,False)
GPIO.output(PIN3,False)
GPIO.output(PIN4,False)

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
    server.sendto(b'I receved your command.', client)
server.close()

# RasPi
GPIO.output(PIN1,False)
GPIO.output(PIN2,False)
GPIO.output(PIN3,False)
GPIO.output(PIN4,False)
GPIO.cleanup()