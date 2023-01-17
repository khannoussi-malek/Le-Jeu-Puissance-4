

import tkinter as tk
from player import Player
from checkForWinner import CheckForWinner


class Board(tk.Frame):
    """
    its the bord or marice of the game we inisialize it with 0's
    and when we click on a button we change the text on the button, the text and color depend on the player
    and with every click we check if there is a winner
    and if they are a winner we show a message
    then we reset the bord
    """
    def __init__(self, master = None):
        super().__init__(master)
        self.grid(padx=30, pady=30)
        self.resetBord()
        self.create_buttons()
        self.playerPlay=Player()
        self.checking = CheckForWinner()
    def resetBord(self):
        self.grid = [[0]*7 for i in range(6)]
        
    def create_buttons(self):
        self.buttons = []
        for y in range(6):
            self.buttons.append([])
            for x in range(7):
                self.buttons[y].append(x)
                self.buttons[y][x] = tk.Button(self)
                self.buttons[y][x].grid(column = str(x), row = str(y))
                self.buttons[y][x].config(font = ('Arial', 22), width = 4, height = 2)
                self.buttons[y][x].config(anchor = 'center')
                self.buttons[y][x].config(command = lambda x=x,y=y: self.button_press(x,y))
       
    def button_press(self,x,y):
        verif = 5
        while self.grid[verif][x] != 0 and verif >= 0:
            verif = verif - 1
        y = verif
        if self.grid[y][x] == 0 and y >= 0:
            self.grid[y][x] = self.playerPlay.getPlayer()

            if hasattr(self, 'winner'):
                self.winner.destroy()
            if( self.playerPlay.getPlayer()==1):
                self.buttons[int(y)][int(x)].config(text = '⚪', bg = 'black', fg = 'white')
            else:
                self.buttons[int(y)][int(x)].config(text = '⚫', bg = 'white', fg = 'black')
            if self.checking.search(self.grid):
                self.winner = tk.Label(self, text = 'Player ' + str(self.playerPlay.getPlayer()) + ' wins! 🥳')
                self.winner.config(font = ('Arial', 30))
                self.winner.grid(column = '0', row = '6', columnspan = '7')
                self.playerPlay.resetPlayer()
                self.resetBord()
                self.create_buttons()
            else:
                self.playerPlay.nextPlayer()
                
           