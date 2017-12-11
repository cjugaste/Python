#Cassandra Jugaste 10IT
maht = int(input("Mis on faili suurus (MB)? "))
andmed = int(input("Kui palju andmeid on plaadile kirjutatud (MB)? "))
kogumaht = 700
vaba = kogumaht - andmed - maht

if maht + andmed < kogumaht:
    print("Plaadil on vaba ruumi: " + str(vaba) + " MB.")
elif maht + andmed > kogumaht:
    print("Limiit on ületatud!")
elif maht + andmed == kogumaht:
    print("Fail mahub täpselt.")