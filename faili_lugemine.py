f = open("andmed.txt")
 
nimi = f.readline()
vanus = f.readline()
aadress = f.readline()
 
print("Nimi:", nimi)
print("Vanus:", vanus)
print("Aadress:", aadress)
 
f.close()