from tkinter import *
from tkinter import messagebox
from cardSelector import CardSelector
from ttStats import TTStats

class CardGame:

    cardRows = 3
    cardColumns = 3

    cardList = []
    cardImages = []
    clickedIds = []

    def __init__(self, tk: Tk):
        self.tk = tk
        self.tk.title("Card Game")

        self.mainFrame = Frame(self.tk, padx=20, pady=20)
        self.mainFrame.pack()

        self.logoImage = PhotoImage(file="textures/logo.png")
        self.gameLabelLogo = Label(self.mainFrame, image=self.logoImage)
        self.gameLabelLogo.pack()

        self.cardFrame = Frame(self.mainFrame, padx=10, pady=10)
        self.cardFrame.pack()

        self.labelCardValue = Label(self.mainFrame, font=("Noto Sans", 26))
        self.labelCardValue.pack()

        for x in range(self.cardRows):
            for y in range(self.cardColumns):
                imagePath = "textures/0.png"
                cardImage = PhotoImage(file=imagePath)
                cardId = (y + x * self.cardColumns)
                cardLabel = Label(
                    self.cardFrame, text=cardId, image=cardImage
                )
                cardLabel.grid(column=y, row=x, padx="0", pady="0")
                cardLabel.bind("<Button-1>", self.cardClick)

                self.cardList.append(cardLabel)
                self.cardImages.append(cardImage)

    def cardClick(self, event):
        label = event.widget
        labelId = label.cget("text")

        for x in self.clickedIds:
            if x == labelId:
                return

        self.cardSelector = CardSelector(self.tk)

        self.cardImages[labelId] = PhotoImage(file=f"textures/{self.cardSelector.cardValue}.png")
        label.config(image=self.cardImages[labelId])

        self.labelCardValue.config(text=label.cget("text"))

        self.clickedIds.append(labelId)






tk = Tk()
cardGame = CardGame(tk)
tk.mainloop()
