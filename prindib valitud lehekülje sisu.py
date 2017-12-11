from urllib.request import urlopen
 
vastus = urlopen("http://startit.ee/karjaar/")
 
baidid = vastus.read()
# veebist lugemisel annab käsk read() meile tavalise sõne asemel hunniku baite,
# mis on vaja veel sõneks "dekodeerida"
tekst = baidid.decode()
vastus.close()
 
print(tekst)
