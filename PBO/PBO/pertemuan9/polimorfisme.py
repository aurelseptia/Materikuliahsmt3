#tanpa implementasi polimorfisme
class jumlah:
    def tambah(n1 , n2):
        print (f"hasilnya : {n1+n2}")
objek3 = jumlah
objek3.tambah(1,2,3) #menghasilkan error karena jumlah parameter strict wajib 2
#implementasi polimorfisme
class penjumlahan:
    def tambah(*num):
        return sum(num)
objek1 = penjumlahan
print(objek1.tambah(2,3)) #tidak meghasilakan error 

#menggunakan defaault parameter
class Default:
    def tambah2(a, b,c=0,d=0,e=0):
        print (f"hasilnya (a+b+c+d+e)")
objek2 = Default
objek2.tambah2(2,4,2,3,5)




#contoh awal
#class penjumlahan:
    #def tambah(n1 , n2):
        #print (f"hasilnya : {n1+n2}")
#objek1 = penjumlahan
#print(objek1.tambah(2,3,5,10))