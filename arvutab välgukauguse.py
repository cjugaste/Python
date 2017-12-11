def välgu_kaugus(ajavahemik):
    valem = round(ajavahemik * 330 / 1000)
    return valem

ajavahemik = float(input("Mitu sekundit kulus välgu nägemisest müristamise kuulmiseni?"))
kaugus = välgu_kaugus(ajavahemik)
print("Välgulöögi kaugus kilomeetrites: " + str(int(kaugus)))