from random import *
import termcolor
def drawCard(num):
    cards = []
    colours = ["yellow","blue","green","red"]
    for x in range(num):
        cards.append([colours[randint(0,3)],randint(0,9)])
    return cards

class Player:
    def __init__(self,given_name):
        self.name = given_name
        self.deck = drawCard(7)
    def status(self):
        for x in self.deck:
            termcolor.cprint(x[1],x[0],end=" , ")


player1 = Player("Nikhil")
player1.status()