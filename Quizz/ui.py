from tkinter import *
from quiz_brain import QuizBrain

# Constants
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Initialize QuizInterface with a QuizBrain object
        self.quiz = quiz_brain

        # Create the main window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas for question text
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic")
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        # False button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,  command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        # Get the first question
        self.get_next_question()

        # Start the main loop
        self.window.mainloop()

    def get_next_question(self):
        # Configure canvas and display next question
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # End of quiz
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        # Handle True button press
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        # Handle False button press
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        # Give feedback based on user's answer
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # Get next question after a delay
        self.window.after(1000, self.get_next_question)
