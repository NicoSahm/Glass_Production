class sensor:
    def __init__(self, name):
        self.__name = name

class temperature_probe(sensor):
    def __init__(self, name, temperature):
        super().__init__(name)
        self.__temp = temperature

    def get_temp(self):
        return self.__temp

    def set_temp(self, temp):
        self.__temp += temp

    Temp = property(get_temp, set_temp)

class gas_burner(sensor):
    def __init__(self, name, stat):
        super().__init__(name)
        self.__status = stat

    def get_status(self):
        return self.__status

    def set_status(self, stat):
        self.__status = stat

    Status = property(get_status, set_status)