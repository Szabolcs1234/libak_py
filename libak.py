# LIBÁK

# A róka libát lop a faluból. A libák súlyát – pontosabban tömegét – listában adjuk meg. A farkas a dűlőútnál várja a rókát, és a három kilónál nagyobb libákat elveszi – a piciket nagylel�kűen otthagyja a rókának.
# libak = [1,5,2,3,4]


# b. Átlagosan hány kilósak a rókának maradt libák?
# c1. Előfordult-e olyan, hogy a róka legalább háromkilós libát lopott?
# c2. Előfordult-e olyan, hogy a róka kisebb libát hozott, mint az előző napon?
# d. Hányadik napon sikerült a rókának először legalább háromkilós libát lopnia?
# e. Melyik a róka első legalább háromkilós libája?
# f. Hány libát tarthat meg a róka?
# g. Mekkora a legkisebb liba, amit a farkas elvesz a rókától?

def beolvasas():
    l=[]
    with open("libak.txt", "r", encoding="UTF-8") as fm:
        for sor in fm:
            l.append(int(sor.strip()))
    return l
    
def osszegzes(l):
    osszeg=0
    for elem in l:
        if elem<=3:
            osszeg+=elem
    return osszeg 


def kiir(l,r_kg):
    print(f"A libák súlyai{l}")
    print(f"Átlagosan {r_kg} kiló libát ehet meg a róka")   
#Főprogram
#Input
libak=beolvasas()

#számolás
# a. Hány kiló libát ehet meg a róka?
r_megehet_ossz_kg=osszegzes(libak)
#output
kiir(libak, r_megehet_ossz_kg)
"""
def kereses(l):
    van = False
    sorszam=-1
    i=0
    while i<len(l) and not l[i]<=3:
        i+=1
    if i<len(l):
        van = True
        sorszam=i
    else:
        van = False
    return sorszam
"""