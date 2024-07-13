import json
import random
import matplotlib.pyplot as plt
from cryptography.fernet import Fernet


class ChatBot:
    def __init__(self):
        self.questions = self.load_questions()
        self.points = 0
        self.content = self.load_content()
        self.points_over_time = []

    def load_questions(self):
        with open('Intents_init.json', 'r') as f:
            intents = json.load(f)
        return intents['intents'][:5]  # Get the first 5 questions

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
            self.points_over_time.append(options[user_answer]['points'])

    def plot_bar_chart(self):
        # Plotting the bar chart for points of each question
        question_numbers = range(1, len(self.points_over_time) + 1)
        plt.bar(question_numbers, self.points_over_time, color='blue')
        plt.xlabel('Question Number')
        plt.ylabel('Points')
        plt.title('Points for Each Question')
        avg_points = sum(self.points_over_time) / len(self.points_over_time)
        plt.axhline(avg_points, color='red', linestyle='dashed', linewidth=2, label=f'Average: {avg_points:.2f}')
        plt.legend()
        plt.show()


    def load_content(self):
        with open('content.json', 'r') as f:
            return json.load(f)

    def run(self):
        print("Welcome to the ChatBot!\nHere are few questions for you\n")
        for question in self.questions:
            self.ask_question(question)
            user_answer = self.get_user_answer()
            self.calculate_points(user_answer, question)
            print(f"You chose: {user_answer}\n")

        print("Thank you for answering the questions!")
        self.plot_bar_chart()
        self.analyze_and_feedback()

    def analyze_and_feedback(self):
        print("\nAnalyzing your responses...")
        if self.points > 10:
            print("Your mental health condition is GOOD. Keep it up!")
            self.login_form()
        elif 5 <= self.points <= 10:
            print("Your mental health condition is BAD. Let me cheer you up!")
            self.tell_jokes_and_affirmations()
            self.ask_mood()
        else:
            print("Your mental health condition is CRITICAL. Please consider seeking professional help.")

    def tell_jokes_and_affirmations(self):
        jokes = self.content.get('jokes', [])
        affirmations = self.content.get('affirmations', [])

        print("\nHere are some jokes to lighten your mood:")
        for i in range(1, 4):
            print(random.choice(jokes))

        print("\nAnd some affirmations to boost your spirits:")
        for i in range(1, 4):
            print(random.choice(affirmations))

    def ask_mood(self):
        a=1
        while True:
            mood = input("How are you feeling now? (good/bad): ").lower()
            if mood == 'good':
                print("Glad to hear that your mood is good!")
                self.login_form()
                break
            elif mood == 'bad':
                print("I am Sorry to hear that. Let me tell you another joke to brighten your mood : ")
                self.tell_jokes_and_affirmations()
            else:
                print("Invalid Input")
                exit()
            
            a=a+1
            #print(a)
            if a>3:
                print('Ok, Bye. Hpe for the best')
                exit()
                
    def login_form(self):
        try:
            with open('dataset.json', 'r') as json_file:
                existing_dataset = json.load(json_file)
        except FileNotFoundError:
            existing_dataset = []

    # Collect new details for one person
        print("\nEnter Registration Details : ")
        a = input("Enter Your Full Name : ")
        c = input("Enter Your Email : ")
        b= input('Enter user name: ')
        d = input("Enter Password : ")

        #key = Fernet.generate_key()
        #fernet = Fernet(key)
        #dNew = fernet.encrypt(d.encode())

        #decMessage = fernet.decrypt(dNew).decode()
        #print(decMessage)
        #print(dNew)

        #Password encrpytion
        encmsg = ""
        for ch in d:
            asc = ord(ch) + 3
            ench = chr(asc)
            encmsg += ench

        decmsg=""
        for ch in encmsg:
            asc = ord(ch) - 3
            dnch = chr(asc)
            decmsg += dnch

       # print(decmsg)

    # Check if the new user already exists in the dataset based on email and password
        user_exists = any(user["Email"] == c and user["Password"] == encmsg for user in existing_dataset)

        if user_exists:
            print("User with the same email and password already exists in the dataset.")
        else:
        # Append new data to the existing dataset
            new_data = [{"Name": a, "Email": c, "User name": b,"Password": encmsg}]
            combined_dataset = existing_dataset + new_data

        # Save the combined dataset to the JSON file
            with open('dataset.json', 'w') as json_file:
                json.dump(combined_dataset, json_file, indent=2)
                print("User added successfully.")


        ans1=input('\n\nDo you want further conversation?: ')

        # add morling 20th. want second conversation or not
        if ans1=='y':
            with open('main.py', 'r') as file:
                s10 = file.read()
            exec(s10)
        else:
            print('Ok, Bye')


if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.run()

