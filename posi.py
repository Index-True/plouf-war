def askCell(text):
    tab = ["A","B","C","D","E","F","G","H","I","J"]
    while not text[0] in tab and not text[1:].isdigit() and not 1 <= text[1:] <= 10:

        text = input("Please enter values like A2 : ")
    text = text[0]+', '+text[1:]
    text = text.split(', ')
    text[1]=int(text[1])
    for i in range(len(tab)):
        if text[0] == tab[i]:
            text[0] = i

    return(text)
print(askCell("B8"))


'''def placeBoat(boatSize, boatId,grid):
    
    
    posiD = input("Enter the first cell of the table where you want to put your "+str(boatSize)+" cell boat ex:A1 :")

#test si l'input est une chaine de 2 caractere, si le premier caractere est une lettre compris dans le tableau et le deuxieme caractere un nombre entre 1-10
    
            
    direction = input("enter a direction ")''' 
'''  '''