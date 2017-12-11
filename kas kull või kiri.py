from random import randint
 
print("Kas kull (1) või kiri (2)?")
kasutaja_valik = int(input())
suvaline_arv = randint(1, 2)
 
if kasutaja_valik == suvaline_arv:
    print("Arvasid õigesti.")
else:
    print("Arvasid valesti.")