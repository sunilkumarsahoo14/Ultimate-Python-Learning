# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint  # techniques to directly import randint from random

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo
        

    def bookTicket(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def noOfStatus(self):
        print(f"Train no: {self.trainNo} is running on time.")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

objTrain = Train(12399)
objTrain.bookTicket("Rampur", "Anugul")
objTrain.noOfStatus()
objTrain.getFare("Rampur", "Anugul")