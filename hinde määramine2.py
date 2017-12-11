print("Sisesta punktide arv")
punktid = int(input())
 
if punktid > 90:
    print("Hinne A")
elif punktid > 80:
    print("Hinne B")
else:
    print("Hinne ei ole A ega B")