import random

class joueur :
    def __init__(self, vie, potions, attaque):
        self.vie = vie
        self.potions = potions
        self.attaque = attaque
        
    def utiliser_potion(self):
        if self.potions > 0:
            self.vie += random.randint(15,50)
            self.potions -= 1
            print("Potion utilisée! Vie actuelle:", self.vie)
        else:
            print("Pas de potions restantes!")
            
    def attaquer(self, ennemie):
        ennemie.vie -= self.attaque
        print("Ennemi attaqué! Vie de l'ennemi restante:", ennemie.vie)