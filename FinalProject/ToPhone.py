from FinalProject.FromPhone import FromPhone
import time

class ToPhone:

    s_2 = None

    # TODO: change mock phone response into actual response on android end

    # RECIEVED messages from pi
    @staticmethod
    def firstMove():
        send_message1 = 'Please select a direction to move: north, south, east or west: \r\n'
        ToPhone.s_2.send(send_message1.encode('ascii'))
        print("Please select a direction to move: north, south, east or west: ")
        time.sleep(3)

        send_message = 'get speech\r\n'
        ToPhone.s_2.send(send_message.encode('ascii'))
        # code to simulate phone's response:
        #direction = input("Please select a direction to move: north, south, east or west: ")
        #FromPhone.chooseNewDirection(direction)  # to pi

    @staticmethod
    def wrongDirection():
        send_message1 = 'That way is blocked. Choose another way.\r\n'
        ToPhone.s_2.send(send_message1.encode('ascii'))
        print("That way is blocked. Choose another way." )

        time.sleep(2.5)
        send_message2 = 'get speech\r\n'
        ToPhone.s_2.send(send_message2.encode('ascii'))
        # code to simulate phone's response:
        #direction = input("Blocked! Which way? " )  # on phone
        #FromPhone.chooseNewDirection(direction)  # to pi

    @staticmethod
    def invalidDirection():
        send_message1 = 'Sorry, that is not a valid direction. Choose again:  \r\n'
        ToPhone.s_2.send(send_message1.encode('ascii'))
        print("Sorry, that's not a valid direction. Choose again: ")

        time.sleep(3)

        send_message = 'get speech\r\n'
        ToPhone.s_2.send(send_message.encode('ascii'))
        # code to simulate phone's response:
        #direction = input("Sorry, that's not a valid direction. Choose again: ")  # on phone
        #FromPhone.chooseNewDirection(direction)  # to pi

    @staticmethod
    def finish():
        send_message1 = 'Congratulations, you found the treasure! \r\n'
        ToPhone.s_2.send(send_message1.encode('ascii'))
        print("Congratulations, you found the treasure!")

        #send_message = 'get speech'
        #ToPhone.s_2.send(send_message.encode('ascii'))
        # code to simulate phone's response:

    @staticmethod
    def validDirection():
        send_message1 = 'Where to now? \r\n'
        ToPhone.s_2.send(send_message1.encode('ascii'))
        print("Where to now? ")
        time.sleep(1.5)

        send_message = 'get speech\r\n'
        ToPhone.s_2.send(send_message.encode('ascii'))
        # code to simulate phone's response:
        #direction = input("Now where to? ")
        #FromPhone.chooseNewDirection(direction) # to pi

