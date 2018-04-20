


from FinalProject.BlockedNode import BlockedNode
from FinalProject.PlainNode import PlainNode
from FinalProject.FinishNode import FinishNode
from FinalProject.Player import Player
from FinalProject.FromPhone import FromPhone
from FinalProject import MovementController



class GameManager:

    def __init__(self):
        # initialize 5 x 5 array of nodes
        self.maze = [[None for x in range(5)] for y in range(5)]
        # fill in maze with nodes
        self.createMaze()
        # create player at location 0,0 with health of 100
        self.player = Player(0,0,100, self)
        # set player on FromPhone class, so that it can call player methods upon receiving messages
        FromPhone.player = self.player


    # start player's first turn
    def runGame(self):
        self.player.startTurn()

    # fill in maze with nodes (currently test maze)
    def createMaze(self):
        self.maze[0][0] = PlainNode()
        self.maze[0][1] = PlainNode()
        self.maze[0][2] = FinishNode()

        self.maze[0][3] = BlockedNode()
        self.maze[1][0] = BlockedNode()
        self.maze[1][1] = BlockedNode()
        self.maze[1][2] = BlockedNode()







