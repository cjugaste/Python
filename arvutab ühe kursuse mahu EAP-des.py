#Cassandra Jugaste 10IT
ühe_perioodi_kursuste_arv = int(input("Sisestage ühe perioodi kursuste arv: "))
tundide_arv = (45*35)/(60*26)
EAP = round(ühe_perioodi_kursuste_arv * tundide_arv)
print("Maht EAPdes: " + str(EAP))