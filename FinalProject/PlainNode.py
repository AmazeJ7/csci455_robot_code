from FinalProject.PassableNode import PassableNode
from FinalProject.PhoneAPI import PhoneAPI

class PlainNode(PassableNode):

    def landOn(self, player):
        PhoneAPI.validDirection()
