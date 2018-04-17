from FinalProject.PassableNode import PassableNode
from FinalProject.PhoneAPI import PhoneAPI

class FinishNode(PassableNode):

    def landOn(self, player):
        PhoneAPI.finish()