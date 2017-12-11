#Cassandra Jugaste 10IT
from random import randint
tekst = int(input("Mitu korda tahad täringut visata?"))
x = 0                    #algab nullist
while x <= tekst - 1:    #-1 sest x algab nullist, kui miinust ei pane ja algab nullist siis tuleb 1 vise rohkem
    vise = randint(1,6)
    print(vise)
    x += 1
    
    