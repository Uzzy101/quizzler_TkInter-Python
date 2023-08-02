from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = 'Quizzler'
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text=f'Score:{self.quiz.score}', bg=THEME_COLOR, fg='white', font=('Arial', 15, 'italic'))
        self.label.grid(column=1)

        self.canvas = Canvas(width=300, height=300)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.q_text = self.canvas.create_text(20, 125, fill=THEME_COLOR, text='', font=('Arial', 20, 'italic'))

        self.canvas_t = Canvas(width=100, height=97, highlightthickness=0)
        self.correct = PhotoImage(file='images/true.png')
        self.canvas_t.create_image(50, 50, image=self.correct)
        self.true_button = Button(self.window, image=self.correct, border=0, command=self.true)
        self.true_button.grid(column=0, row=2)
        self.canvas_t.grid(column=0, row=2, pady=20)

        self.canvas_f = Canvas(width=100, height=97, highlightthickness=0)
        self.wrong = PhotoImage(file='images/false.png')
        self.canvas_f.create_image(50, 50, image=self.wrong)
        self.false_button = Button(self.window, image=self.wrong, border=0, command=self.false)
        self.false_button.grid(column=1, row=2)
        self.canvas_f.grid(column=1, row=2, pady=20)

        self.q_box()
        self.window.mainloop()

    def q_box(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label.config(text=f'Score:{self.quiz.score}')
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=question, anchor=W, width=280)
        else:
            self.canvas.itemconfig(self.q_text, text='You have reached the end of the end of the quiz')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.q_box)
