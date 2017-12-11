print("Sisesta PIN-kood:")
sisestatud_pin = input()
kontoseis = 100
if sisestatud_pin == "1234":
    print("Sisenesid pangaautomaati! Pangakontol on " + str(kontoseis) + " eurot.")
    print("Sisesta, mitu eurot soovid välja võtta:")

else:
    print("Vale parool! Enesehävitusrežiim aktiveeritud: 3 ... 2 ... 1 ....")

soovitud_raha = int(input())
if soovitud_raha <= kontoseis:
    kontoseis = kontoseis - soovitud_raha
    print("Välja võetud: " + str(soovitud_raha) + " eurot.")
    print("Pangakontol on nüüd: " + str(kontoseis) + " eurot.")
    print("Ärge unustage raha masinast ära võtta!")
else:
    print("Kontol ei ole nii palju raha!")
