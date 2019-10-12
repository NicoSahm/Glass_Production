import time

class silos(object):
    
    #Methods for: calculating current time, getting the weight of the silos and saving them, fill the silos, open vault (startTime, totalTime)

    sandSiloCurrentLevel = None
    ncSiloCurrentLevel = None
    limeSiloCurrentLevel = None

    sandSiloMaxLevel = 2000
    ncSiloMaxLevel = 500
    limeSiloMaxLevel = 500

    def getRemainingFillingTime(self, providedSiloName):
        siloMaxLevel = silos.siloMaxLevelSelector(self, providedSiloName)
        siloName = silos.siloSelector(self, providedSiloName)
        diff = siloMaxLevel - siloName
        fullFillupTimeMin = 20
        fullFillupTimeSec = fullFillupTimeMin * 60
        fillupPerSec = fullFillupTimeSec / siloMaxLevel
        predictedFillupTime = diff * fillupPerSec
        return round(predictedFillupTime, 3)

    def siloMaxLevelSelector(self, siloName):
        if(siloName == silos.sandSiloCurrentLevel):
            return silos.sandSiloMaxLevel
        elif(siloname == silos.ncSiloCurrentLevel):
            return silos.ncSiloMaxLevel
        else:
            return silos.limeSiloMaxLevel

    def siloSelector(self, siloName):
        if(siloName == silos.sandSiloCurrentLevel):
            return silos.sandSiloCurrentLevel
        elif(siloname == silos.ncSiloCurrentLevel):
            return silos.ncSiloCurrentLevel
        else:
            return silos.limeSiloCurrentLevel

    def fillSilos(self, providedSiloName):
        siloMaxLevel = silos.siloMaxLevelSelector(self, providedSiloName)
        siloCurrentLevel = silos.siloSelector(self, providedSiloName)
        while(True):
            print(siloCurrentLevel)
            if(siloCurrentLevel >= siloMaxLevel-0.5):
                print("Break")
                break
            else:
                siloCurrentLevel += 0.6
                time.sleep(1)

# Method to open the vaults(Total Weight, Starttime)            


x = silos()

print(x.getRemainingFillingTime(x.sandSiloCurrentLevel))
