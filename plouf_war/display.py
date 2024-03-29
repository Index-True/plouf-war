def displayScreen(grid,playerID,mode) :
    """
    Input:
    gird = tableaux de donnés dans le tableau à trois dimensions
    playerID = id du joueur dont on veut afficher l'ecran
    mode = boolean, True = le joueur regarde son tableau
                    False= le joueur regarde le tableau de son adversaire
    """
    disIn = [0,1,2,3,20,30,31,40,50]
    screen = grid[playerID]

    if mode :
        disOut = [" ∙ "," o ","▒▒▒","▒▒▒","███","███","███","███","███"]
    else :
        disOut = [" ∙ "," o ","▒▒▒"," x "," ∙ "," ∙ "," ∙ "," ∙ "," ∙ "]

    print("    A  B  C  D  E  F  G  H  I  J")
    for i in range(10):
        ln = f"{i+1}".ljust(3," ")
        for j in range(10):
            l = 0
            for k in disIn:
                if (screen[i][j] == k):
                    ln += disOut[l]
                l += 1
        print(ln)