from turtle import *
from random import randint
 
värv = randint(1, 3)
if värv == 1:
    color("blue")                  # Sinine
if värv == 2:
    color("black")                 # Must
if värv == 3:
    color("white")                 # Valge valgel taustal
begin_fill()                       # Kilpkonn alustab ringi värvimist
circle(100)                        # Kilpkonn joonistab ringi raadiusega 100 pikslit
end_fill()                         # Kilpkonn lõpetab ringi värvimise
 
exitonclick()