from tkinter import *
import random

root = Tk()
root.title("Encapsulation")
root.geometry("500x500")
root.config(bg = "white")

lbl_score = Label(root, font = ("Gigi", 15,"bold"), bg = "white")
lbl_score.place(relx = 0.1, rely = 0.2, anchor = W)

lbl_color = Label(root, font = ("Gigi", 30, "bold"), bg = "white")
lbl_color.place(relx = 0.5, rely = 0.4, anchor = CENTER)

entry_text_color = Entry(root)
entry_text_color.place(relx = 0.5, rely = 0.6, anchor = CENTER)

class Score():
    
    def __init__(self):
        self.__score = 0
        
    def updateGame(self):
        self.text = ["BLUE", "GREEN", "ORANGE", "PINK", "RED", "YELLOW", "PURPLE", "BROWN", "GREY", "BLACK"]
        self.random_no_text = random.randint(0, 9)
        
        self.color = ["Blue", "Green", "Orange", "Pink", "Red", "Yellow", "Purple", "Brown", "Grey", "Black"]
        self.random_no_color = random.randint(0, 9)
        
        lbl_color["text"] = self.text[self.random_no_text]
        lbl_color["fg"] = self.color[self.random_no_color]
        
    def __updateScore(self, entry_text_color):
        if entry_text_color == self.color[self.random_no_color]:
            print("You Guessed Correct Answer :)")
            self.__score += random.randint(0, 4)
            print("Score : ", str(self.__score))
            lbl_score["text"] = "Score : " + str(self.__score)
            
        elif entry_text_color != self.color[self.random_no_color]:
            print("You Guessed Incorrect Answer :(")
            self.__score -= random.randint(0, 4)
            print("Score : ", str(self.__score))
            lbl_score["text"] = "Score : " + str(self.__score)
            
    def get_updateScore(self, entry_text_color):
        self.__updateScore(entry_text_color)

obj = Score()

def get_textColor():
    text_color = entry_text_color.get()
    obj.get_updateScore(text_color)
    obj.updateGame()
    
    entry_text_color.delete(0, END)
        
btn_check = Button(root, text = "CHECK", command = get_textColor, relief = FLAT, bg = "pink", fg = "white", padx = 10, pady = 1, font = ("Arial", 15))
btn_check.place(relx = 0.3, rely = 0.8, anchor = CENTER)

btn_start = Button(root, text = "START", command = obj.updateGame, relief = FLAT, bg = "lightgreen", fg = "white", padx = 10, pady = 1, font = ("Arial", 15))
btn_start.place(relx = 0.7, rely = 0.8, anchor = CENTER)

root.mainloop()