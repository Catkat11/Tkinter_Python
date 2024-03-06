from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Creating an empty list to store Question objects
question_bank = []

# Iterating through each question data fetched from question_data
for question in question_data:
    # Extracting question text and answer from each question data
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # Creating a new Question object using the extracted data
    new_question = Question(question_text, question_answer)

    # Adding the created Question object to the question_bank list
    question_bank.append(new_question)

# Creating a QuizBrain object with the question_bank list
quiz = QuizBrain(question_bank)

# Creating a QuizInterface object to handle the user interface
quiz_ui = QuizInterface(quiz)

# Printing a message indicating quiz completion along with the final score
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
