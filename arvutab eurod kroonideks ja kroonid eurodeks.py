#Cassandra Jugaste 10IT
raha = int(input("Sisestage rahasumma:"))
kurss = input("Palun sisestage kurss, milleks soovite teisendada (EUR/EEK):")
euro = raha / 15.6466
kroon = raha * 15.6466
if kurss == "EUR":
    print("Summa on %0.2f eurot." % (euro))  #print("Summa on" + str(euro) + ".") vastuses liiga palju komakohti
elif kurss == "EEK":                         #%0.2f jätab paljude komakohtadega arvule ainult 2 komakohta
    print("Summa on %0.2f krooni." % (kroon))
else:
    print("Vale sisestus.")