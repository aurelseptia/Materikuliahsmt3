class Buku:
    jumlah_mobil= 0
    def __init__(self, judulbuku, penerbit, penulis):
        self.judulbuku = judulbuku
        self.penerbit = penerbit
        self.penulis = penulis
    #Membuat method string
    def __str__(self):
        return f"{self.judulbuku}, {self.penerbit}, {self.penulis}"
    def boreup(self, bore):
        self.kapasitas += bore
#Membuat object baru M1
M1 = Buku("Sinila", "Elexmedia", Salman_Ayashi)
print(M1)
print("Jumlah Buku:". Buku.jumlah_buku)
M1.boreup(500)
print(M1)
#Membuat objek Baru M2
M2 = Buku("Mariposa", "Added", Novaayu)
print (M2)
print("jumlah buku: ", Buku.jumlah_buku)