def displayScreen(grid,playerID,mode) :
    """
    Input:
    gird = tableaux de donnés dans le tableau à trois dimensions
    playerID = l'exact même que dans le main, id du joeur qui va regarder l'output
    mode = boolean, True = le joueur regarde son tableau
                    False= le joueur regarde le tableau de son adversaire
    """
    disIn = [0,1,2,3,20,30,31,40,50]
    screen = grid[playerID]

    if mode :
        disOut = [" ∙ "," o ","▒▒▒","▒▒▒","███","███","███","███","███"]
    else
        disOut = [" ∙ "," o ","▒▒▒"," x "," ∙ "," ∙ "," ∙ "," ∙ "," ∙ "]
    for i in range(10):
        ln = ""
        for j in range(10):
            l = 0
            for k in disIn:
                if (screen[i][j] == k):
                    ln += disOut[l]
                l += 1
        print(ln)