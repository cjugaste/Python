#Cassandra Jugaste&Iris Maria Rohelpuu 10IT
kujund = input("Millist kujundit soovid? (ruut, ring, ristkülik) ")
värv = input("Sisestage värv inglise keeles: ")

from turtle import*
if kujund == "ruut":
    laius = int(input("Sisestage kujundi laius: "))
    pikkus = int(input("Sisestage kujundi pikkus: "))
    color(värv)
    begin_fill()
    fd(laius)
    lt(90)
    fd(pikkus)
    lt(90)
    fd(laius)
    lt(90)
    fd(pikkus)
    end_fill()
elif kujund == "ristkülik":
    laius = int(input("Sisestage kujundi laius: "))
    pikkus = int(input("Sisestage kujundi pikkus: "))
    color(värv)
    begin_fill()
    fd(laius)
    lt(90)
    fd(pikkus)
    lt(90)
    fd(laius)
    lt(90)
    fd(pikkus)
    end_fill()
elif kujund == "kolmnurk":
    color(värv)
    begin_fill()
    fd(laius)
    lt(120)
    fd(pikkus)
    lt(120)
    fd(pikkus)
    end_fill()
elif kujund == "ring":
    raadius = int(input("Sisestage ringi raadius: "))
    color(värv)
    begin_fill()
    circle(raadius)
    end_fill()
else:
    print("Vale sisestus.")
    
    



