'''1. lépés: osztály létrehozása'''
class Etel: #mindig nagybetűvel kezdjük
    def __init__(self,nev:str="",ar:int=1000,elk_ido:float=1):
        """ konstruktor feladata, hogy létrehozza a konkrét
        példányt a konkrét adatokat a tervrajzból
        beállítsa az adattagokat - obijektum
        tulajdonságok értékei
        """

        self.nev=nev
        self.ar=ar
        self.elk_ido=elk_ido
        self.allapot="folyamatban"

    def keszul(self):
        self.allapot ="kész"