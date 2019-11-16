import time

class silos(object):
    
    #Methods for: calculating current time, getting the weight of the silos and saving them, fill the silos, open vault (startTime, totalTime)

    #Silo1 = Sand
    #Silo2
    #Silo3

    sandSiloCurrentLevel = 2000
    ncSiloCurrentLevel = 500
    limeSiloCurrentLevel = 500

    sandSiloMaxLevel = 2000
    ncSiloMaxLevel = 500
    limeSiloMaxLevel = 500

    sand_name = "Sand"
    nc_name = "NC"
    lime_name = "Kalk"

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

    def setSiloLevel(self, siloName, amount):
        if(siloName == silos.sandSiloCurrentLevel):
            silos.sandSiloCurrentLevel = amount
        elif(siloname == silos.ncSiloCurrentLevel):
            silos.ncSiloCurrentLevel = amount
        else:
            silos.limeSiloCurrentLevel = amount
        

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
                silos.setSiloLevel(self, providedSiloName, siloCurrentLevel)
                time.sleep(1)

    def fillMixer(self, providedSiloName, amount):
        siloCurrentLevel = silos.siloSelector(self, providedSiloName)
        if(siloCurrentLevel < amount):
            print("Error. Not enough material")
        else:
            siloCurrentLevel -= amount
            silos.setSiloLevel(self, providedSiloName, siloCurrentLevel)
            return amount
# Method to open the vaults(Total Weight, Starttime)            

x = silos()

#print(x.getRemainingFillingTime(x.sandSiloCurrentLevel))
print(x.fillSilos(x.sandSiloCurrentLevel))
print(x.sandSiloCurrentLevel)
filling = x.fillMixer(x.sandSiloCurrentLevel, 400)
print(filling)
print(x.sandSiloCurrentLevel)