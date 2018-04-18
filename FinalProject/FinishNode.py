from FinalProject.PassableNode import PassableNode
from FinalProject.ToPhone import ToPhone

class FinishNode(PassableNode):

    def landOn(self, player):
        ToPhone.finish()