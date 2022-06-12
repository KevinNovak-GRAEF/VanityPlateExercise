# The License Plate Vanity Class
# Checks criteria for a vanity plate

from cmath import log
from unicodedata import name


class VanityPlate:
    
    # The __init__ method accepts an argument
    
    def __init__(self,plate,logo,collector):
        self.__plate = plate
        self.__logo = logo
        self.__collector = collector

    def set_plate(self,plate):
        self.__plate = plate

    def get_plate(self):
        return self.__plate
    
    def set_logo(self,logo):
        self.__logo = logo
    
    def get_logo(self):
        return self.__logo
    
    def set_collector(self,collector):
        self.__collector = collector
    
    def get_collector(self):
        return self.__collector

    def StartCriteria(self):
        start = self.get_plate()
        return (start[:2].isalpha())

    def PlateLength(self):
        length = self.get_plate()
        if len(length) >= 2 and len(length) <=6:
            return True
        else:
            return False
    
    def PlateMiddle(self):
        middle = self.get_plate()
        if not middle.isalpha():
            return middle[0].isalpha() and middle[-1].isdigit()
        else:
            return True
    
    def PlateDigitStart(self):
        digit = self.get_plate()
        try:
            mid_num = digit.index("0")
            if digit[mid_num-1].isdigit():
                return True
            else:
                return False
        except ValueError:
            return True
    
    def PlatePunctuation(self):
        punctuation = self.get_plate()
        return punctuation.isalnum()