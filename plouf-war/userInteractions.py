def askCell(text):
    tab = ["A","B","C","D","E","F","G","H","I","J"]

    userInput = input(text)

    while not userInput[0] in tab and not userInput[1:].isdigit() and not 1 <= userInput[1:] <= 10:

        userInput = input("Please enter values like A2 : ")
    
    col = tab.index(userInput[0])
    line = userInput[1:]
    
    return line, col