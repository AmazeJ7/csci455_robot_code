from FinalProject.PhoneAPI import PhoneAPI

class Player:

    def __init__(self, x, y, startHealth, gameManager):
        self.x = x
        self.y = y
        self.health = startHealth
        self.gameManager = gameManager


    def startTurn(self):
        PhoneAPI.firstMove();


    # called upon input from android
    def resolveDirection(self, direction):
        newX = self.x
        newY = self.y

        if(direction == "right"):
            newX += 1
        elif (direction == "left"):
            newX -= 1
        elif (direction == "up"):
            newY -= 1
        elif (direction == "down"):
            newY += 1
        else:
            PhoneAPI.invalidDirection()
            return
        # if out of bounds
        print(newY, newX)

        if(newX > 4 or newX < 0 or newY > 4 or newY < 0 or self.gameManager.maze[newY][newX].passable == False):
            # TODO: pass error message to phone
            PhoneAPI.wrongDirection()

        else:
            self.x = newX
            self.y = newY
            # follow directions of node that we landed on
            self.gameManager.maze[newY][newX].landOn(self);







