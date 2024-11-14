from datetime import datetime

class Szolga:
    def __init__(self, nev:str="", szul_datum:int=1960, fizetes:int=200000, pozicio:str="",kor:int=20):
        
        self.nev=nev
        self.szul_datum=szul_datum
        self.fizetes=fizetes
        self.pozicio=pozicio
        self.kor=self.kor_szamit()

    def kor_szamit(self):
        jelenlegi_ev=datetime.now().year
        return jelenlegi_ev - self.szul_datum
    
    def __str__(self):
        return (f"Név: {self.nev}, Kor: {self.kor}, Születési dátum: {self.szul_datum}, Fizetes: {self.fizetes}, Pozício: {self.pozicio}")