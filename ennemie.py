import random

class ennemie :
    def __init__(self, vie, attaque):
        self.vie = vie
        self.attaque = attaque
        
    def attaquer(self, joueur):
        joueur.vie -= self.attaque
        print("Joueur attaqué! Vie du joueur restante:", joueur.vie)