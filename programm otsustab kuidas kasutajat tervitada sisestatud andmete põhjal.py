#IrisMariaRohelpuu, CassandraJugaste, GregoryLandrat

nimi = input("Palun sisestage oma nimi: ")
perekonnaseis = input("Palun sisestage oma perekonnaseis(vallaline või abielus): ")
sugu = input("Palun sisestage oma sugu: ")
vanus = int(input("Palun sisestage oma vanus: "))

if perekonnaseis == 'abielus' and sugu == 'naine':
    print("Tere proua, " + nimi + "!" )
elif perekonnaseis == 'abielus' and sugu == 'mees':
    print("Tere härra, " + nimi + "!")
if vanus <= 30 and sugu == 'mees' and perekonnaseis == 'vallaline':
    print("Tere noormees!")
elif vanus <= 30 and sugu == 'naine' and perekonnaseis == 'vallaline':
    print("Tere preili!")
if vanus >= 30 and sugu == 'mees' and perekonnaseis == 'vallaline':
    print("Tere härrasmees!")
elif vanus >= 30 and sugu == 'naine' and perekonnaseis == 'vallaline':
    print("Tere, " + nimi + "!")