def askCell(text):
    tab = ["A","B","C","D","E","F","G","H","I","J"]

    userInput = input(text)

    while not userInput[0] in tab and not userInput[1:].isdigit() and not 1 <= userInput[1:] <= 10:

        userInput = input("Please enter values like A2 : ")
    
    col = tab.index(userInput[0])
    line = userInput[1:]
    
    return line, col
print(askCell("B8"))


'''def placeBoat(boatSize, boatId,grid):
    
    
    posiD = input("Enter the first cell of the table where you want to put your "+str(boatSize)+" cell boat ex:A1 :")

#test si l'input est une chaine de 2 caractere, si le premier caractere est une lettre compris dans le tableau et le deuxieme caractere un nombre entre 1-10
    
            
    direction = input("enter a direction ")''' 
'''  '''