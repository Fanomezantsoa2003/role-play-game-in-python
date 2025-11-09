from joueur import joueur
from ennemie import ennemie
import random

def main():
    Joueur = joueur(50, 3, random.randint(5, 10))
    Ennemie = ennemie(50, random.randint(5, 15))
    
    while Joueur.vie > 0 and Ennemie.vie > 0:
        action = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        if action == '1':
            Joueur.attaquer(Ennemie)
            
            if Ennemie.vie > 0:
                Ennemie.attaquer(Joueur)
                print(f"Le joueur a {Joueur.vie} points de vie.")
                print(f"L'ennemi a {Ennemie.vie} points de vie.")
                print(f'vous avez {Joueur.potions} potions restantes.')
                if Joueur.vie <= 0:
                    print("Le joueur est vaincu!")
            else:
                print("L'ennemi est vaincu!")
        elif action == '2':
            joueur.utiliser_potion()
            
            if Ennemie.vie > 0:
                Ennemie.attaquer(Joueur)
                print(f"Le joueur a {Joueur.vie} points de vie.")
                print(f"L'ennemi a {Ennemie.vie} points de vie.")
                print(f'vous avez {Joueur.potions} potions restantes.')
                if Joueur.vie <= 0:
                    print("Le joueur est vaincu!")
            else:
                print("L'ennemi est vaincu!")
        else:
            print("Action invalide. Veuillez choisir 1 ou 2.")
            
if __name__ == "__main__":
    main()