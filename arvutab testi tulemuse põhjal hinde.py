#Cassandra Jugaste 10IT
kokku_punkte = int(input("Mitu punkti oli töö max?"))
punktid = int(input("Mitu punkti sa said?"))
valem = (punktid / kokku_punkte) * 100
if valem >= 90:
    print("Hinne on 5.")
elif valem >= 75:
    print("Hinne on 4.")
elif valem >= 50:
    print("Hinne on 3")
elif valem >= 30:
    print("Hinne on 2.")
elif valem >= 0:
    print("Hinne on 1.")