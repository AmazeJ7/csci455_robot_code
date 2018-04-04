from MockMaestro import Controller
import os
import socket
import threading

# Maestro instantiation
controller = Controller()
for chan in range(len(controller.Targets)):
    controller.setTarget(chan, 6000)
controller.setAccel(0, 10)
controller.setAccel(1, 10)
controller.setAccel(2, 30)
controller.setAccel(3, 20)
controller.setAccel(3, 20)
os.system('xset r off')

# Global Variables
actions = []
port = 9999
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
temp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
temp_s.connect(('10.255.255.255', 1))
host = temp_s.getsockname()[0]
temp_s.close
print(host)

# bind to the port
s.bind((host, port))
s.listen(5)


while True:
    print('Hi')
    s_2, ip = s.accept()
    print("Got a connection from %s" % str(ip))
    msg = 'Thank you for connecting\r\n'
    s_2.send(msg.encode('ascii'))


os.system('xset r on')
