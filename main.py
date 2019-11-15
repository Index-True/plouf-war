grids = [
    [
        [
            0 for _ in range(10) # Generation d'une ligne contenant 10 `0`
        ] for _ in range(10) # generation de 10 lignes
    ], # Grille du joueur 0
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

