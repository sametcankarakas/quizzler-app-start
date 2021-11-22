from tkinter import *
from quiz_brain import QuizBrain
from data import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score_point = 0
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="some text here",
                                                     fill="black",
                                                     font=("Arial", 20, "italic")
                                                     )
        self.score = Label(text=f"Score: {self.score_point}", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)
        self.true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_button_image, command=self.true_button_press, highlightthickness=0,
                                  bd=0)
        self.true_button.grid(column=0, row=2)
        self.false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_button_image, command=self.false_button_press,
                                   highlightthickness=0, bd=0)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.true_text = "true"
        self.false_text = "false"
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_button_press(self):
        is_right = self.quiz.check_answer(self.true_text)
        self.give_feedback(is_right)



    def false_button_press(self):
        is_right = self.quiz.check_answer(self.false_text)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.score_point += 1
            self.canvas.config(bg="green")
            self.score.config(text=f"Score: {self.score_point}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.get_next_question)

