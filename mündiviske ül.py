from random import randint
 
suvaline_arv = randint(1, 2)
if suvaline_arv == 1:
    arvuti_valik = "kull"
else:
    arvuti_valik = "kiri"
 
print("Mündiviskes võitis: " + arvuti_valik)