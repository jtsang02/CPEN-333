# student name:     Josiah Tsang
# student number:   74191248
from queue import Full
import random

class TicTacToe:
    def __init__(self): # Use as is
        """ initializes data fields (board and played) 
            and prints the banner messages 
            and prints the initial board on the screen
        """
        self.board = [' '] * 9 # A list of 9 strings, one for each cell, 
                               # will contain ' ' or 'X' or 'O'
        self.played = set()    # Set (of cell num) already played: to keep track of the played cells 
        print("Welcome to Tic-Tac-Toe!")
        print("You play X (first move) and computer plays O.")
        print("Computer plays randomly, not strategically.")
        self.printBoard()

    def printBoard(self) -> None:
        """ prints the board on the screen based on the values in the self.board data field """
        print()
        print(self.board[0],"|", self.board[1], "|", self.board[2],"   ", "0 | 1 | 2")  # first line
        print("--+---+--","   ", "--+---+--")                                           # line separation
        print(self.board[3],"|", self.board[4],"|", self.board[5],"   ", "3 | 4 | 5 ")  # second line
        print("--+---+--","   ", "--+---+--")                                           # line separation
        print(self.board[6],"|", self.board[7],"|", self.board[8],"   ", "6 | 7 | 8 ")  # second line
        print()

    def playerNextMove(self) -> None:
        """ prompts the player for a valid cell number; 
            error checks that the input is a valid cell number; 
            and prints the info and the updated self.board;
        """
        while (True):
            try:
                x = int(input("Next move for X (state a valid cell num):"))
                if (x in range(0,9)):
                    if (x in self.played):
                        print("Must enter a valid cell number")
                    else:
                        break
                else:
                    print("Must enter a valid cell number")            
            except:
                print("Must be an integer")              
        self.played.add(x)
        self.board[x] = 'X' 
        print("you chose cell", x)  
        self.printBoard()

    def computerNextMove(self) -> None:
        """ computer randomly chooses a valid cell, 
            and prints the info and the updated self.board 
        """
        while (True):
            o = random.randint(0,8)                  # choose random number from 0 to 8
            if (o in self.played): continue          
            else: break
        print("Computer chose cell", o)
        self.played.add(o)
        self.board[o] = 'O'
        self.printBoard()

    def hasWon(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
        # horizontal win conditions: {0, 1, 2}, {3, 4, 5}, {6, 7, 8}
        # vertical win conditions: {0, 3, 6}, {1, 4, 7}, {2, 5, 8}
        # diagonal win conditions: {0, 4, 8}, {2, 4, 6}
        allWinCombos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                    [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                    [0, 4, 8], [2, 4, 6]]
        for winCombo in allWinCombos:
            if all(self.board[move] == who for move in winCombo):
                return True
        return False

    def terminate(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
            it also prints the final messages:
                 "You won! Thanks for playing." or 
                 "You lost! Thanks for playing." or 
                 "A draw! Thanks for playing."  
        """
        if (self.hasWon(who)):
            if (who == 'X'):
                print("You won! Thanks for playing.")
            else:
                print("You lost! Thanks for playing.")
            return True
        else:
            if (len(self.played) == 9):
                print("A draw! Thanks for playing.")
                return True
            else:
                return False    # keep playing

if __name__ == "__main__":  # Use as is
    ttt = TicTacToe()  # initialize a game
    while True:
        ttt.playerNextMove()            # X starts first
        if(ttt.terminate('X')): break   # if X won or a draw, print message and terminate
        ttt.computerNextMove()          # computer plays O
        if(ttt.terminate('O')): break   # if O won or a draw, print message and terminate