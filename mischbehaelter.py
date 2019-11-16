# Sensoren
# mischbehaelter_wage

# Mischverhältnis: 30:7:2
# Ventil1 = 23.0769 kg
# Ventil2 = 5.3846 kg
# Ventil2 = 1.5385 kg

class mische:   
  def createMische():
    amount1 = 23.0769
    amount2 = 5.3846
    amount3 = 1.5385

    if (silo1Weight >= amount1 && silo2Weight >= amount2 && silo3Weight >= amount3 )
        # 1. Ventil 1 öffnen bis ca. max23kg auf der Wage sind.
        print("Open Ventil 1")
        silo1Weight =   silo1.getWeight()

        while wage.weight <= amount1
            ventil1.open
        
        print("Close Ventil 1")
        ventil1.close

        # 2. Ventil 2 öffnen bis 5,4kg zusätzlich hinzugefügt wurden.
        print("Open Ventil 2")
        while wage.weight <= (amount2 + amount1)
            ventil2.open
        
        print("Close Ventil 2")
        ventil2.close

        # 3. 30sek alles Mischen. (sleep und print-Ausgabe)
        print("Mixing for 30 seconds.")
        mixer.start
        sleep (30000)
        mixer.stop

        # 4. Ventil 3 öffnen und warten bis 1,5 zusätzlich auf der Wagen.
        print("Open Ventil 3")
        while wage.weight <= (1.5385 + 5.3846 + 23.0769)
            ventil3.open
        
        print("Close Ventil 3")
        ventil3.close

        # 5. 60sek alles mischen. (sleep und print-Ausgabe)
        print("Mixing for 60 seconds.")
        mixer.start
        sleep (60000)
        mixer.stop

        # 6. Ausgangsventil öffnen und Scheiße raushauen.
        print("current weight: " + wage.weight)
        print("Go away shit.")
        while wage.weight > 0
            ventil4.open

        ventil4.close    
        print("current weight: " + wage.weight)

        return ("Sucess")

    else
        return ("Fatal ERROR")