"""
Krustiņi un nullītes.
"""

import random

laukums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


"""
TODO: Drukā grafisku spēles laukumu (kā paraugā) no figūrām, kas glabājas sarakstā.
Ja elements ir skaitlis, tad to izlaiž. Citādi izdrukā X vai 0.
Katru simbolu pozicionē kvadrātiekavās.

Paraugs:
[X][ ][0]
[ ][X][0]
[ ][ ][X]
"""
def ziimeeLaukumu():
    pass


"""
TODO: Aicina spēlētāju izdarīt gājienu, ievadot skaitli intervālā 1 - 9.
TODO: Atkarībā no ievadītā skaitļa, ieraksta X vai 0 attiecīgajā pozīcijā sarakstā.
Funkcijas parametrs speletajs satur simbolu X vai 0 atkarībā, kurš no spēlētājiem izdara gājienu.
Izdrukā pašreizējo spēles laukumu un pārbauda, vai nav fiksēta uzvara/neizšķirts.
Ja spēle nav galā, tā turpinās ar nākamo gājienu.
"""
def gajiens(speletajs):
    global laukums

    # ... sastādi gājiena izdarīšanas algoritmu ...

    ziimeeLaukumu()

    iznakums = parbaudaUzvaru()
    if iznakums != False:
        spelesBeigas(iznakums)
    else:
        if speletajs == "X":
            gajiens("0")
        else:
            gajiens("X")


"""
Attīra laukumu no esošajām figūrām, sanumurē laukus.
Spēle turpinās ar pirmo gājienu.
"""
def jaunaSpele(speletajs):
    global laukums
    skaititajs = 1
    for i in range(len(laukums)):
        for j in range(len(laukums[i])):
            laukums[i][j] = skaititajs
            skaititajs += 1

    gajiens(speletajs)


"""
TODO: Cikliski caurskata sarakstu un pārbauda, vai eksistē uzvaroša kombinācija vai neizšķirts.
TODO: Ja eksistē uzvaroša kombinācija, atgriež uzvarētāja simbolu (X vai 0).
TODO: Ja konstatēts neizšķirts, atgriež "neizšķirts".
TODO: Citādi atgriež False.
"""
def parbaudaUzvaru():
    pass


"""
Izvada jautājumu par jaunas spēles sākumu. 
Ja atbild apstiprinoši, izsauc f-ju jaunaSpele(), padodot kā parametru uzvarētāju, kurš sāks spēli.
"""
def spelesBeigas(uzvaretajs):
    izvele = input("Vai vēlies spēlēt vēlreiz? (y/n")
    if izvele == "y":
        if uzvaretajs == "X":
            jaunaSpele("X")
        elif uzvaretajs == "0":
            jaunaSpele("0")
        else:
            jaunaSpele(random.choice(["X", "0"]))


# Spēli sāk X
jaunaSpele("X")
