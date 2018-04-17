from FinalProject.Node import Node
from abc import abstractmethod

class PassableNode(Node):

    def __init__(self):
        self.passable = True;

    @abstractmethod
    def landOn(self, player):
        pass