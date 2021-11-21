from tkinter import *
from data import *
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=50, pady=50)
        self.language_text = self.canvas.create_text(150, 125, text="language", fill="black",
                                                     font=("Arial", 20, "italic"))
        self.score = Label(text=f"Score: ", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)
        self.true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_button_image, command=None, highlightthickness=0, bd=0)
        self.true_button.grid(column=0, row=2)
        self.false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_button_image, command=None, highlightthickness=0, bd=0)
        self.false_button.grid(column=1, row=2)
        self.window.mainloop()