from lib.cardFamily import CardFamily
from lib.deck import Deck
from lib.card import Card


def test_cardFamily():
    cf = CardFamily('napoletane')
    dk = Deck(cf)
    assert dk.cardFamily.family == 'napoletane'


def test_validateCard():
    cf = CardFamily('napoletane')
    dk = Deck(cf)
    cv = Card('asso', 'bastoni')
    assert dk.validateCard(cv) == True
    civ = Card('jack','cuori')
    assert dk.validateCard(civ) == False
