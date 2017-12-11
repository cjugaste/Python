#Cassandra Jugaste 10IT

november = int(input("Mitu õpilast läheb vaatama filmi November? "))
kosmos = int(input("Mitu õpilast läheb vaatama filmi Kosmos meie vahel? "))
osalejad = november + kosmos
raha = 6.9 * osalejad

print("Piletite jaoks läheb raha: " + str(raha) + " eurot.")
print("Kino külastavaid õpilasi kokku: " + str(osalejad) + " õpilast.")
