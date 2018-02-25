#IrisMariaRohelpuu  #EliisaRaal #CassandraJugaste

#from turtle import Turtle, Screen

#FONT = ("Arial", 50)

#esileht = Turtle()
#esileht.write("IGAVLEJA ABIMEES", align="center", font=FONT)
#esileht.hideturtle()

#screen = Screen()
#screen.bgpic("movies.gif")
#screen.exitonclick()

import random

#kasutajasisestus
print("Tere! Oleme siin, et leida Teile õhtuks meelepärane tegevus.")
tegevus = input("Kas sooviksite teha midagi aktiivset või passiivset? ")

#definitsioon
def failist_järjendisse(retsept):
    f = open(retsept, encoding = "UTF-8-SIG")

    koostisosad = []
    for rida in f:
        koostisosad.append(rida)

    return koostisosad

#tingimus
if tegevus == "aktiivset":
    aktiivne_teg = input("Selge! Palun valige järgmiseks valdkond: küpsetamine, sport või sotsialiseerumine? ")
    if aktiivne_teg == "küpsetamine":
        retsept = input("Magus valik ;) palun vali, millist retsepti soovid küpsetada: brownie, kirju koer, küpsisetort või napoleoni kook? ")

        if retsept == "brownie":
            f = open("brownie.txt", encoding = "UTF-8-SIG")
            print("Brownie küpsetamiseks on vaja: " + ", ".join(l.strip() for l in f.readlines()))
        elif retsept == "kirju koer":
            f = open("kirjukoer.txt", encoding = "UTF-8-SIG")
            print("Kirju koera küpsetamiseks on vaja: " + ", ".join(l.strip() for l in f.readlines()))
        elif retsept == "küpsisetort":                            
            f = open("küpsisetort.txt", encoding = "UTF-8-SIG")
            print("Küpsisetordi küpsetamiseks on vaja: " + ", ".join(l.strip() for l in f.readlines()))
        elif retsept == "napoleoni kook":
            f = open("napoleon.txt", encoding = "UTF-8-SIG")
            print("Napoleoni koogi küpsetamiseks on vaja: " + ", ".join(l.strip() for l in f.readlines()))
        else:
            print("Vale sisestus.")
    elif aktiivne_teg == "sport":
        print("Tervislik valik! Meil on Sulle välja pakkuda järgnevad soovitused: jooksmine, uisutamine, tantsimine, võrkpall, jalgpall, suusatamine, tennis ja batuudil hüppamine.")
    elif aktiivne_teg == "sotsialiseerumine":
        print("Vahva! Soovitame sõbraga välja sööma ja/või kinno minemist, pidu, shoppamist, mõnele üritusele vabatahtlikuks või hoopis 3D kogudusse minemist!")
    else:
        print("Vale sisestus.")
    

                
else:
    passiivne_teg = input("Selge! Palun valige järgmiseks valdkond: filmi vaatamine, lugemine või mängimine? ")
    if passiivne_teg == "lugemine":
        muutuja = int(input("Mitme raamatu vahel soovite valida? "))
        žanr = input("Hea valik! Palun valige žanr: science fiction, young adult, fiction, romance või classics? ")
        if žanr == "science fiction":
            f = open("science fiction.txt", encoding = "UTF-8-SIG")
        elif žanr == "young adult":
            f = open("young adult.txt", encoding = "UTF-8-SIG")
        elif žanr == "fiction":
            f = open("fiction.txt", encoding = "UTF-8-SIG")
        elif žanr == "romance":
            f = open("romanceB.txt", encoding = "UTF-8-SIG")
        elif žanr == "classics":
            f = open("classics.txt", encoding = "UTF-8-SIG")
        else:
            print("Vale sisestus.")
        def valib(mitu): #Luuakse funktsioon
            järjend1 = [] #Luuakse tühi järjend
            valik1 = []   #Luuakse tühi järjend
            for rida in f: #Hakatakse vastavast tekstifailist andmeid lugema
                järjend1.append(rida.strip()) #Lisatakse failis olevad read järjendisse
            while mitu > 0: #Järgmised 5 rida võtavad nendest nii palju suvalisi filminimesid kui kasutaja sisestas
                suvaline = random.randint(0, mitu)
                valik1.append(järjend1[suvaline])
                järjend1.remove(järjend1[suvaline])
                mitu -= 1
            return valik1 #Tagastatakse filmide nimed
        if muutuja < 1:
            print("Sisestage nullist suurem arv.") #Kui kasutaja sisestab 1-st väiksema arvu palutakse sisestada nullist suurem arv
        elif muutuja > 9:
            print("Sisestage arv üheksa piires.") #Kui kasutaja sisestab 9-st suurema arvu palutakse sisestada arv üheksa piires
        else:
            print("Raamatusoovitus(ed): ")
            for i in valib(muutuja): #Kui kasutaja sisestatud arv on 1-9 piires prinditakse talle tema filmisoovitused
                print(i)
        f.close()
        
    if passiivne_teg == "mängimine":
        print("Vahva, aitame sul leida selle õige! Soovitame: The Sims 4, Minecraft, Transformice, GTA, CS:GO, League of Legends, Fortnite, Overwatch ja Tomb Raider.")
    elif passiivne_teg == "filmi vaatamine":
        muutuja2 = int(input("Mis olekski mõnusam, kui üks hea film!  Mitut filmi soovite vaadata? ")) 
        filmižanr = input("Sisestage filmi kategooria (action, horror, comedy, thriller, romance): ")
        if filmižanr == "action":
            f = open("action.txt", encoding = "UTF-8-SIG")
        elif filmižanr == "horror":
            f = open("horror.txt", encoding = "UTF-8-SIG")
        elif filmižanr == "comedy":                            #Kõik read if-i ja elif-iga avavad vastava tekstifaili
            f = open("comedy.txt", encoding = "UTF-8-SIG")
        elif filmižanr == "thriller":
            f = open("thriller.txt", encoding = "UTF-8-SIG")
        elif filmižanr == "romance":
            f = open("romance.txt", encoding = "UTF-8-SIG")
        else:
            print("Vale sisestus.")
        def valib(mitu): #Luuakse funktsioon
            järjend = [] #Luuakse tühi järjend
            valik = []   #Luuakse tühi järjend
            for rida in f: #Hakatakse vastavast tekstifailist andmeid lugema
                järjend.append(rida.strip()) #Lisatakse failis olevad read järjendisse
            while mitu > 0: #Järgmised 5 rida võtavad nendest nii palju suvalisi filminimesid kui kasutaja sisestas
                suvaline = random.randint(0, mitu)
                valik.append(järjend[suvaline])
                järjend.remove(järjend[suvaline])
                mitu -= 1
            return valik #Tagastatakse filmide nimed
        if muutuja2 < 1:
            print("Sisestage nullist suurem arv.") #Kui kasutaja sisestab 1-st väiksema arvu palutakse sisestada nullist suurem arv
        elif muutuja2 > 9:
            print("Sisestage arv üheksa piires.") #Kui kasutaja sisestab 9-st suurema arvu palutakse sisestada arv üheksa piires
        else:
            print("Filmisoovitus(ed): ")
            for i2 in valib(muutuja2): #Kui kasutaja sisestatud arv on 1-9 piires prinditakse talle tema filmisoovitused
                print(i2)
        f.close()
