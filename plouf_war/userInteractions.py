def askCell(text):
    """
    Fonction askCell, demande a l'utilisateur d'entrer une case, verifie les informations
    entrées et retourne la case
    # Paramètres
    text : Le texte a afficher a l'utilisateur pour lui demander une case
    # Return
    retourne deux valeurs:
    line : l'index de la ligne
    col : l'index de la colone
    """
    tab = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    userInput = input(text)

    while (not userInput[0] in tab) or (not userInput[1:].isdigit()) or (not 1 <= int(userInput[1:]) <= 10):

        userInput = input("Please enter values like A2 : ")

    col = tab.index(userInput[0])
    line = int(userInput[1:])

    return line, col


def isIntinRange(var, min, max):
    testFor = True
    while testFor:
        while not isinstance(var, int):
            try:
                var = int(input("Entrez un entier comprit entre " +
                                str(min) + " et " + str(max) + ": "))
            except ValueError:
                var = "notInt"
        if var < max+1 and var > min-1 and var % 1 == 0:
            testFor = False
        else:
            var = "notInt"
    return var


def placeBoat(girds, playerID):

    testFor1 = False
    boatsNames = ["Torpilleur", "Contre-torpilleur","Contre-torpilleur", "Croiseur", "Porte-Avion"]
    boatsIDs = [20, 30, 31, 40, 50]
    boatsSizes = [2, 3, 3, 4, 5]
    extrX = 0
    extrY = 0

    for i in range(5):
        dumpTest = []
        while not testFor1:
            pointeurY, pointeurX = askCell(
                "Entez la case du coin superieur gauche du " + boatsNames[i] + "sous la forme \"A1\"")

            print("Choisissez l'orientation du navire: \n 1 - Horizontal \n 2 - Vertical")
            inOrient = isIntinRange("", 1, 2)

            if inOrient == 1:
                extrX = pointeurX + (boatsSizes[i]-1)
                extrY = pointeurY

            elif inOrient == 2:
                extrX = pointeurX
                extrY = pointeurY + (boatsSizes[i]-1)

            if not (extrX > 9 or extrY > 9):
                for j in range(boatsSizes[i]):
                    dumpTest[j] = girds[playerID][(
                        pointeurY+(pointeurY+(extrY)/j+1))][(pointeurX+(pointeurX+(extrX)/j+1))]

            if dumpTest == [0]*len(dumpTest):
                testFor1 = True
                for k in range(boatsSizes[i]):
                    girds[playerID][pointeurY+(pointeurY+(extrY)/k+1)][pointeurX+(pointeurX+(extrX)/k+1)] = boatsIDs[i]
            else:
                print("Votre bateau ne peut pas être placé ici")