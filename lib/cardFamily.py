#
# card type
#

class CardFamily:

    def __init__(self,family):
        self.__validFamilies = ['napoletane','siciliane']

        if self.isFamilyValid:
            self.__family = family
            self.setValidSeedsForFamily(family)
            self.setValidValuesForFamily(family)
        else:
            raise ValueError("Invalid Card's family!!!", family)


    @property
    def family(self):
        return self.__family

    @property
    def seeds(self):
        return self.__seeds

    @property
    def values(self):
        return self.__values

    @property
    def numOfSeeds(self):
        return len(self.__seeds)

    @property
    def numOfValues(self):
        return len(self.__values)

    @property
    def validFamilies(self):
        return self.__validFamilies

    @property
    def validSeeds(self):
        return self.__seeds

    @property
    def validValues(self):
        return self.__values


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

    #
    def isFamilyValid(self,family):
        if family in self.validFamilies:
            return True
        else:
            return False

    #
    def setValidSeedsForFamily(self,family):
        if family == 'napoletane':
            self.__seeds = ['D', 'S', 'B', 'C']
        elif family == 'siciliane':
            self.__seeds = ['D', 'S', 'B', 'C']
        else:
            raise ValueError("SSH: unsupported family!!")

    #
    def setValidValuesForFamily(self, family):
        if family == 'napoletane':
            self.__values = ['1', '2', '3', '4', '5', '6', '7', 'F', 'C', 'R']
        elif family == 'siciliane':
            self.__values = ['1', '2', '3', '4', '5', '6', '7', 'F', 'C', 'R']
        else:
            raise ValueError("SSH: unsupported family!!")

