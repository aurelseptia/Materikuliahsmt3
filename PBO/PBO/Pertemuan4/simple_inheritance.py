#class simple Inheritance
class Animal:
    #membuat konstruktor untuk menampung atribut
    def __init__ (self, name, ras):
        self.name = name
        self.ras = ras
    #membuat method bersuara
    def Speaks(self):
        print(f"{self.name} bisa bersuara")
#membuat kelas 1 turunan dari super kelas
class Cat(Animal):
    def speaksCat(self):
        print(f"Nama {self.name} dengan Ras {self.ras} bersuara Meeeowww")

#Membuaat kelas 2 turunan dari super kelas
class Dog(Animal):
    def speaksDog(self):
         print(f"Nama {self.name} dengan Ras {self.ras} bersuara Gukkgukk")

#Membuat objek
cat = Cat("Kitty", "Angora")
cat.speaksCat()
dog = Dog("Puppy", "Pitbull")
dog.speaksDog()