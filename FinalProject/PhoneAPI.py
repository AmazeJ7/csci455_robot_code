class PhoneAPI:

    player = None # gets assigned in GameManager

    # TODO: change mock code into sending messeges back and forth with robot

    # RECIEVED messages from pi
    @staticmethod
    def firstMove():
        direction = input("Hello, which way would you like me to go? ")
        PhoneAPI.chooseNewDirection(direction)  # to pi

    @staticmethod
    def wrongDirection():
        direction = input("Blocked! Which way? " )  # on phone
        PhoneAPI.chooseNewDirection(direction)  # to pi

    @staticmethod
    def invalidDirection():
        direction = input("Sorry, that's not a valid direction. Choose again: ")  # on phone
        PhoneAPI.chooseNewDirection(direction)  # to pi

    @staticmethod
    def finish():
        print("Congratulations, you found the treasure!")

    @staticmethod
    def validDirection():
        direction = input("Now where to? ")
        PhoneAPI.chooseNewDirection(direction) # to pi


    # messages SENT BACK to pi

    @staticmethod
    def chooseNewDirection(direction):
        PhoneAPI.player.resolveDirection(direction)  # from phone