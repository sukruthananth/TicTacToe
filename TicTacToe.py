from tkinter import *
import numpy as np

class TicTacToe:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.height = 600
        self.width = 600
        self.canvas = Canvas(self.window, width = self.width, height =self.height)
        self.canvas.pack()
        self.window.bind('<Button-1>',self.click)
        self.player_X = False
        self.player_O = False
        self.player_turn = None
        self.gap = self.width//3
        self.draw_board()
        self.value = np.zeros(shape=(3,3))
        self.player_X_score = 0
        self.player_O_score = 0
        self.tie_score = 0
        self.reset_board = False

    def draw_board(self):
        #draw columns
        for i in range(3):
            self.canvas.create_line(0,i*self.gap,self.height, i*self.gap, width = 3)
            self.canvas.create_line(i*self.gap,0,i*self.gap,self.width, width = 3)

    def click(self,event):
        real_y = event.x//self.gap
        real_x = event.y//self.gap

        if not self.reset_board:
            if np.count_nonzero(self.value) < 9:
                if self.player_X == False or self.player_turn ==0:
                    self.player_turn = 1
                    self.player_X = True
                    if self.value[real_x][real_y] ==0:
                        self.value[real_x][real_y] = 1
                        self.create_player(real_y, real_x)
                    if self.validate_board():
                        self.show_result(1)
                elif self.player_O == False or self.player_turn ==1:
                    self.player_O = True
                    self.player_turn = 0
                    if self.value[real_x][real_y] ==0:
                        self.value[real_x][real_y] = 2
                        self.create_player(real_y, real_x)
                    if self.validate_board():
                        self.show_result(0)
                elif np.count_nonzero(self.value) == 9:
                    self.show_result(2)
            else:
                self.show_result(2)
        else:
            self.canvas.delete("all")
            self.player_X = False
            self.player_O = False
            self.player_turn = None
            self.value = np.zeros(shape=(3, 3))
            self.draw_board()
            self.reset_board = False

    def create_player(self,x,y):
        if self.player_turn:
            self.canvas.create_line(x*self.gap+50, y*self.gap+50, x*self.gap +self.gap-50, y*self.gap +self.gap-50, width = 4, fill = 'red')
            self.canvas.create_line(x*self.gap + self.gap-50, y*self.gap + 50, x*self.gap+50, y*self.gap +self.gap-50, width = 4, fill = 'red')
        else:
            self.canvas.create_oval(x*self.gap+50, y*self.gap+50, x*self.gap + self.gap-50, y*self.gap+self.gap-50, width = 4,outline = 'blue')

    def validate_board(self):
        # checking the rows
        for i in range(3):
            if self.value[i][i]!=0 and (self.value[i][0] == self.value[i][1] ==self.value[i][2] or self.value[0][i] == self.value[1][i] == self.value[2][i]):
                return True
        # checking the diagonals
        if (self.value[0][0] == self.value[1][1] == self.value[2][2] or self.value[0][2] == self.value[1][1] == self.value[2][0]) and self.value[1][1]!=0:
            return True
        return False

    def show_result(self, winner):
        self.canvas.delete("all")
        if winner == 1:
            text = "Player 1 wins"
            self.player_X_score +=1
            color ='red'
        elif winner == 0:
            text = "Player 2 wins"
            self.player_O_score +=1
            color = 'blue'
        else:
            color = 'Grey'
            text = "It is a Tie game"
            self.tie_score +=1

        # show the result with the text
        self.canvas.create_text(self.width/2,self.height/3, font = "cmr 60 bold", fill = color, text= text)

        self.canvas.create_text(self.width / 2, 5*self.height / 8, font="cmr 40 bold", fill="green", text="Scores")

        scores = "Player X : " +str(self.player_X_score) +"\n" + "Player O : " + str(self.player_O_score) +"\n" + "Tie             : " + str(self.tie_score)

        self.canvas.create_text(self.width/2, 3 *self.height/4, font = "cmr 30 bold", fill = "green", text= scores )

        self.canvas.create_text(self.width/2, 15*self.height/16, font= "cmr 20 bold", fill = "grey", text = "Click to play again\n")
        self.reset_board = True

play_game = TicTacToe()
play_game.window.mainloop()

