from Maestro import Controller
from tkinter import *
import time
import os
import socket
import threading



class Mover:

    def __init__(self):
        # Maestro instantiation
        self.controller = Controller()
        for chan in range(len(self.controller.Targets)):
            self.controller.setTarget(chan, 6000)
            self.controller.setAccel(0, 10)
            self.controller.setAccel(1, 10)
            self.controller.setAccel(2, 30)
            self.controller.setAccel(3, 20)
            self.controller.setAccel(3, 20)
        os.system('xset r off')


    def move(self, prevOrientation, newOrientation):
        if(prevOrientation == newOrientation):
            self.controller.setTarget(1, 4000)
            time.sleep(1)
            self.controller.setTarget(1, 6000)


        elif(self.getAxis(prevOrientation) != self.getAxis(prevOrientation)):
            # TODO turn 180 and move forward
            pass

        else:
            leftRight = self.getLeftRight(prevOrientation,newOrientation)
            if (leftRight == "left"):
                # TODO turn 90 left and move forward
                pass
            else:
                # TODO turn 90 right and move forward
                pass



    # get axis of a direction
    def getAxis(self, direction):
        if (direction == "north" or direction == "south"):
            return "ns"
        else:
            return "ew"

    # should robot turn right or left?
    def getLeftRight(self, prevDirection, nextDirection):
        directions = {"north" : 0,"east" : 1,"south" : 2,"west" : 3}
        if(prevDirection != "north"):
            if(prevDirection > nextDirection):
                return "left"
        # prevDirection == "north"
        else:
            if (nextDirection == "east"):
                return "right"
            else:
                return "left"

        if(prevDirection != "west"):
            if (prevDirection < nextDirection):
                return "right"
        # prevDirection == "west"
        else:
            if (nextDirection == "north"):
                return "right"
            else:
                return "left"
















