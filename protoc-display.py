def displayScreen(screen,viewer) :
    if viewer :
        disIn = [0,1,2,3,20,30,31,40,50]
        disOut = [" ∙ "," o ","▒▒▒","▒▒▒","███","███","███","███","███"]
        for i in range(10):
            ln = ""
            for j in range(10):
                l = 0
                for k in disIn:
                    if (screen[i][j] == k):
                        ln += disOut[l]
                    l += 1
            print(ln)
    else:
        disIn = [0,1,2,3,20,30,31,40,50]
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
