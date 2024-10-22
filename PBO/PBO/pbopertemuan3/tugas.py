#membuat Kelas Hero
class Hero:
    #membuat konstruktor uuntuk menampung atribut
    def __init__(self, name, role, health_point, attack_damage, skill):
    #lakukan iinisiasi untuk masing masing variabel
        self.nm = name
        self.rl = role
        self.hp = health_point
        self.ad = attack_damage
        self.sk = skill
#membuat method attack
    def attack(self, target):
        target.hp -= self.ad
        print(f"{self.nm} menyerang {target.nm}")
        print(f"{target.nm} kehilangan {self.ad} HP.")
#membuat method Use Skill
    def useSkill(self, target):
        target.hp -= self.ad * 2.5
        print(f"{self.nm} Menggunakan Skill : {self.sk}! \n{target.nm} Kehilangan {self.ad * 2.5} HP")
#membuat methode show stats
    def showStats(self):
        print(f"Status {self.nm}")
        print(f"Role {self.rl}")
        print(f"HP {int(self.hp)}")
        print(f"AD {self.ad}")
        print(f"Skill {self.sk}")
        print("----------")

layla = Hero("layla", "marksman", 350, 50, "Destruction Rush")
tigreal = Hero("Tigreal", "Tank", 500, 40, "Sacred Hammer")
# Tigreal.showStats()
layla.attack(tigreal)
tigreal.useSkill(layla)
layla.showStats()
tigreal.showStats()

