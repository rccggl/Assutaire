#
# Name:     Assutaire
# Version:  0.1
#
# MIT License
#

import yaml
from lib.cardFamily import CardFamily
from lib.deck import Deck
from lib.card import Card
from lib.game import Game



def main():
    # main tasks goes here

    print("Welcome to Assutaire! A solitaire for CPU!\n")

    # load configration
    with open("conf/config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    # setup card family based on configuration
    cf = CardFamily(cfg['cardFamily']['default'])

    # setup a deck
    dk = Deck(cf)

    print("This is the deck we have shuffled ...\n")
    dk.printDeck()

    # setup table

    # play until the stack is void
    # permutation 1 / 2 / 3
    # result




if __name__ == '__main__':
    main()
