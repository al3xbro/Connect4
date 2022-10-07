import os
class Board: 

    chipArray = [[" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "], 
                [" ", " ", " ", " ", " ", " ", " "], 
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "], 
                [" ", " ", " ", " ", " ", " ", " "]]

    def __init__ (self):
        pass            

    def placeChip (self, redOrYellow):
        success = 0
        colFail = False
        inpFail = False
        while success == 0:
            os.system("CLS")
            if redOrYellow == "r":
                self.printInfo()
                print ()

                # checks for fails
                if colFail:
                    print ("You can't place a chip there!")
                    colFail = False
                elif inpFail:
                    print ("Please type in the number of a column.")
                    inpFail = False

                whichColumn = input ("Place a red chip.\n")

                # input valid?
                if whichColumn == "0" or whichColumn == "1" or whichColumn == "2" or whichColumn == "3" or whichColumn == "4" or whichColumn == "5" or whichColumn == "6" or whichColumn == "7":
                    for i in reversed (range (6)):
                        if self.chipArray[i][int (whichColumn)] == " ":
                            self.chipArray[i][int (whichColumn)] = "r"
                            success = 1
                            break
                    # space?
                    else:
                        colFail = True
                else:
                    inpFail = True

            elif redOrYellow == "y":
                self.printInfo()
                print ()

                # checks for fails
                if colFail:
                    print ("You can't place a chip there!")
                    colFail = False
                elif inpFail:
                    print ("Please type in the number of a column.")
                    inpFail = False
                whichColumn = input ("Place a yellow chip.\n")

                # input valid?
                if whichColumn == "0" or whichColumn == "1" or whichColumn == "2" or whichColumn == "3" or whichColumn == "4" or whichColumn == "5" or whichColumn == "6" or whichColumn == "7":
                    for i in reversed (range (6)):
                        if self.chipArray[i][int (whichColumn)] == " ":
                            self.chipArray[i][int (whichColumn)] = "y"
                            success = 1
                            break
                    # space?
                    else:
                        colFail = True
                else:
                    inpFail = True

    def checkWin (self, who):
        # vert check
        for row in range (0, 3): 
            for col in range (0, 7): 
                if self.chipArray[row][col] == who and self.chipArray[row+1][col] == who and self.chipArray[row+2][col] == who and self.chipArray[row+3][col] == who:
                    return True
        
        # hori check
        for row in range (0, 6):
            for col in range (0, 4):
                if self.chipArray[row][col] == who and self.chipArray[row][col+1] == who and self.chipArray[row][col+2] == who and self.chipArray[row][col+3] == who:
                    return True
        
        # upward diag check
        for row in range (3, 6):
            for col in range (0, 4):
                if self.chipArray[row][col] == who and self.chipArray[row-1][col+1] == who and self.chipArray[row-2][col+2] == who and self.chipArray[row-3][col+3] == who:
                    return True

        # downward diag check
        for row in range (0, 3):
            for col in range (0, 4):
                if self.chipArray[row][col] == who and self.chipArray[row+1][col+1] == who and self.chipArray[row+2][col+2] == who and self.chipArray[row+3][col+3] == who:
                    return True

        return False
                    

    def printInfo (self): 
        print ()
        print ("  0  |  1  |  2  |  3  |  4  |  5  |  6  ")
        for i in range (6):
            print ("  ", end="")
            for j in range (6):
                print (str(self.chipArray[i][j]) + "  |  ", end="")
            print (str(self.chipArray[i][6]), end="") 
            print ("")

    def clearBoard (self):
        chipArray = [[" ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " "], 
                    [" ", " ", " ", " ", " ", " ", " "], 
                    [" ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " "], 
                    [" ", " ", " ", " ", " ", " ", " "]]

##############################################################################################################
board = Board()
os.system("CLS")
board.printInfo()
print()
input ("Welcome to Connect4! Type in the column you want to place your piece. Press enter to begin.\n")
while True:
    board.placeChip("r")
    if board.checkWin("r"):
        os.system("CLS")
        board.printInfo()
        print ()
        print ("Red won!")
        break

    board.placeChip("y")
    if board.checkWin("y"):
        os.system("CLS")
        board.printInfo()
        print ()
        print ("Yellow won!")
        break



