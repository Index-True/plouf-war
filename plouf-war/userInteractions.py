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
    tab = ["A","B","C","D","E","F","G","H","I","J"]

    userInput = input(text)

    while not userInput[0] in tab and not userInput[1:].isdigit() and not 1 <= int(userInput[1:]) <= 10:

        userInput = input("Please enter values like A2 : ")
    
    col = tab.index(userInput[0])
    line = int(userInput[1:])
    
    return line, col