# Can you change the slf-parameter inside a class to something else (say“harry”). Try changing slf to “slf” or “harry” and see the effects


# ----> It don't affect the code and it's workings 

from random import randint  # techniques to directly import randint from random

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo
        

    def bookTicket(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")

    def noOfStatus(slf):
        print(f"Train no: {slf.trainNo} is running on time.")

    def getFare(slf, fro, to):
        print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is {randint(222, 5555)}")

objTrain = Train(12399)
objTrain.bookTicket("Rampur", "Anugul")
objTrain.noOfStatus()
objTrain.getFare("Rampur", "Anugul")