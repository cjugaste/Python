# -- PROGRAMMI 1. OSA - FUNKTSIOON TUTVUSTUS() --
 
def tutvustus():
    print("Inglise-eesti sõnastik (" + str(len(inglise_sõnad)) + " sõna)")
    print("'v' - välju")
    print("'a' - abi")
 
 
# -- PROGRAMMI 2. OSA - FAILI SISSELUGEMINE --
 
f = open('sonastik.txt', encoding='UTF-8')
 
inglise_sõnad = []
eesti_sõnad = []
rida = f.readline()
 
while rida != '':
    sõnad = rida.split('\t')
    inglise_sõna = sõnad[0].strip().lower()
    eesti_sõna = sõnad[1].strip().lower()
 
    inglise_sõnad.append(inglise_sõna)
    eesti_sõnad.append(eesti_sõna)
 
    rida = f.readline()
 
f.close()
 
 
# -- PROGRAMMI 3. OSA - FUNKTSIOONI RAKENDAMINE JA OTSIMINE --
 
tutvustus()
 
while True:
    otsing = input('Sisesta otsitav ingliskeelne sõna: ')
 
    otsing = otsing.lower()
 
    if otsing == 'v':
        break
    elif otsing == 'a':
        tutvustus()
    elif otsing in inglise_sõnad:
        print('Inglise keeles: ' + otsing)
        otsitava_sõna_indeks = inglise_sõnad.index(otsing)
        print('Eesti keeles: ' + eesti_sõnad[otsitava_sõna_indeks])
    else:
        print('Sellist sõna pole!')
        