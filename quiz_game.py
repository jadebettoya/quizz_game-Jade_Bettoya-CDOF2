import random

class QuizGame:
    def __init__(self):
        self.questions = [
            "Quelle est la capitale de l'Espagne ?",
            "Quelle est la plus grosse planète du système solaire ?",
            "Qui a écrit 'Les Misérables' ?",
            "Quel est le plus long fleuve du monde ?",
        ]

        self.answers = [
            ["Madrid", "Londres", "Berlin"],
            ["Mars", "Jupiter", "Pluton"],
            ["Shakespeare", "Victor Hugo", "Zola"],
            ["Nil", "Mississippi", "Amazone"],
        ]

        self.correct_answers = [0, 1, 1, 2]  

        self.score = 0

    def shuffle_questions(self):
        combined = list(zip(self.questions, self.answers, self.correct_answers))
        random.shuffle(combined)
        self.questions, self.answers, self.correct_answers = zip(*combined)

    def display_question(self, question, choices):
        print(question)
        for i, choice in enumerate(choices, start=1):
            print(f"{i}. {choice}")
        user_answer = input("Votre réponse est (entrez le numéro) : ")
        return int(user_answer) - 1  

    def run_game(self):
        self.shuffle_questions()

        for question, choices, correct_answer in zip(self.questions, self.answers, self.correct_answers):
            user_choice = self.display_question(question, choices)

            if user_choice == correct_answer:
                print("Bonne réponse !")
                self.score += 1
            else:
                print("Mauvaise réponse. La bonne réponse était :", choices[correct_answer])

        print(f"Fin du jeu. Votre score est de {self.score}/{len(self.questions)}.")

if __name__ == "__main__":
    game = QuizGame()
    game.run_game()
