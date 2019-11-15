def placeBoat(boatSize, boatId,grid):
    tab = ["A","B","C","D","E","F","G","H","I","J"]
    posiD = input("Enter the first cell of the table where you want to put your "+str(boatSize)+" cell boat ex:A1 :")
    


    for i in range(len(tab)):
        if posiD[0] ==tab[i]:
            posiD[0] = i
