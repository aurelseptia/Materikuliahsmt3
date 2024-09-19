# Membuat Class
class Mobil:
    #Membuat class variabel
    jumlah_mobil= 0
    #Membuat Construktor
    def __init__(self, ban, merk, cc):
        #instance variabel
        self.merkban = ban
        self.merkmobil = merk
        self.kapasitas = cc
        Mobil.jumlah_mobil += 1
    #Membuat method string
    def __str__(self):
        return f"{self.merkban}, {self.merkmobil}, {self.kapasitas}"
    def boreup(self, bore):
        self.kapasitas += bore
#Membuat object baru M1
M1 = Mobil("Bridgestone", "Toyota-Kijang", 1500)
print(M1)
print("Jumlah Mobil:". Mobil.jumlah_mobil)
M1.boreup(500)
print(M1)
#Membuat objek Baru M2
M2 = Mobil("Pirelli", "Subaru", 2000)
print (M2)
print("jumlah mobil: ", Mobil.jumlah_mobil)