''''''
'''hozz létre egy osztályzatok listát és
osztalyzatok_lista=[3,4,5,2,3,4,5,4]
nevek=["Béla", "Jenő", "Ági", "Rozi", ]
nevek és a nevekhez tartozó osztályzatok összetartoznak
etelek=["húsleves","krumplis"]
ar=[1234,3456]
új adatszerkezet - ami egybe tudja kezelni az összetartozó adatokat
szemely={név: "Béla", osztalyzat:3}
kaja1={nev:"húsleves", ar:1234, elk_ido:2}
kaja2={nev:"krumplis", ar:2345, elk_ido:0.5}
objektumok - tulajdonságokkal (főnevek) és viselkedéssel 
(cselekvés) bíró adatszerkezet
Készítsünk egy sablont, ami alapján le tudjuk gyártani
a konkrét egyedeket.
OSZTÁLY - sablon - osztály - tervrajz
OBJEKTUM - konkrét egyedek - obijektum - konkrét termék
'''
'''
from Etel import Etel
import fuggvenyek
"""2. lépés: Létrehozzuk a konkrét példányt a tervrajz alapján"""
etel1=Etel("húsleves",1234)
etel2=Etel("krumplis",2345)
etel3=Etel("rántott hús", 2145)
etel4=Etel("palacsinta", 1450)
etel_lista=[]
etel_lista.append(etel1)
etel_lista.append(etel2)
etel_lista.append(etel3)
etel_lista.append(etel4)
print("Szia, én vagyok a "+ etel1.nev+" Az állapotom "+ etel1.allapot)
etel1.keszul()
print("Szia, én vagyok a "+ etel1.nev+" Az állapotom "+ etel1.allapot)
print("Szia, én vagyok a "+ etel2.nev+" Az állapotom "+ etel2.allapot)

fuggvenyek.etlap(etel_lista)

atlag_ar=fuggvenyek.atlag_ar(etel_lista)
print(f"Az ételek átlagára: {atlag_ar}")

maxi=fuggvenyek.legdragabb(etel_lista)
print(f"A legdrágább étel neve és ára {etel_lista[maxi]}, {etel_lista[maxi]}")

'''
""" hoz létre egy Alkalmazott osztályt, amelyikben az alábbi onfókat tudod tárolni egy cég dolgozóiról:
nev
szul_datum
fizetes
pozicio
kor

Készíts kor metódust, ami megmondja az adott ember korát
__str__

Hozz létre legalább 5 embert, tedd bele őket listába
-mennyi az össz fizetés?
-hány éves a legidősebb ember?
-hány ember van "beosztott" pozícióba?
-kinek a legalacsonyabb a fizetése?

++az osztálynak legyen egy fizetésemelés metódusa, 
amelyik a fizetést megemeli a paraméterében megadott százalék értékkel.
A legkisebb fizetésű ember fizetését emeld meg 20%al!"""

from Szolga import Szolga
import fuggvenyek

szolga1=Szolga("Admirális Andor",1969,269696,"Igazgató")
szolga2=Szolga("Brúnó Béla",1974,269666,"Igazgató helyettes")
szolga3=Szolga("Garantált Géza",1969,269656,"Műszakvezető")
szolga4=Szolga("Info Irén",1969,169696,"IT Vezető")
szolga5=Szolga("Magas Márton",2004,100000,"Csóró Diák")
szolga_lista=[]
szolga_lista.append(szolga1)
szolga_lista.append(szolga2)
szolga_lista.append(szolga3)
szolga_lista.append(szolga4)
szolga_lista.append(szolga5)

ossz_fiz=fuggvenyek.ossz_fizu(szolga_lista)
print(f"Az emberek összfizetése: {ossz_fiz}")
