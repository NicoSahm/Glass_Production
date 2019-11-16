import time

class production_road:
    def __init__(self):
        self.__speed = 1
        self.__duration = 40
        self.__amount = 0
        self.__glasses = 0


    def produce(self):
        start = 0
        while(start < self.__duration):
            time.sleep(1)

    def set_amount(self, amount):
        self.__amount += amount

    def calc_glasses(self):
        self.__glasses = self.__amount / 100

    def bottling(self):
        return self.__glasses
