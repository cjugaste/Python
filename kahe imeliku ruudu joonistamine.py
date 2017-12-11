from turtle import *
 
def ruut():                # Defineerime funktsiooni nimega ruut
    i = 0
    while (i < 4):
        forward(100)
        left(90)
        i = i + 1
 
ruut()                     # Kutsume funktsiooni ruut välja. Kilpkonn joonistab ruudu küljega 100 pikslit
right(45)                  # Pöörame paremale 45°
ruut()                     # Kutsume uuesti funktsiooni ruut välja
 
exitonclick()