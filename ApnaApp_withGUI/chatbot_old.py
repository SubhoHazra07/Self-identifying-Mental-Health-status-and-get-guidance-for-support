import json
import random

class ChatBot:
    def __init__(self):
        self.questions = self.load_questions()
        self.points = 0
        self.content=self.load_content()

    def load_questions(self):
        with open('Intents2.json', 'r') as f:
            intents = json.load(f)
        return intents['intents'][:15]  # Get the first 5 questions

    def ask_question(self, question):
        print(question['patterns'][0])
        options = question.get('options', {})
        for key, value in options.items():
            print(f"{key}: {value['text']}")

    def get_user_answer(self):
        answer = input("Your answer (enter the option letter): ").lower()
        return answer

    def calculate_points(self, user_answer, question):
        options = question.get('options', {})
        if user_answer in options:
            self.points += options[user_answer]['points']

    def load_content(self):
        with open('content.json', 'r') as f:
            return json.load(f)

    def run(self):
        print("Welcome to the ChatBot!")
        for question in self.questions:
            self.ask_question(question)
            user_answer = self.get_user_answer()
            self.calculate_points(user_answer, question)
            print(f"You chose: {user_answer}\n")

        print("Thank you for answering the questions!")
        self.analyze_and_feedback()

    def analyze_and_feedback(self):
        print("\nAnalyzing your responses...")
        if self.points > 36:
            print("Your mental health condition is GOOD. Keep it up!")
        elif 18 <= self.points <= 32:
            print("Your mental health condition is BAD. Let me cheer you up!")
            self.tell_jokes_and_affirmations()
        else:
            print("Your mental health condition is CRITICAL. Please consider seeking professional help.")

    def tell_jokes_and_affirmations(self):
        jokes = self.content.get('jokes', [])
        affirmations = self.content.get('affirmations', [])

        print("\nHere are some jokes to lighten your mood:")
        for i in range(1,4):
            print(random.choice(jokes))

        print("\nAnd some affirmations to boost your spirits:")
        for i in range(1,4):
            print(random.choice(affirmations))


if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.run()
