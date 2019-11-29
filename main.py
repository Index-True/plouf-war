from plouf_war import *
import os

def clear():os.system('cls' if os.name=='nt' else 'clear')

grids = [
    [
        [
            0 for _ in range(10)  # Generation d'une ligne contenant 10 `0`
        ] for _ in range(10)  # generation de 10 lignes
    ],  # Grille du joueur 0
    [
        [
            0 for _ in range(10)
        ] for _ in range(10)
    ]  # Grille du joueur 1
]

"""
Variable grids : contient l'etat de la grille de jeu pour les deux joueurs
pour acceder a la case B4 du joueur 1 on ecrit : grids[0][1][3]
                                                       |  |  |
                                                  joueur  |  |
                                                      ligne  |
                                                        colone
                                                         
"""

def game():
    player = 0
    enemy = 1
    print("Joueur 1 : Placement des bateaux")
    for boatSize, boatId in boats:
        placeBoat(grids, 0)
    
    clear()
    print("Joueur 2 : Placement des bateaux")
    for boatSize, boatId in boats:
        placeBoat(grids, 1)

    clear()

    while True:
        print(f"Au tour du joueur {player+1}")
        input("Appuiez sur entrée pour continuer")
        
        clear()
        print("Ennemi :")
        display.displayScreen(grids, enemy, False)

        print("Vous :")
        display.displayScreen(grids, player, True)
        
        if shoot.shoot(player,grids):
            break

        clear()
        print("Ennemi :")
        display.displayScreen(grids, enemy, False)

        print("Vous :")
        display.displayScreen(grids, player, True)
        
        input("Appuiez sur entrée pour continuer")
        clear()

        player, enemy = enemy, player
    print("Fin de partie")
        