from FinalProject.PassableNode import PassableNode
from FinalProject.ToPhone import ToPhone

class PlainNode(PassableNode):

    def landOn(self, player):
        ToPhone.validDirection()
