def etlap(etel_lista):
    """itt írjuk ki az ételek neveit"""
    for i in range(0, len(etel_lista),1):
        print(f"** {etel_lista[i].nev} {etel_lista[i].ar} Ft **")

def atlag_ar(etel_lista):
    osszeg:float=0
    for i in range(0, len(etel_lista),1):
        osszeg+=etel_lista[i].ar
    return osszeg/len(etel_lista)

def legdragabb(etel_lista):
    max_index:float=0
    for i in range(0, len(etel_lista),1):
        if(etel_lista[i].ar>etel_lista[max_index].ar):
            max_index=i
        return max_index
    
def ossz_fizu(szolga_lista):
    osszeg:float=0
    for i in range(0, len(szolga_lista),1):
        osszeg+=szolga_lista[i].fizetes
    return osszeg


        
