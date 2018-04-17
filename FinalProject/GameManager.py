from FinalProject.BlockedNode import BlockedNode
from FinalProject.PlainNode import PlainNode
from FinalProject.FinishNode import FinishNode
from FinalProject.Player import Player
from FinalProject.PhoneAPI import PhoneAPI


class GameManager:

    def __init__(self):
        # initialize 5 x 5 array of nodes
        self.maze = [[None for x in range(5)] for y in range(5)]

        # create test maze
        self.maze[0][0] = PlainNode()
        self.maze[0][1] = PlainNode()
        self.maze[0][2] = FinishNode()

        self.maze[0][3] = BlockedNode()
        self.maze[1][0] = BlockedNode()
        self.maze[1][1] = BlockedNode()
        self.maze[1][2] = BlockedNode()

        # create player at location 0,0 with health of 100
        self.player = Player(0,0,100, self)
        PhoneAPI.player = self.player


    def runGame(self):
        self.player.startTurn()



gm = GameManager()
gm.runGame()



