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
                                                     colone  |
                                                         ligne
"""


def scan(playerId, grids):
    """
    # Description 
        Fonction `scan(playerId)` permet de surveiller l'etat de la grille et d'informer 
        la fonction parente si le joueur vient de couler un bateau ou si il vient de gagner.
    ## Parmetres
        playerId : L'id sur player dont il faut scanner la grille
        grids : Les grilles de status du jeu   
    ## Retourne
        Elle retourne un tuple `(shipKilled, hasWon)` de booleens, 
        shipKilled est a true si un bateau viens d'etre coulé
        hasWon est a true si le joueur viens de gagner
    """
    shipKilled, hasWon = False, True
    for ship,status in scan.stats[playerId].items():
        if status:
            status = False
            for col in grids[playerId]:
                for cell in col:
                    if cell == ship:
                        status = True
            if not status:
                scan.stats[playerId][ship] = status
                shipKilled = True
    
    for ship in scan.stats[playerId]:
        if scan.stats[playerId][ship]:
            hasWon = False
    return shipKilled, hasWon

scan.stats = [
    {
        50: True, 40: True, 30: True, 31: True, 20: True
    } for i in range(2)
]