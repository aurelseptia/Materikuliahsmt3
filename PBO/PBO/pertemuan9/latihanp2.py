#implementasi polimorfisme dengan mencari bangun datar 
class BangunDatar: #abstract class
    def luas(self): #abstract method
        raise NotImplementedError("method wajib di implementasikan")
class Persegi(BangunDatar) : #Kelas turunan 1
    def __init__(self, sisi):
        self.sisi  = sisi
    def luas(self):
        print(f"luas persegi adalah: [self.sisi**2]")
class segitiga(BangunDatar) : # kelas turunan 2
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def luas(self):
        print(f"lus segitiga adalah: {(self.alas*self.tinggi)/2}")
class lingkaran(BangunDatar): #kelas turunan 3
    def __init__(self, r, spi=3.14):
        self.pi = pi 
        self.r = r 
    def luas(self):
        print(f"luas lingkaran adalah {self.pi*(self.r**2)}")
objek1 = Persegi(2) 
objek2 = segitiga(2,3)       
objek3 = lingkaran(5)
objek1.luas()
objek2.luas()
objek3.luas()

ytyv