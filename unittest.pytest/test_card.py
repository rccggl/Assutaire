from lib.card import Card


def test_isSeedValid():
    # test
    c = Card('bastoni','asso')
    assert c.isValidSeed('bastoni') == True
    assert c.isValidSeed('invalid') == False


def test_getName():
    # test
    c = Card('asso','bastoni')
    assert c.getName() == 'asso di bastoni'


def test_validateCard():
    cv = Card('asso', 'bastoni')
    assert cv.validateCard() == True
    civ = Card('jack','cuori')
    assert civ.validateCard() == False


