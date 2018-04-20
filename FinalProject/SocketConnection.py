import sys
sys.path.append('/home/pi/Desktop')

import os
import socket
import threading
from FinalProject.FromPhone import FromPhone
from FinalProject.ToPhone import ToPhone
from FinalProject.GameManager import GameManager
from tkinter import *

port = 7777

# Socket setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
temp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
temp_s.connect(('10.255.255.255', 1))
host = temp_s.getsockname()
temp_s.close()
print(str(host[0]))
s.bind((str(host[0]), port))
s.listen(5)


# Function to initiate the socket
def init_socket():
    while True:
        global s_2
        print('Listening')
        s_2, ip = s.accept()
        ToPhone.s_2 = s_2
        print('Got a connection from %s' % str(ip))
        gm.runGame()
        rt = threading.Thread(target=receive(s_2))
        rt.start()



# Function to receive STT commands
def receive(s_2):
    while True:
        global actions, actions_inv
        r = s_2.recv(1024)
        msg = r.decode('ascii')
        print('Received: ' + msg)
        msg_parts = msg.split()
        # msg_parts[1] should be the direction chosen by the user
        FromPhone.chooseNewDirection(msg_parts[0]);

gm = GameManager()

root = Tk()
root.title('Maze Game')
canvas = Canvas(root, bg='#1F1F1F', width='750', height='443')
# Socket thread init
init_socket_thread = threading.Thread(target=init_socket)
init_socket_thread.start()

root.geometry('800x450')
root.mainloop()
os.system('xset r on')
