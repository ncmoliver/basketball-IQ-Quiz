import random

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = random.randint(0,25)
        self.question_list = q_list
        self.quiz_length = 0
        self.run = 0
        self.correct = 0
        self.incorrect = 0
        self.easy = 5
        self.medium = 7
        self.hard = 10
        self.user_answers = []



    def selectDifficulty(self):
        difficulty = int(input("Select Level of Difficulty:\n"
                  "1. Easy     |   5 Questions\n"
                  "2. Medium   |   7 Questions\n"
                  "3. Hard     |   10 Questions"))
        if difficulty == 1:
            self.quiz_length == self.easy
        elif difficulty == 2:
            self.quiz_length == self.medium
        elif difficulty == 3:
            self.quiz_length == self.hard
        else:
            print("Invalid option: Defaulting to Easy Level settings")
            self.quiz_length == self.easy
        return difficulty
        

    def still_has_questions(self):
            if self.run < self.quiz_length:
                return True
            else:
                return False


    def next_question(self):
            #pull questions
            current_question = self.question_list[self.question_number]
            while self.run <= self.quiz_length:
                user_answer = input(f"Q. {self.question_number}: {current_question.text} (True/False): ")
                self.user_answers.append(user_answer)
                self.question_number += 1
                self.run += 1
                return self.user_answers
            else:
                 print("Error: next question fx")
