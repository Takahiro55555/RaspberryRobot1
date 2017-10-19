#!/usr/bin/python3
# -*- coding: utf-8 -*-
#sorce page: http://deutschina.hatenablog.com/entry/2016/02/22/013000
""" This is UDP clietnt."""
#動作確認済み
import getch

"""
PIN1 = 11
PIN2 = 12
PIN3 = 15
PIN4 = 16
"""

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
GPIO.output(PIN1,False)
GPIO.output(PIN2,False)
GPIO.output(PIN3,False)
GPIO.output(PIN4,False)
GPIO.cleanup()
print("see you")
break
'''

command1 = b'''
GPIO.output(PIN1,False)
GPIO.output(PIN2,False)
GPIO.output(PIN3,False)
GPIO.output(PIN4,False)
print("Go straight")
GPIO.output(PIN1,False)
GPIO.output(PIN2,True)
GPIO.output(PIN3,False)
GPIO.output(PIN4,True)
'''

command2 = b'''
GPIO.output(PIN1,False)
GPIO.output(PIN2,False)
GPIO.output(PIN3,False)
GPIO.output(PIN4,False)
print("Back")
GPIO.output(PIN1,True)
GPIO.output(PIN2,False)
GPIO.output(PIN3,True)
GPIO.output(PIN4,False)
'''

command3 = b'''
GPIO.output(PIN1,False)
GPIO.output(PIN2,False)
GPIO.output(PIN3,False)
GPIO.output(PIN4,False)
print("Right")
GPIO.output(PIN1,False)
GPIO.output(PIN2,True)
GPIO.output(PIN3,True)
GPIO.output(PIN4,False)
'''

command4 = b'''
GPIO.output(PIN1,False)
GPIO.output(PIN2,False)
GPIO.output(PIN3,False)
GPIO.output(PIN4,False)
print("Left")
GPIO.output(PIN1,True)
GPIO.output(PIN2,False)
GPIO.output(PIN3,False)
GPIO.output(PIN4,True)
'''

command5 = b'''
GPIO.output(PIN1,False)
GPIO.output(PIN2,False)
GPIO.output(PIN3,False)
GPIO.output(PIN4,False)
print("STOP")
'''
while True:
    key = ord(getch.getch())
    print(str(key))
    if key == 119:
        #w
        send_commmand('192.168.11.20', 6789, command1)
        print("Go straight")

    elif key == 115:
        #s
        send_commmand('192.168.11.20', 6789, command2)
        print("Back")

    elif key == 100:
        #d
        send_commmand('192.168.11.20', 6789, command3)
        print("Right")

    elif key == 97:
        #a
        send_commmand('192.168.11.20', 6789, command4)
        print("Left")

    elif key == 32:
        #space key
        send_commmand('192.168.11.20', 6789, command5)
        print("STOP")

    elif key == 113:
        #q
        send_commmand('192.168.11.20', 6789, command5)
        send_commmand('192.168.11.20', 6789, command0)
        print("Finish")
        break;

    else:
        continue

