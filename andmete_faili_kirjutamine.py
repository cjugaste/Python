nimi = input("Palun sisesta oma nimi: ")
vanus = input("vanus: ")
aadress = input("aadress: ")
 
f = open("andmed.txt", "w")
f.write(nimi + "\n")
f.write(vanus + "\n")
f.write(aadress + "\n")
f.close()