import Maestro
from tkinter import *
import os

x = Maestro.Controller()

for chan in range(len(x.Targets)):
    x.setTarget(chan, 6000)

x.setAccel(0, 10)
x.setAccel(1, 10)
x.setAccel(2, 30)
x.setRange(3, 3200, 7800)
x.setAccel(3, 20)
x.setAccel(3, 20)

os.system('xset r off')

root = Tk()
global forwardSpeed
global backSpeed
global headPos
global headTilt
forwardSpeed = 5250
backSpeed = 6750
headPos = 6000
headTilt = 6000


def forward(event):
    x.setTarget(1, forwardSpeed)


def back(event):
    x.setTarget(1, backSpeed)


def forwardBackOff(event):
    x.setTarget(1, 6000)


def left(event):
    x.setTarget(2, 7000)


def right(event):
    x.setTarget(2, 5000)


def leftRightOff(event):
    x.setTarget(2, 6000)


def stop(event):
    for i in range(len(x.Targets)):
        x.setTarget(i, 6000)


def setSpeed(event):
    global forwardSpeed
    global backSpeed
    if (event.char == 'i'):
        forwardSpeed = 5250
        backSpeed = 6750
        print("speed set to low")
    if (event.char == 'o'):
        forwardSpeed = 5000
        backSpeed = 7000
        print("speed set to med")
    if (event.char == 'p'):
        forwardSpeed = 4750
        backSpeed = 7250
        print("speed set to high")


def setWaist(event):
    if (event.char == 'a'):
        x.setTarget(0, 4250)
    if (event.char == 's'):
        x.setTarget(0, 6000)
    if (event.char == 'd'):
        x.setTarget(0, 7750)


def setHead(event):
    global headPos
    if (event.char == 'q'):
        headPos = headPos - 1000
    if (event.char == 'w'):
        headPos = 6000
    if (event.char == 'e'):
        headPos = headPos + 1000
    x.setTarget(3, headPos)


def setHeadTilt(event):
    global headTilt
    if (event.char == 'z'):
        headTilt = headTilt - 1000
    if (event.char == 'x'):
        headTilt = 6000
    if (event.char == 'c'):
        headTilt = headTilt + 1000
    x.setTarget(4, headTilt)


root.bind('<Up>', forward)
root.bind('<KeyRelease-Up>', forwardBackOff)

root.bind('<space>', stop)

root.bind('<Down>', back)
root.bind('<KeyRelease-Down>', forwardBackOff)

root.bind('<Left>', left)
root.bind('<KeyRelease-Left>', leftRightOff)

root.bind('<Right>', right)
root.bind('<KeyRelease-Right>', leftRightOff)

root.bind('<i>', setSpeed)
root.bind('<o>', setSpeed)
root.bind('<p>', setSpeed)

root.bind('<a>', setWaist)
root.bind('<s>', setWaist)
root.bind('<d>', setWaist)

root.bind('<q>', setHead)
root.bind('<w>', setHead)
root.bind('<e>', setHead)

root.bind('<z>', setHeadTilt)
root.bind('<x>', setHeadTilt)
root.bind('<c>', setHeadTilt)

root.mainloop()

os.system('xset r on')
