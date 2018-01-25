#
# Table class
#

class Table():

    # setup a table for the game
    def __init__(self, deck):
        self.__deck = deck
        self.__layed = []

        self.setup()



    @property
    def deck(self):
        return self.__deck



    def setup(self):
        nc = 5
        for card in self.deck:





