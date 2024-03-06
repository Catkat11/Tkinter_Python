import html

class QuizBrain:
    def __init__(self, q_list):
        # Initialize QuizBrain object with question number, score, question list, and current question attributes
        self.question_number = 0  # Tracks current question number
        self.score = 0  # Tracks user's score
        self.question_list = q_list  # List of Question objects
        self.current_question = None  # Current Question object

    def still_has_questions(self):
        # Check if there are still questions in the question list
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Get the next question from the question list
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Decode HTML entities in question text
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        # Check if the user's answer matches the correct answer, update score accordingly
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
