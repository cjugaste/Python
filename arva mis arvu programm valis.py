from random import randint
 
arv = randint(1,19) # juhuslik täisarv
print("Mõtlen ühele 20-st väiksemale naturaalarvule. Arva ära!")
arvamus = int(input())
 
while arvamus != arv:
    if arv > arvamus:
        print("Minu arv on suurem!")
    else:
        print("Minu arv on väiksem!")
 
    print("Arva veel!")
    arvamus = int(input())
 
print("Õige! Tubli!")