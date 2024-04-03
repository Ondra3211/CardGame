from tkinter import *

class CardSelector:
    cardValue = 0

    def __init__(self, tk):
        self.tk = Toplevel(tk)
        self.tk.title("Card Selector")
        self.cardImages = []

        for x in range(10):
            imagePath = f"textures/{x+1}.png"
            cardImage = PhotoImage(file=imagePath)
            cardLabel = Label(self.tk, text=(x+1), image=cardImage)
            cardLabel.bind("<Button-1>", self.getCard)
            cardLabel.pack(side="left")

            self.cardImages.append(cardImage)

        self.tk.wait_window()

    def getCard(self, event):
        # UwU
        self.cardValue = event.widget.cget("text")
        self.tk.destroy()
        pass