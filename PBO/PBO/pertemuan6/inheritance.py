#membuat simple inheritance
#membuat kelas superclass Animal
class Animal:
  #membuat constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age
  #membuat method sound
  def sound(self):
    print(f"This {self.name} makes a sound")

  #membuat kelas turunan / subclass Dog
  class Dog(Animal):
    pass

  name = input("masukan Nama peliharaan anda ")
  dog = Animal(nama, 3)
  dog.sound()

  