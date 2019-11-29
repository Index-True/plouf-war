from .userInteractions import askCell

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
            for line in grids[playerId]:
                for cell in line:
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

def shoot(playerId, grids):
    """
    fonction qui demande a l'utilisateur où il veut tirer
    # Parametres
    playerId : Id du joueur qui tire ( int 0 ou 1)
    grids : grilles d'etat de la partie
    # Retourne
    hasWon : bool , vrai si le joueur viens de gagner la partie faux sinon
    """
    target = 1 if playerId == 0 else 0
    
    while True:
        line, col = askCell("Coordonnées du tir ? [A-J][1-10]")
        if not grids[target][line][col] in [1,2,3]:
            break
        print("Vous avez déja tiré ici...")

    if grids[target][line][col] == 0:
        # tir dans l'eau
        grids[target][line][col] = 1
        return False
    
    grids[target][line][col] = 2
    shipKilled, hasWon = scan(target,grids)

    if shipKilled:
        grids[target][line][col] = 3
        
    return hasWon