def placeBoat(boatSize, boatId,grid):
    tab = ["A","B","C","D","E","F","G","H","I","J"]
    
    posiD = input("Enter the first cell of the table where you want to put your "+str(boatSize)+" cell boat ex:A1 :")

#test si l'input est une chaine de 2 caractere, si le premier caractere est une lettre compris dans le tableau et le deuxieme caractere un nombre entre 1-10
    while posiD != 1 or posiD[0] != (val for val in tab)or posiD[1]-1!= (j for j in range(len(tab))):

        posiD = input("Please enter values like A2 : ")
        
        
    for i in range(len(tab)):#replacer la lettre par un nombre
        if posiD[0] ==tab[i]:
            posiD[0] = i
            
    