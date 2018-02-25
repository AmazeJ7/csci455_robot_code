import Maestro
from tkinter import *
import os

# x = Maestro.Controller()
#
# for chan in range(len(x.Targets)):
#      x.setTarget(chan, 6000)
#
# x.setAccel(0, 10)
# x.setAccel(1, 10)
# x.setAccel(2, 30)
# x.setRange(3, 3200, 7800)
# x.setAccel(3, 20)
# x.setAccel(3, 20)
#
# os.system('xset r off')
#
# global forwardSpeed
# global backSpeed
# global headPos
# global headTilt
# forwardSpeed = 5250
# backSpeed = 6750
# headPos = 6000
# headTilt = 6000
#
# def forward(event):
#     x.setTarget(1, forwardSpeed)
#
# def back(event):
#     x.setTarget(1, backSpeed)
#
# def forwardBackOff(event):
#     x.setTarget(1, 6000)
#
# def left(event):
#     x.setTarget(2, 7000)
#
# def right(event):
#     x.setTarget(2, 5000)
#
# def leftRightOff(event):
#     x.setTarget(2, 6000)
#
# def stop(event):
#     for i in range(len(x.Targets)):
#         x.setTarget(i, 6000)
#
# def setSpeed(event):
#     global forwardSpeed
#     global backSpeed
#     if (event.char == 'i'):
#         forwardSpeed = 5250
#         backSpeed = 6750
#         print("speed set to low")
#     if (event.char == 'o'):
#         forwardSpeed = 5000
#         backSpeed = 7000
#         print("speed set to med")
#     if (event.char == 'p'):
#         forwardSpeed = 4750
#         backSpeed = 7250
#         print("speed set to high")
#
# def setWaist(event):
#     if (event.char == 'a'):
#         x.setTarget(0, 4250)
#     if (event.char == 's'):
#         x.setTarget(0, 6000)
#     if (event.char == 'd'):
#         x.setTarget(0, 7750)
#
# def setHead(event):
#     global headPos
#     if (event.char == 'q'):
#         headPos = headPos - 1000
#     if (event.char == 'w'):
#         headPos = 6000
#     if (event.char == 'e'):
#         headPos = headPos + 1000
#     x.setTarget(3, headPos)
#
# def setHeadTilt(event):
#     global headTilt
#     if (event.char == 'z'):
#         headTilt = headTilt - 1000
#     if (event.char == 'x'):
#         headTilt = 6000
#     if (event.char == 'c'):
#         headTilt = headTilt + 1000
#     x.setTarget(4, headTilt)
#
# root.bind('<Up>', forward)
# root.bind('<KeyRelease-Up>', forwardBackOff)
#
# root.bind('<space>', stop)
#
# root.bind('<Down>', back)
# root.bind('<KeyRelease-Down>', forwardBackOff)
#
# root.bind('<Left>', left)
# root.bind('<KeyRelease-Left>', leftRightOff)
#
# root.bind('<Right>', right)
# root.bind('<KeyRelease-Right>', leftRightOff)
#
# root.bind('<i>', setSpeed)
# root.bind('<o>', setSpeed)
# root.bind('<p>', setSpeed)
#
# root.bind('<a>', setWaist)
# root.bind('<s>', setWaist)
# root.bind('<d>', setWaist)
#
# root.bind('<q>', setHead)
# root.bind('<w>', setHead)
# root.bind('<e>', setHead)
#
# root.bind('<z>', setHeadTilt)
# root.bind('<x>', setHeadTilt)
# root.bind('<c>', setHeadTilt)
#
# os.system('xset r on')

xpos = 0
ypos = 0
actionCount = 0
actions = ['','','','','','','','']
pictureSize = 100

root = Tk()

htPhoto = PhotoImage(file="icons\HeadTilt.png")
htPhoto = htPhoto.subsample(2,2)
hrPhoto = PhotoImage(file="icons\HeadRotate.png")
hrPhoto = hrPhoto.subsample(2,2)
runPhoto = PhotoImage(file="icons\Move.png")
runPhoto = runPhoto.subsample(2,2)
turnPhoto = PhotoImage(file="icons\Rotate.png")
turnPhoto = turnPhoto.subsample(2,2)
brPhoto = PhotoImage(file="icons\BodyRotate.png")
brPhoto = brPhoto.subsample(2,2)

def go():
    print('go!')

def ht():
    global xpos, ypos, actionCount, actions
    myCan.create_image(50+xpos, 50, image=htPhoto)
    xpos += 105
    actions[actionCount] = icon('ht')
    actionCount += 1

def hr():
    global xpos, ypos, actionCount, actions
    myCan.create_image(50+xpos, 50, image=hrPhoto)
    xpos += 105
    actions[actionCount] = icon('hr')
    actionCount += 1

def run():
    global xpos, ypos, actionCount, actions
    myCan.create_image(50+xpos, 50, image=runPhoto)
    xpos += 105
    actions[actionCount] = icon('run')
    actionCount += 1

def turn():
    global xpos, ypos, actionCount, actions
    myCan.create_image(50+xpos, 50, image=turnPhoto)
    xpos += 105
    actions[actionCount] = icon('turn')
    actionCount += 1

def br():
    global xpos, actionCount, actions
    myCan.create_image(50+xpos, 50, image=brPhoto)
    xpos += 105
    actions[actionCount] = icon('br')
    actionCount += 1

class icon:
    def __init__(self, name):
        self.name = name
        self.time = 2

    def openSettings(self):
        settingsTK = Tk()
        w = Scale(settingsTK, from_=0, to=10)
        w.pack()
        w2 = Scale(settingsTK, from_=0, to=5)
        w2.pack()
        print(w.get())
        settingsTK.mainloop()

class mouseMovement:
    def __init__(self):
        self.flag = False

    def mousePressed(self, event):
        global actionCount, actions
        for x in range(0, 8):
            if (x*105+100) > event.x > (x*105) and 0 < event.y < 100 and actionCount > x:
                self.flag = True
                print(actions[x])
                actions[x].openSettings()

    def mouseRelease(self, event):
        if self.flag == True:
            self.flag = False

m = mouseMovement()

myCan = Canvas(root, bg="#a9a9a9", width="830", height="100")
myCan.pack(side=RIGHT)
myCan.bind('<ButtonPress-1>', m.mousePressed)
myCan.bind('<ButtonRelease-1>', m.mouseRelease)

ht = Button(root, command=ht)
ht.config(image=htPhoto, width = pictureSize, height = pictureSize)
ht.pack(side=TOP)

hr = Button(root, command=hr)
hr.config(image=hrPhoto, width = pictureSize, height = pictureSize)
hr.pack(side=TOP)

run = Button(root, command=run)
run.config(image=runPhoto, width = pictureSize, height = pictureSize)
run.pack(side=TOP)

turn = Button(root, command=turn)
turn.config(image=turnPhoto, width = pictureSize, height = pictureSize)
turn.pack(side=TOP)

br = Button(root, command=br)
br.config(image=brPhoto, width = pictureSize, height = pictureSize)
br.pack(side=TOP)

go = Button(root, width = 13, text = 'GO!', bg = 'black', fg = 'white', command=go)
go.pack(side=TOP)

root.mainloop()
