class silos(object):
    

    def fillSilos(self, currentState, siloMaxLevel):
        diff = siloMaxLevel - currentState
        fullFillupTimeMin = 20
        fullFillupTimeSec = fullFillupTimeMin * 60
        fillupPerSec = fullFillupTimeSec / siloMaxLevel
        predictedFillupTime = diff * fillupPerSec
        return predictedFillupTime


x = silos()

print(x.fillSilos(100,2000))
# 1900 fehlen
# 1200 sek Gesamtdauer
# 0,6 pro Sekunde
# 1140 Sekunden dauert die Befüllung
