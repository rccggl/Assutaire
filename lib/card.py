#
# Card class
#

class Card():

    # constructor
    def __init__(self, value, seed):
        self.__seed = seed
        self.__value = value


    def __str__(self) -> str:
        """
        Print myself

        :return:
        """
        return ' -- \n|{}{}|\n -- '.format(self.value, self.seed)


    @property
    def name(self) -> str:
        """
        Print myself in form of 3B

        :return:
        """
        return '{}{}'.format(self.value, self.seed)


    @property
    def seed(self):
        if isinstance(self.__seed, str):
            return self.__seed
        else:
            return "invalid seed"


    @property
    def value(self):
        return self.__value





