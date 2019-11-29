import copy
from .display import displayScreen


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


def ask(text, answers):
    """
    Fonction ask, permet de demander a l'utilisateur de choisir entre plusieurs possibilitées

    text: Texte affiché à l'utilisateur lors de la demande
    answers: réponses possibles

    Return : la reponse fournie par l'utilisateur
    """
    answersStrings = [str(a) for a in answers]

    answersDisplay = "("
    for a in answers:
        answersDisplay += f"{a} "
    answersDisplay += ")"

    userInput = input(f"{text} {answersDisplay} ")

    while userInput not in answersStrings:
        userInput = input(
            f"Merci d'entrer une valeur parmis {answersDisplay} ")

    return answers[answersStrings.index(userInput)]


def placeBoat(grids, playerID):

    boats = [
        (5, 0, "Porte-Avion"),
        (4, 0, "Croiseur"),
        (3, 0, "Contre-torpilleur"),
        (3, 1, "Contre-torpilleur"),
        (2, 0, "Torpilleur"),
    ]

    for boatSize, boatId, boatName in boats:
        boatPlaced = False
        while not boatPlaced:
            cell = askCell(
                f"Ou placer le {boatName} ? (Nom de la cellule ex: A2)")

            orientation = ask("""Dans quelle orientation placer le bateau ?
H : horizontal vers la droite
H- : horizontal vers la gauche
V : Vertical vers le haut
V- : Vertical vers le bas""", ["H", "H-", "V", "V-"])

            if orientation == "H" and cell[1] + boatSize < len(grids[playerID][0]):
                cellsToCheck = [ (cell[0], i) for i in range(cell[1], cell[1] + boatSize) ]
            
            elif orientation == "H-" and 0 <= cell[1] - boatSize:
                cellsToCheck = [ (cell[0], i) for i in range(cell[1] - boatSize,cell[1]) ]

            elif orientation == "V" and 0 <= cell[0] - boatSize :
                cellsToCheck = [ (i, cell[0]) for i in range(cell[0] - boatSize,cell[0]) ]

            elif orientation == "V-" and cell[0] + boatSize < len(grids[playerID]):
                cellsToCheck = [ (i, cell[0]) for i in range(cell[0],cell[0] + boatSize) ]
                
            checkFailed = False

            for c in cellsToCheck:
                if grids[playerID][c[0]][c[1]] != 0:
                    checkFailed = True
                    break
            
            if not checkFailed:
                tempGrids = copy.deepcopy(grids)

                for c in cellsToCheck:
                    tempGrids[playerID][c[0]][c[1]] = boatSize * 10 + boatId

                displayScreen(tempGrids,playerID,True)

                if ask("Valider ce placement ? ", ["Oui", "Non"]) == "Oui" :
                    grids = tempGrids
                    boatPlaced = True
                


                 
            