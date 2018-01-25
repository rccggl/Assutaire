#
# The dock class
#
import random
from lib.card import Card
from lib.cardFamily import CardFamily


class Deck:
    """
    The deck is an ordered sequence of cards.
    First card (bottom card) has index 1, last card (top card) has index 40


    Attributes
    ----------


    Methods
    -------


    """

    def __init__(self, cardFamily):
        """
        Create the deck with all cards, then shuffle it.
        """
        # the card family object
        self.__cardFamily = cardFamily

        # the deck stack
        self.__deck = []

        # create the deck
        for s in cardFamily.seeds:
            for v in cardFamily.values:
                self.addCard(Card(v, s))

        # shuffle the deck
        self.shuffleDeck()


    @property
    def deck(self):
        return self.__deck


    @property
    def cardFamily(self):
        return self.__cardFamily



    def addCard(self, card):
        """
        Add a card in a position

        Parameters
        ----------
        card : object
            The card to add to deck

        Returns
        -------
        nothing

        """
        self.__deck.append(card)



    def shuffleDeck(self):
        """
        Shuffles the deck

        :return:
        """
        for iter in range(0, random.randrange(1, 20)):
            for pcard1 in range(0, random.randrange(1, 39)):
                for pcard2 in range(0, random.randrange(1, 39)):
                    self.swapCards(pcard1, pcard2)


    def validateCard(self, card) -> bool:
        """
        Validates a card

        :param card:
            The card object

        :return:
            Boolean
        """
        if card.seed in self.cardFamily.validSeeds:
            if card.value in self.cardFamily.validValues:
                return True
            else:
                return False
        else:
            return False



    def printDeck(self):
        """
        Prints out the cards in the deck

        :return:
        """
        for c in self.deck:
            print(c.name + " ", end='')


    def swapCards(self, pcard1, pcard2):
        """
        Swaps two cards at positions pcard1, pcard2

        :param pcard1: int, the list's index of the first card
        :param pcard2: int, the list's index of the second card
        :return: none
        """
        card1 = self.deck[pcard1]
        self.__deck[pcard1] = self.deck[pcard2]
        self.__deck[pcard2] = card1
