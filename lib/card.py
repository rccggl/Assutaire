#
# Card class
#

class Card():

    # constructor
    def __init__(self, value, seed):
        self.seed = seed
        self.value = value

        self.validSeeds = ['denari','spade','bastoni','coppe']
        self.validValues = ['asso','due','tre','quattro','cinque','sei','sette','fante','cavallo','re']



    #
    def isValidSeed(self,seed) -> bool:
        if seed in self.validSeeds:
            return True
        else:
            return False



    #
    def isValidValue(self,value) -> bool:
        if value in self.validValues:
            return True
        else:
            return False



    # define the card
    def getName(self) -> str:
        return "%s di %s" % self.value, self.seed


    # protected
    def validateCard(self) -> bool:
        if self.seed in self.validSeeds:
            if self.value in self.validValues:
                return True
            else:
                return False
        else:
            return False

