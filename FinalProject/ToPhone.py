from FinalProject.FromPhone import FromPhone

class ToPhone:

    s_2 = None

    # TODO: change mock phone response into actual response on android end

    # RECIEVED messages from pi
    @staticmethod
    def firstMove():
        send_message = 'firstMove'
        ToPhone.s_2.send(send_message.encode('ascii'))
        # code to simulate phone's response:
        direction = input("Please select a direction to move: north, south, east or west: ")
        FromPhone.chooseNewDirection(direction)  # to pi

    @staticmethod
    def wrongDirection():
        send_message = 'wrongDir'
        ToPhone.s_2.send(send_message.encode('ascii'))
        # code to simulate phone's response:
        direction = input("Blocked! Which way? " )  # on phone
        FromPhone.chooseNewDirection(direction)  # to pi

    @staticmethod
    def invalidDirection():
        send_message = 'invalidDir'
        ToPhone.s_2.send(send_message.encode('ascii'))
        # code to simulate phone's response:
        direction = input("Sorry, that's not a valid direction. Choose again: ")  # on phone
        FromPhone.chooseNewDirection(direction)  # to pi

    @staticmethod
    def finish():
        send_message = 'finish'
        ToPhone.s_2.send(send_message.encode('ascii'))
        # code to simulate phone's response:
        print("Congratulations, you found the treasure!")

    @staticmethod
    def validDirection():
        send_message = 'validDir'
        ToPhone.s_2.send(send_message.encode('ascii'))
        # code to simulate phone's response:
        direction = input("Now where to? ")
        FromPhone.chooseNewDirection(direction) # to pi

