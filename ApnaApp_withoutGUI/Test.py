import json
import random


class ChatBot:
    def __init__(self):
        self.content = self.load_content()

    def load_content(self):
        with open('content.json', 'r') as f:
            return json.load(f)

    def load_questions(self, option):
        with open('Test.json', 'r') as f:
            intents = json.load(f)
        all_questions = intents['intents']

        # Determine the range of questions based on the user's option
        if option == 1:
            return all_questions[:10]
        elif option == 2:
            return all_questions[10:18]
        elif option == 3:
            return all_questions[18:27]
        elif option == 4:
            return all_questions[27:31]
        elif option == 5:
            return all_questions[31:50]
        elif option == 6:
            return all_questions[50:67]
        elif option == 7:
            return all_questions[67:]
        else:
            return []

    def ask_question(self, question):
        print(question['patterns'][0])
        options = question.get('options', {})
        for key, value in options.items():
            print(f"{key}: {value['text']}")

    def get_user_choice(self):
        print("Choose an option:")
        print("Option 1 : Depression Test(PHQ - 9)")
        print("Option 2 : Anxiety Test(GAD - 7)")
        print("Option 3 : Bipoler Disorder Test(MDQ)")
        print("Option 4 : Addiction Test(CAGE)")
        print("Option 5 : Psychosis and Schizophrenia Test(PQB)")
        print("Option 6 : Adult Self Result Test(ADHD)")
        print("Option 7 : Post-Traumatic Test Disorder(PTSD)")
        user_choice = int(input("Your choice (enter the option number): "))
        return user_choice

    def get_user_answer(self):
        answer = input("Your answer (enter the option letter): ").lower()
        return answer

    def calculate_points(self, user_answer, question):
        options = question.get('options', {})
        if user_answer in options:
            return options[user_answer]['points']
        return 0

    def run(self):
        print("Welcome to the Testing Area!!!")
        user_choice = self.get_user_choice()
        questions = self.load_questions(user_choice)

        if not questions:
            print("Invalid option. Exiting.")
            return

        total_points = 0
        for question in questions:
            self.ask_question(question)
            user_answer = self.get_user_answer()
            total_points += self.calculate_points(user_answer, question)
            print(f"You chose: {user_answer}\n")

        print("Thank you for answering the questions!")
        self.analyze_and_feedback(total_points)

    def analyze_and_feedback(self, total_points):
        print("\nAnalyzing your responses...")
        if total_points > 32:
            print("You do not have this condition at all. Keep it up! We recommend you to take the other tests as well.")
            self.tell_jokes_and_affirmations()
        elif 18 <= total_points <= 32:
            print("Your test result shows that your condition is moderate. Make sure you take the other tests too so that you can get a clearer idea about your mental health.")
            self.tell_jokes_and_affirmations()
        else:
            print(
                "Your mental health condition is severe. Please consider seeking professional help.")

    def tell_jokes_and_affirmations(self):
        jokes = self.content.get('jokes', [])
        affirmations = self.content.get('affirmations', [])

        print("\nHere are some jokes to lighten your mood:")
        for i in range(1, 4):
            print(random.choice(jokes))

        print("\nAnd some affirmations to boost your spirits:")
        for i in range(1, 4):
            print(random.choice(affirmations))


if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.run()
