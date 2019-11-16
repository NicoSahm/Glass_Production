from time import *
import sensors

class furnace:
    def __init__(self):
        #max intake in kg
        self.__max_intake = 30
        #current_intake in kg
        self.__current_intake = 0
        #duration time in sec
        self.__duration = 420
        #heat duration for furnace
        self.__heat_duration = 600
        #the max temperature of the furnace
        self.__max_temp = 2571
        #the max production amount of glasses in one process
        self.__max_glasses = 300
        #tempreature probe
        self.__temperature_probe = sensors.temperature_probe("TempProbe", 0)
        #gas burner
        self.__gas_burner = sensors.gas_burner("GasBurner", True)
        self.__molten = False

    def get_max_intake(self):
        return self.__max_intake

    def get_duration(self):
        return self.__duration

    def get_max_glasses(self):
        return self.__max_glasses

    def heat(self):
        if self.__gas_burner.Status == True:
            helper = 0
            while helper != self.__heat_duration:
                self.__temperature_probe.Temp = 4.585
                print("Current temp: " + str(self.__temperature_probe.Temp))
                helper += 1
                sleep(1)

    def fill(self, amount):
        if (self.__current_intake + amount) <= self.__max_intake:
            self.__current_intake += amount
        else:
            print("Error: Max intake of furnace reached")

    def melt(self):
        if self.__temperature_probe.Temp == self.__max_temp and self.__current_intake == self.__max_intake:
            count = 0
            while count < self.__duration:
                count += 1
                sleep(1)
            self.__molten = True
        return self.__molten

    def bottling(self):
        self.__current_intake -= 100