class FromPhone:

    player = None # gets assigned in GameManager

    # messages SENT BACK to pi

    @staticmethod
    def chooseNewDirection(direction):
        FromPhone.player.resolveDirection(direction)  # from phone