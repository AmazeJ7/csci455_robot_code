from FinalProject.ToPhone import ToPhone
from FinalProject.MovementController import Mover

class Player:

    def __init__(self, x, y, startHealth, gameManager):
        self.x = x
        self.y = y
        self.health = startHealth
        self.gameManager = gameManager
        self.mover = Mover()
        self.orientation = "east"


    def startTurn(self):
        ToPhone.firstMove();


    # called upon input from android
    def resolveDirection(self, direction):
        newX = self.x
        newY = self.y
        newOrientation = ""

        if(direction == "west"):
            newX += 1
            newOrientation = "west"
        elif (direction == "east"):
            newX -= 1
            newOrientation = "east"
        elif (direction == "north"):
            newY -= 1
            newOrientation = "north"

        elif (direction == "south"):
            newY += 1
            newOrientation = "south"

        else:
            ToPhone.invalidDirection()
            return
        # if out of bounds
        print(newY, newX)

        if(newX > 4 or newX < 0 or newY > 4 or newY < 0 or self.gameManager.maze[newY][newX].passable == False):
            ToPhone.wrongDirection()

        else:
            self.x = newX
            self.y = newY
            self.orientation = newOrientation
            self.mover.move(self.orientation, newOrientation)
            self.orientation = newOrientation
            # follow directions of node that we landed on
            self.gameManager.maze[newY][newX].landOn(self);


