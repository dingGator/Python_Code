from oop_quiz_game__question_model import Question
from oop_quiz_game__data import question_data
from oop_quiz_game__quiz_brain import QuizBrain



question_bank = []

for question  in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

#print(question_bank[0].text)
#print(question_bank[0].answer)
quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
