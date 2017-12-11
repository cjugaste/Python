import re

tekst = input("Sisesta postiindeks: ")
arv = "[1-9][0-9]{4}$"

if re.match(arv, tekst):
    print("On Eesti postiindeks")
else:
    print("Ei ole Eesti postiindeks")