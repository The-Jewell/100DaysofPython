from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # question canvas
        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # false button
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, command=self.picked_false)
        self.false_button.config(highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        # true button
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, command=self.picked_true)
        self.true_button.config(highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz. Your final score is {self.quiz.score}/10 "
                                   )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def picked_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def picked_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(2000, self.get_next_question)


