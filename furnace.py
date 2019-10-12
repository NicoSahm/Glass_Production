from time import *
class furnace:
    def __init__(self):
        #max intake in kg
        self.__max_intake = 30
        #duration time in sec
        self.__duration = 420
        #heat duration for furnace
        self.__heat_duration = 600
        #the current temperature of the furnace
        self.__current_temp = 0
        #the max temperature of the furnace
        self.__max_temp = 2571
        #the max production amount of glasses in one process
        self.__max_glasses = 300

    def get_max_intake(self):
        return self.__max_intake

    def get_duration(self):
        return self.__duration

    def get_max_glasses(self):
        return self.__max_glasses

    def get_current_temp(self):
        return self.__current_temp

    def heat(self):
        helper = 0
        while helper != self.__heat_duration:
            self.__current_temp += 4.585
            print("Current temp: " + str(self.__current_temp))
            helper += 1
            sleep(1)


